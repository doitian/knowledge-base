---
comment: true
date: '2017-11-18T10:46:07+08:00'
description: "Introduce how to read various public/private key in Ruby"
katex: false
share: true
title: Read Various RSA Keys in Ruby
---

# Read Various RSA Keys in Ruby

#ruby

I recently worked in a Ruby on Rails project which should integrate with many different payment systems. There system mostly use RSA in encryption and signature. However they provide the RSA keys in different formats, it is a challenge to choose a right way to read the keys in Ruby.

RSA is an asymmetric cryptographic algorithm, thus it requires two keys, private key and public key. The key itself is just binary, but it can be encoded in different format.

<!--more-->

# DER/PEM

DER is a binary encoding method. It is consisted of unreadable characters. The extension is usually `.cer`, `.crt`, or `.der`.

PEM encode key using base64, then add PEM header and footer around key. For example

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

This is the most frequently used format, since `ssh-keygen` generate private key in PEM format. The PEM key file extension is usually `.pem`.

Both DER and PEM format can be read in Ruby using following code:

```ruby
k = OpenSSL::PKey::RSA.new(File.read("/path/to/keyfile"))
```

If the key file has a passphrase, it can be specified as the second argument.

The method `k.private?` can be used to check whether the key is a private key. Since public key can be calculated from private key, public key is always available.

Sometimes, the key is provided just in base64 format without PEM header. There are two solutions:

1. Base64 decode the string and pass it as key content

    ```ruby
    k = OpenSSL::PKey::RSA.new(Base64.decode64(key_content))
    ```

2. Format it using PEM and then read the key

    ```ruby
    pem = key_content.gsub("\r\n", "").scan(/.{1,64}/).join("\n")
    # or use BEGIN PRIVATE KEY
    pem = "-----BEGIN PUBLIC KEY-----\n#{pem}\n-----END PUBLIC KEY-----\n"
    k = OpenSSL::PKey::RSA.new(pem)                        
    ```

# PKCS12

PKCS12 key file extension is usually `.p12` or `.pfx`. It is a frequently used format in browsers to export certificates. Most PKCS12 files are protected using password, which is the optional second argument in the constructor.

```ruby
pkcs12 = OpenSSL::PKCS12.new(key_content, certificate_password)
k = pkcs12.key
```

# X509 Certificate

X509 Certificate adds some meta information to key, such as issuer, expiration date. X509 can be encoded using DER or PEM, the key file extension is usually `.cer`. In PEM format, the header is `BEGIN CERTIFICATE`.

X509 Certificate can be read as following:

```ruby
cert = OpenSSL::X509::Certificate.new(File.read("/path/to/certfile"))
k = cert.public_key
```

When asn1 error is thrown, try switch between `OpenSSL::X509::Certificate` and `OpenSSL::PKey::RSA`.

