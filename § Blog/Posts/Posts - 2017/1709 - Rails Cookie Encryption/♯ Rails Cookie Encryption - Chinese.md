---
comment: true
date: 2017-09-23 07:47:49
description: 如何解密 Rails Cookie，从而跨服务跨语言共享 Rails session。
katex: false
share: true
title: Rails Cookie 如何解密
---

# Rails Cookie Encryption

#rails #encryption

{{TOC}}

如果想在已有的 Rails app 上使用其它语言加些 API，同时能直接使用 Rails 的登陆信息，最简单的就是用 Nginx 等代理将不同的服务映射到相同的域名下，其它的 App 解密 Cookie 获得登陆信息。

本文以 Ruby 代码为例说明 Rails 的 Cookie 是如何加密，然后以 Go 为例说明如何解密的。

/rails-cookie-encryption.png "Rails Cookie 加密"

<!--more-->

Rails 的实现可以参考 [ActiveSupport::MessageEncryptor](https://github.com/rails/rails/blob/0a6f69a5debf89748da3a43747c61d201095997e/activesupport/lib/active_support/message_encryptor.rb)，[ActiveSupport::MessageVerifier](https://github.com/rails/rails/blob/0a6f69a5debf89748da3a43747c61d201095997e/activesupport/lib/active_support/message_verifier.rb) 和相应的单元测试。

## 加密

上图说明了原始的 Session 对象 *Session Data* 是如何最终生成 Cookie 的。如果登陆用了 [Devise](https://github.com/plataformatec/devise)，那么 Session Data 中的登陆信息保存在 `warden.user.user.key` 中。之后就用下面例子说明加密。

```ruby
session = { "warden.user.user.key" => [[1],"secret"] }
```

### ① Cookie Serializer

从 Rails 4.1 开始，默认使用的 JSON，4.1 之前使用的 Ruby Marshal。为了方便其它语言中解析，推荐使用 4.1 或更新的版本并使用 JSON 做为 Cookie 的 serializer。配置在 `config/initializers/cookies_serializer.rb` 中

```ruby
Rails.application.config.action_dispatch.cookies_serializer = :json
```

JSON 的 serializer 就很直接了

```ruby
require 'json'
session_json = JSON.dump(session)
puts session_json.inspect
# => "{\"warden.user.user.key\":[[1],\"secret\"]}"
```

### ② Padding

下一步的加密要求数据的字节数必须是 16 的倍数，用的算法是 [PKCS7](https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7)。简单说就是如果差 n 个字节到下个 16 的倍数就补 n 个 n。如果刚好是 16 的倍数就补 16 个 16。

```ruby
def padding(data, block_size = 16)
  n = block_size - data.bytesize % block_size
  return data.force_encoding('ASCII-8BIT') + n.chr * n
end
padded_session = padding(session_json)
puts padded_session.inspect
# => "{\"warden.user.user.key\":[[1],\"secret\"]}\t\t\t\t\t\t\t\t\t"
```

末尾的 `\t` ASCII 码是 9，表示补了 9 个字节。

### ③ 加密 AES-CBC

这一步是最主要的加密了，算法是 AES-CBC。加密需要配置密钥并随机生成 IV (initialization vector)。因为 Ruby 的 OpenSSL::Cipher 封装会自动 padding，所以可以跳过第 ② 步。

我们知道 Rails 需要配置 secret key base，密钥就是通过 secret key base 和 salt 产生的，使用的算法 `pbkdf2` 在 OpenSSL 里也提供了。

```ruby
OpenSSL::PKCS5.pbkdf2_hmac_sha1(pass, salt, iter, keylen)
```

- `pass` 配置中的 secret key base
- `salt` 如果使用默认 Rails 配置的话，加密是 `encrypted cookie`，后面签名步骤是 `signed encrypted cookie`
- `iter` 默认是 1000, `keylen` 加密是 32，签名是 64。也可以统一用 64，但是加密的 Key 只取前 32 个字节。

```ruby
require 'openssl'
SECRET_KEY_BASE = "development_secret"
DEFAULT_SALT     = "encrypted cookie"
DEFAULT_SIGN_SALT = "signed encrypted cookie"
DEFAULT_ITER = 1000
DEFAULT_KEYLEN = 64
def generate_key(secret_key_base, salt, iter = DEFAULT_ITER, keylen = DEFAULT_KEYLEN)
  OpenSSL::PKCS5.pbkdf2_hmac_sha1(secret_key_base, salt, iter, keylen)
end

encrypt_key = generate_key(SECRET_KEY_BASE, DEFAULT_SALT)[0...32]
puts Base64.strict_encode64(encrypt_key)
# => vozBHj31liL/p88es/k7aywa4Po4mwMVkW/eqhFjw/4=
```

IV 是随机的 16 个字节。解密的时候需要用到，所以需要保存起来下一步拼装的时候用。可以用 `SecureRandom.random_bytes` 或者 `OpenSSL::Cipher.random_iv`。

使用 OpenSSL 实现如下，IV 应该要随机的，为了方便对照，直接用了 16 个 0

```ruby
encrypt_key = generate_key(SECRET_KEY_BASE, DEFAULT_SALT)[0...32]
puts Base64.strict_encode64(encrypt_key)

cipher = OpenSSL::Cipher.new("aes-256-cbc")
cipher.encrypt
cipher.key = encrypt_key

iv = "\0" * 16
# iv = cipher.random_iv

encrypted_content = cipher.update(session_json)
encrypted_content << cipher.final
puts Base64.strict_encode64(encrypted_content)
# => t7c1ncaCXhZAOPRtX0BI8eceOmx/Qg3Jrg6uwmgJuSNosKIc7M4KRfOw1q3mFWv7ZSiNO3ZRPxJMGI1cDvu+PQ==
```

### ④ 拼装加密内容和 IV

得到 `encrypted_content ` 和 `iv` 后，分别 base64 后用 `--` 连接，然后再做一次 base64 得到 `encrypted_data`

```ruby
encrypted_data = Base64.strict_encode64(
  Base64.strict_encode64(encrypted_content) +
  "--" +
  Base64.strict_encode64(iv)
)
puts encrypted_data
# => dDdjMW5jYUNYaFpBT1BSdFgwQkk4ZWNlT214L1FnM0pyZzZ1d21nSnVTTm9zS0ljN000S1JmT3cxcTNtRld2Ny0tQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT09
```

### ⑤ 签名 HMAC-SHA1

签名用的 `HMAC-SHA1`，结果转成 16 进制字符串。Key 参考 加密步骤中的说明。

```ruby
sign_key = generate_key(SECRET_KEY_BASE, DEFAULT_SIGN_SALT)
sign = OpenSSL::HMAC.hexdigest(OpenSSL::Digest::SHA1.new, sign_key, encrypted_data)
puts sign
# => 75d8323b0f0e41cf4d5aabee1b229b1be76b83b6
```

### ⑥ 拼装签名

最后把 `encrypted_data` 和 `sign` 用 `--` 连接然后做一次 URL Query Escape 就可以了

```ruby
require "uri"
cookie_content = URI.encode_www_form_component(encrypted_data + "--" + sign)
puts cookie_content
# => dDdjMW5jYUNYaFpBT1BSdFgwQkk4ZWNlT214L1FnM0pyZzZ1d21nSnVTTm9zS0ljN000S1JmT3cxcTNtRld2Ny0tQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT09--75d8323b0f0e41cf4d5aabee1b229b1be76b83b6
```

完整的代码: [rails-cookie-encrypt.rb](https://gist.github.com/doitian/2a89dc9e4372e55335c9111f576b47bf#file-rails-cookie-encrypt-rb)

如果用 `ActiveSupport` 可以简化成

```ruby
require "active_support/key_generator"
require "active_support/message_encryptor"
encrypt_key = ActiveSupport::KeyGenerator.new(SECRET_KEY_BASE, iterations: DEFAULT_ITER).generate_key(DEFAULT_SALT, 32)
sign_key = ActiveSupport::KeyGenerator.new(SECRET_KEY_BASE, iterations: DEFAULT_ITER).generate_key(DEFAULT_SIGN_SALT, 64)
encryptor = ActiveSupport::MessageEncryptor.new(encrypt_key, sign_key, serializer: JSON)
puts encryptor.encrypt_and_sign(session)
```

## 解密

解密就是把 6 个步骤反过来，输入就是

```go
cookieContent := "dDdjMW5jYUNYaFpBT1BSdFgwQkk4ZWNlT214L1FnM0pyZzZ1d21nSnVTTm9zS0ljN000S1JmT3cxcTNtRld2Ny0tQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT09--75d8323b0f0e41cf4d5aabee1b229b1be76b83b6"
```

### ⑥ 分离签名

URL Query Unescape 然后以 `--` 分成 `encryptedData` 和 `sign`

```go
var err error
var unescapedCookieContent string
if unescapedCookieContent, err = url.QueryUnescape(cookieContent); err != nil {
  panic(err)
}
encryptedDataSignVectors := strings.SplitN(unescapedCookieContent, "--", 2)
encryptedData := encryptedDataSignVectors[0]
sign := encryptedDataSignVectors[1]
fmt.Printf("encrypted_data = %v\n", encryptedData)
fmt.Printf("sign = %v\n", sign)
// => encrypted_data = dDdjMW5jYUNYaFpBT1BSdFgwQkk4ZWNlT214L1FnM0pyZzZ1d21nSnVTTm9zS0ljN000S1JmT3cxcTNtRld2Ny0tQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT09
// sign = 75d8323b0f0e41cf4d5aabee1b229b1be76b83b6
```

### ⑤ 验证签名

验证签名其实就是再签一次然后对比结果。为了安全，可以使用 `hmac.Equal` 来比较签名是否一致。

Key 的生成可以使用 `golang.org/x/crypto/pbkdf2`

```go
const (
  keyIterNum = 1000
  keySize    = 64
)

func generateKey(base, salt string) []byte {
  return pbkdf2.Key([]byte(base), []byte(salt), keyIterNum, keySize, sha1.New)
}
```

验证实现如下

```go
secretKeyBase := "development_secret"
defaultSignSalt := "signed encrypted cookie"
signKey := generateKey(secretKeyBase, defaultSignSalt)
signHmac := hmac.New(sha1.New, signKey)
signHmac.Write([]byte(encryptedData))
verifySign := signHmac.Sum(nil)
fmt.Printf("verifySign = %v\n", hex.EncodeToString(verifySign))
// verifySign = 75d8323b0f0e41cf4d5aabee1b229b1be76b83b6
var signDecoded []byte
if signDecoded, err = hex.DecodeString(sign); err != nil {
  panic(err)
}
if !hmac.Equal(verifySign, signDecoded) {
  panic(fmt.Errorf("verification failed"))
}
```

### ④ 分离加密内容和 IV

Base64 解码一次，用 `--` 分离并分别 Base64 解码得到 `encryptedContent`  和  `iv` 

```go
var encryptedDataBase64Decoded []byte
if encryptedDataBase64Decoded, err = base64.StdEncoding.DecodeString(encryptedData); err != nil {
  panic(err)
}
encryptedContentIvVectors := strings.SplitN(string(encryptedDataBase64Decoded), "--", 2)
var encryptedContent []byte
var iv []byte
if encryptedContent, err = base64.StdEncoding.DecodeString(encryptedContentIvVectors[0]); err != nil {
  panic(err)
}
if iv, err = base64.StdEncoding.DecodeString(encryptedContentIvVectors[1]); err != nil {
  panic(err)
}
fmt.Printf("encrypted_content = %s\n", base64.StdEncoding.EncodeToString(encryptedContent))
fmt.Printf("iv = %v\n", iv)
// encrypted_content = t7c1ncaCXhZAOPRtX0BI8eceOmx/Qg3Jrg6uwmgJuSNosKIc7M4KRfOw1q3mFWv7
// iv = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
```

### ③ 解密

用 Key 和 iv 来解密

```go
defaultSalt := "encrypted cookie"
encryptKey := generateKey(secretKeyBase, defaultSalt)[:32]
c, err := aes.NewCipher(encryptKey)
if err != nil {
  panic(err)
}

cfb := cipher.NewCBCDecrypter(c, iv)
paddedSession := make([]byte, len(encryptedContent))
cfb.CryptBlocks(paddedSession, encryptedContent)
fmt.Printf("padded_session = %s\n", strconv.QuoteToASCII(string(paddedSession)))
// padded_session = "{\"warden.user.user.key\":[[1],\"secret\"]}\t\t\t\t\t\t\t\t\t"
```

### ② Un-padding

去除 padding 只需要看最后一个字节是多少就移除多少个字节。

```go
padding := int(paddedSession[len(paddedSession) - 1])
sessionJSON := string(paddedSession[:(len(paddedSession) - padding)])
fmt.Printf("session_json = %s\n", sessionJSON)
// session_json = {"warden.user.user.key":[[1],"secret"]}
```

### ① Cookie Deserializer

如果是 JSON 用 go JSON 库解析就可以了。如果是 Ruby Marshal 也不用完整实现，可以用正则提取需要的信息。

```go
var jsonData map[string]interface{}
if err := json.Unmarshal([]byte(sessionJSON), &jsonData); err != nil {
  panic(err)
}
fmt.Printf("%+v\n", jsonData)
// map[warden.user.user.key:[[1] secret]]
```

完整的代码: [rails-cookie-decrypt.go](https://gist.github.com/doitian/2a89dc9e4372e55335c9111f576b47bf#file-rails-cookie-decrypt-go)

如果 Rails 里用的 Devise，可以在 `config/initializers/devise.rb` 增加下面的配置来在 Cookie 中包含更多的字段，比如用户名或邮箱

```ruby
Warden::Manager.after_authentication do |user, auth, opts|
  auth.raw_session['warden.user.user.email'] = user.email
end
```

需要用户重新登陆或者更换 secret key base 才会生效。
