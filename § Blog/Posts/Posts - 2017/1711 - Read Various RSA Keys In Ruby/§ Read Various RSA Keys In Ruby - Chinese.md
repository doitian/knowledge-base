---
comment: true
date: 2017-11-18 02:46:10
description: 简单介绍各种 Key 格式，以及如何在 Ruby 中读取
katex: false
share: true
title: Ruby 中读取各种 RSA Keys
tags:
- cryptography
- openssl
- rsa
- ruby
---

# Read Various RSA Keys In Ruby

最近在一个 Ruby on Rails 项目中需要集成各种支付系统。这些系统多使用 RSA 进行加密和签名验证。不过提供的 RSA Key 格式公式个样，所以把各种格式和如何在 Ruby 中读取整理了一下。

RSA 是非对称加密算法，需要 2 个 Keys, 私钥和公钥。Key 本身就是二进制字符串，不过会被编码成各种格式。

<!--more-->

# DER/PEM

DER 是一种二进制编码方案，如果用编辑器查看就是乱码。文件后缀一般是 `.cer`, `.crt`, 或者 `.der`.

PEM 使用 base64 编码，然后在前后添加 PEM 头和尾。比如

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAx4c0F2TEoSe7wMBnn4WA
CSWQZL82eJJG3g128dE1BAMPAcSx0yaLWAEZJ0iZh9q14YND4kh7Or1hkV+beJfo
1c7DjO+VA31l9Nzdps/jGzkxa926VlFoXlLHngBn+zglfmXrhlVNVle/6asDrW49
p8LlLBZHqi/P72f9WUlAa7q45XXY48OqgsJ4ok2Xo0ZbLL9EHAu1GyfGFkBOsnOz
pqJe/aE0gltk+O7dKlVS1bGwm9cwx2eo+mEbH7NgbUm/by/OJKFx1SDbMIJRFcUj
WlosuKfzzkafH4i+z7n07s+StQ6kW5TcZbVVeQPjyzPdWeKvTRZMIvHV3ANVll+i
YQIDAQAB
-----END PUBLIC KEY-----
```

这种格式很常见，比如 `ssh-keygen` 生成的私钥就是 PEM 格式。PEM 文件后缀一般是 `.pem`.

DER 和 PEM 都可以使用下面的方法读取

```ruby
k = OpenSSL::PKey::RSA.new(File.read("/path/to/keyfile"))
```

如果 Key 设置了 passphrase，可以通过第二个参数指定。

通过方法 `k.private?` 可以知道是否是私钥。公钥始终是可用的，因为可以通过私钥计算出公钥。

有时候，提供的 Key 只是使用 base64 编码，但是没有加 PEM 头和尾。这种情况有俩种处理方案：

1. 先 Base64 解码，然后作为 Key 内容读取

    ```ruby
    k = OpenSSL::PKey::RSA.new(Base64.decode64(key_content))
    ```

2. 格式化成 PEM 格式再读取

    ```ruby
    pem = key_content.gsub("\r\n", "").scan(/.{1,64}/).join("\n")
    # or use BEGIN PRIVATE KEY
    pem = "-----BEGIN PUBLIC KEY-----\n#{pem}\n-----END PUBLIC KEY-----\n"
    k = OpenSSL::PKey::RSA.new(pem)
    ```

# PKCS12

PKCS12 文件后缀一般是 `.p12` 或者 `.pfx`. 浏览器导出证书一般会提供该格式。大部分 PKCS12 文件都加了密码保护，可以通过第二个可选参数指定。

```ruby
pkcs12 = OpenSSL::PKCS12.new(key_content, certificate_password)
k = pkcs12.key
```

# X509 Certificate

X509 Certificate 编码 Key 的同时添加了很多信息，比如证书签发者，过期时间等。X509 一般使用 PEM 或 DER 编码，后缀一般是 `.cer`。如果使用 PEM 格式，头一般是 `BEGIN CERTIFICATE`.

X509 Certificate 可以使用下面代码读取

```ruby
cert = OpenSSL::X509::Certificate.new(File.read("/path/to/certfile"))
k = cert.public_key
```

因为容易和 PEM/DER 直接编码的 Key 搞混，如果出现 `asn1 error` 的异常，可以尝试在 `OpenSSL::X509::Certificate` 和 `OpenSSL::PKey::RSA` 之间切换。
