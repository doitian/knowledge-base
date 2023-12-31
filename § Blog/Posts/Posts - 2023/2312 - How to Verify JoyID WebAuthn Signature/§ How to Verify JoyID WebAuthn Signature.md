---
date: 2023-12-17T17:35:33+0800
draft: false
description: This post shows how to verify the signature from the method signChallenge of the `@joyid/ckb` package using using the OpenSSL command line and the Python library PyCryptodome
tags:
  - cryptography
---
# How to Verify JoyID WebAuthn Signature

**Status**:: #x
**Tags**:: #evergreen
**Zettel**:: #zettel/permanent
**Created**:: [[2023-12-17]]
**Reference**:: [[PyCryptodome]], [[JoyID]], [[OpenSSL]]

[JoyID](https://docs.joy.id/guide) is a multichain, cross-platform, passwordless and mnemonic-free wallet solution based on FIDO WebAuthn protocol and Nervos CKB.

This post shows how to verify the signature from the method [signChallenge][] of the `@joyid/ckb` package. The method reference page has a demo. I use the demo to obtain an example response then verify the response using the OpenSSL command line and the Python library [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html).

[signChallenge]: https://docs.joy.id/guide/ckb/sign-message

The JoyID follows the WebAuthn specification and employs secp256r1 for signing. Although the guide references [section 6.3.3](https://www.w3.org/TR/webauthn-2/#sctn-op-get-assertion) of the WebAuthn specification, titled "The authenticatorGetAssertion Operation", I discovered that the example in [this repository](https://github.com/duo-labs/py_webauthn/blob/master/webauthn/authentication/verify_authentication_response.py) provided me much more helps.

<!--more-->

## The Response Parsing

This is the example I obtained from the demo.

```json
{
  "signature": "MEUCICF25qdO6nLreEoBHnyaw-9R6XFHbIu-NwsAI53t016qAiEAgmhlwTEMxoWxKj79R1rUkB_6nrhJfws82DqHkY_HnqQ",
  "message": "K4sF4fAwPvuJj-TW3mARmMenuGSrvmohxzsueH4YfFIFAAAAAHsidHlwZSI6IndlYmF1dGhuLmdldCIsImNoYWxsZW5nZSI6IlUybG5iaUIwYUdseklHWnZjaUJ0WlEiLCJvcmlnaW4iOiJodHRwczovL3Rlc3RuZXQuam95aWQuZGV2IiwiY3Jvc3NPcmlnaW4iOmZhbHNlLCJvdGhlcl9rZXlzX2Nhbl9iZV9hZGRlZF9oZXJlIjoiZG8gbm90IGNvbXBhcmUgY2xpZW50RGF0YUpTT04gYWdhaW5zdCBhIHRlbXBsYXRlLiBTZWUgaHR0cHM6Ly9nb28uZ2wveWFiUGV4In0",
  "challenge": "Sign this for me",
  "alg": -7,
  "pubkey": "3538dfd53ad93d2e0a6e7f470295dcd71057d825e1f87229e5afe2a906aa7cfc099fdfa04442dac33548b6988af8af58d2052529088f7b73ef00800f7fbcddb3",
  "keyType": "main_key"
}
```

### pubkey

The `pubkey` field represents the uncompressed public key concatenating two 32-byte integers in hex. PyCryptodome can import the key by prepending the flag `0x04`. OpenSSL uses PEM to encode keys, and PyCryptodome can help here to export the key in PEM format.

```python
from Crypto.PublicKey import ECC

pubkey_raw_hex = "3538dfd53ad93d2e0a6e7f470295dcd71057d825e1f87229e5afe2a906aa7cfc099fdfa04442dac33548b6988af8af58d2052529088f7b73ef00800f7fbcddb3"
pubkey = ECC.import_key(bytes.fromhex("04" + pubkey_raw_hex), curve_name="secp256r1")
with open("pubkey.pem", "wt") as pemfile:
    pemfile.write(pubkey.export_key(format="PEM"))
```

Double check the key using OpenSSL:

```shell-session
$ openssl ec -text -inform PEM -in pubkey.pem -pubin
...
Public-Key: (256 bit)
pub:
    04:35:38:df:d5:3a:d9:3d:2e:0a:6e:7f:47:02:95:
    dc:d7:10:57:d8:25:e1:f8:72:29:e5:af:e2:a9:06:
    aa:7c:fc:09:9f:df:a0:44:42:da:c3:35:48:b6:98:
    8a:f8:af:58:d2:05:25:29:08:8f:7b:73:ef:00:80:
    0f:7f:bc:dd:b3
ASN1 OID: prime256v1
NIST CURVE: P-256
...
```

### message

The `message` is a binary encoded by base64 [RFC 4648 §5](https://datatracker.ietf.org/doc/html/rfc4648#section-5) without the equal sign (`=`) paddings. Many base64 tools and libraries require padding equal sign (`=`)  in the end of the string to make the length multiple of 4. The `message` in the example response has a length 351, which requires one `=` padding. A trick is always padding two equals at the end of the string before decoding.

The first 37 bytes in `message` are authenticator data, and the following bytes are client data in JSON.

The section [section 6.1](https://www.w3.org/TR/webauthn-2/#sctn-authenticator-data) in the WebAuthn specification defines the layout of the authenticator data.

- `rpIdHash`, 32 bytes: the sha256 checksum of the text `testnet.joyid.dev`
- `flags`, 1 byte: `0x05` in JoyID
- `signCount`, 4 bytes: all zeros

```shell
base64 -d <<<'
K4sF4fAwPvuJj-TW3mARmMenuGSrvmohxzsueH4YfFIFAAAAAHsidHlwZSI6Indl
YmF1dGhuLmdldCIsImNoYWxsZW5nZSI6IlUybG5iaUIwYUdseklHWnZjaUJ0WlEi
LCJvcmlnaW4iOiJodHRwczovL3Rlc3RuZXQuam95aWQuZGV2IiwiY3Jvc3NPcmln
aW4iOmZhbHNlLCJvdGhlcl9rZXlzX2Nhbl9iZV9hZGRlZF9oZXJlIjoiZG8gbm90
IGNvbXBhcmUgY2xpZW50RGF0YUpTT04gYWdhaW5zdCBhIHRlbXBsYXRlLiBTZWUg
aHR0cHM6Ly9nb28uZ2wveWFiUGV4In0=' |
  dd bs=1 count=37 2>/dev/null |
  xxd
#=> 00000000: 2b8b 05e1 f030 3efb 898f e4d6 de60 1198
#=> 00000010: c7a7 b864 abbe 6a21 c73b 2e78 7e18 7c52
#=> 00000020: 0500 0000 00
```

Check the first two lines with the sha256 checksum:

```shell
echo -n 'testnet.joyid.dev' | sha256sum
#=> 2b8b05e1f0303efb898fe4d6de601198c7a7b864abbe6a21c73b2e787e187c52  -
```

The client data JSON looks like this:

```shell
base64 -d <<<'
K4sF4fAwPvuJj-TW3mARmMenuGSrvmohxzsueH4YfFIFAAAAAHsidHlwZSI6Indl
YmF1dGhuLmdldCIsImNoYWxsZW5nZSI6IlUybG5iaUIwYUdseklHWnZjaUJ0WlEi
LCJvcmlnaW4iOiJodHRwczovL3Rlc3RuZXQuam95aWQuZGV2IiwiY3Jvc3NPcmln
aW4iOmZhbHNlLCJvdGhlcl9rZXlzX2Nhbl9iZV9hZGRlZF9oZXJlIjoiZG8gbm90
IGNvbXBhcmUgY2xpZW50RGF0YUpTT04gYWdhaW5zdCBhIHRlbXBsYXRlLiBTZWUg
aHR0cHM6Ly9nb28uZ2wveWFiUGV4In0=' |
  dd bs=1 skip=37 2>/dev/null |
  jq
{
  "type": "webauthn.get",
  "challenge": "U2lnbiB0aGlzIGZvciBtZQ",
  "origin": "https://testnet.joyid.dev",
  "crossOrigin": false,
  ...
}
```

Notice the `challenge` field. It is the parameter passed to `signChallenge`, in base64.

```shell
base64 -d <<<'U2lnbiB0aGlzIGZvciBtZQ=='
#=> Sign this for me
```

Attention that message is not the binary to be signed. According to the Figure 4, Generating an assertion signature, in [the WebAuthn specification](https://www.w3.org/TR/webauthn-2/#sctn-authenticator-data), the binary to be signed is a concatenation of the authenticator data and the sha256 checksum of the client data JSON.

The following code shows how to prepare the message to sign and save it into the file `message.bin`. Attention that base64 must use the alternative keys `-` and `_` to replace `+` and `/` respectively.

> [!attention]
> To decode base64 "RFC 4648 §5" in python, use either `base64.b64decode(s, altchars="-_")` or `binascii.urlsafe_b64decode(s)`.

```python
import base64
from Crypto.Hash import SHA256

message_bin = base64.urlsafe_b64decode(
    "K4sF4fAwPvuJj-TW3mARmMenuGSrvmohxzsueH4YfFIFAAAAAHsidHlwZSI6Indl"
    "YmF1dGhuLmdldCIsImNoYWxsZW5nZSI6IlUybG5iaUIwYUdseklHWnZjaUJ0WlEi"
    "LCJvcmlnaW4iOiJodHRwczovL3Rlc3RuZXQuam95aWQuZGV2IiwiY3Jvc3NPcmln"
    "aW4iOmZhbHNlLCJvdGhlcl9rZXlzX2Nhbl9iZV9hZGRlZF9oZXJlIjoiZG8gbm90"
    "IGNvbXBhcmUgY2xpZW50RGF0YUpTT04gYWdhaW5zdCBhIHRlbXBsYXRlLiBTZWUg"
    "aHR0cHM6Ly9nb28uZ2wveWFiUGV4In0==",
)
authenticator_data = message_bin[:37]
client_data = message_bin[37:]
message_to_sign = authenticator_data + SHA256.new(client_data).digest()

with open("message.bin", "wb") as fout:
    fout.write(message_to_sign)
```

> [!attention]
> The `message` in the response is not the binary to be signed. Instead, the binary to be signed is a concatenation of the authenticator data and the sha256 checksum of the client data JSON.

### signature

The field signature are two 32-byte integers first encoded in [DER][], then base64 [RFC 4648 §5](https://datatracker.ietf.org/doc/html/rfc4648#section-5) without the equal sign (`=`) paddings.

[DER]: https://wiki.openssl.org/index.php/DER

Many base64 tools and libraries require padding equal sign (`=`)  in the end of the string to make the length multiple of 4. The signature in the example response has a length 95, which requires one `=` padding.

OpenSSL also stores signature in DER, let's save one in the file `signature.der`:

```
base64 -d <<<"MEUCICF25qdO6nLreEoBHnyaw-9R6XFHbIu-NwsAI53t016qAiEAgmhlwTEMxoWxKj79R1rUkB_6nrhJfws82DqHkY_HnqQ=" > signature.der
```

The command `openssl asn1parse` can parse the file `signature.der` in the DER format.

```bash
openssl asn1parse -dump -inform DER -in signature.der
# Output =>
# 0:d=0  hl=2 l=  69 cons: SEQUENCE
#     2:d=1  hl=2 l=  32 prim: INTEGER           :2176E6A74EEA72EB784A011E7C9AC3EF51E971476C8BBE370B00239DEDD35EAA
#    36:d=1  hl=2 l=  33 prim: INTEGER           :826865C1310CC685B12A3EFD475AD4901FFA9EB8497F0B3CD83A87918FC79EA4
```

PyCryptodome expects the signature of 64 bytes for two 32-byte integers. Following code uses the `asn1` module to extract the raw signature from the DER binary.

```python
import base64
from Crypto.Util.asn1 import DerSequence

signature_der = base64.urlsafe_b64decode(
    "MEUCICF25qdO6nLreEoBHnyaw-9R6XFHbIu-NwsAI53t016qAiEAgmhlwTEMxoWx"
    "Kj79R1rUkB_6nrhJfws82DqHkY_HnqQ=",
)

signature_seq = DerSequence()
signature_seq.decode(signature_der)
print(signature_seq[0].to_bytes(32).hex())
# => 2176e6a74eea72eb784a011e7c9ac3ef51e971476c8bbe370b00239dedd35eaa
print(signature_seq[1].to_bytes(32).hex())
# => 826865c1310cc685b12a3efd475ad4901ffa9eb8497f0b3cd83a87918fc79ea4
```

## Verifying

PyCryptodome:

```python
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

DSS.new(pubkey, "fips-186-3").verify(SHA256.new(message_to_sign), signature)
print("Verified OK")
```

OpenSSL:

```shell
openssl dgst -sha256 -verify pubkey.pem -signature signature.der message.bin
```

> [!code]- Full Python code ([Gist](https://gist.github.com/doitian/b1f5c60203e9dbaffccff7d0920d9529))
>
> ```python
> import base64
> from Crypto.Hash import SHA256
> from Crypto.PublicKey import ECC
> from Crypto.Signature import DSS
> from Crypto.Util.asn1 import DerSequence
>
>
> response = {
>     "signature": "MEUCICF25qdO6nLreEoBHnyaw-9R6XFHbIu-NwsAI53t016qAiEAgmhlwTEMxoWx"
>     "Kj79R1rUkB_6nrhJfws82DqHkY_HnqQ",
>     "message": "K4sF4fAwPvuJj-TW3mARmMenuGSrvmohxzsueH4YfFIFAAAAAHsidHlwZSI6IndlYmF1dGhuLmdldCIsImNoYWxsZW5nZSI6IlUybG5iaUIwYUdseklHWnZjaUJ0WlEiLCJvcmlnaW4iOiJodHRwczovL3Rlc3RuZXQuam95aWQuZGV2IiwiY3Jvc3NPcmlnaW4iOmZhbHNlLCJvdGhlcl9rZXlzX2Nhbl9iZV9hZGRlZF9oZXJlIjoiZG8gbm90IGNvbXBhcmUgY2xpZW50RGF0YUpTT04gYWdhaW5zdCBhIHRlbXBsYXRlLiBTZWUgaHR0cHM6Ly9nb28uZ2wveWFiUGV4In0",
>     "challenge": "Sign this for me",
>     "alg": -7,
>     "pubkey": "3538dfd53ad93d2e0a6e7f470295dcd71057d825e1f87229e5afe2a906aa7cfc099fdfa04442dac33548b6988af8af58d2052529088f7b73ef00800f7fbcddb3",
>     "keyType": "main_key",
> }
>
> pubkey = ECC.import_key(
>     bytes.fromhex("04" + response["pubkey"]),
>     curve_name="secp256r1",
> )
> with open("pubkey.pem", "wt") as fout:
>     fout.write(pubkey.export_key(format="PEM"))
>
> message_bin = base64.urlsafe_b64decode(response["message"] + "==")
> authenticator_data = message_bin[:37]
> client_data = message_bin[37:]
> # https://github.com/duo-labs/py_webauthn/blob/master/webauthn/authentication/verify_authentication_response.py
> message_to_sign = authenticator_data + SHA256.new(client_data).digest()
> with open("message.bin", "wb") as fout:
>     fout.write(message_to_sign)
>
> signature_der = base64.urlsafe_b64decode(response["signature"] + "==")
> with open("signature.der", "wb") as fout:
>     fout.write(signature_der)
> signature_seq = DerSequence()
> signature_seq.decode(signature_der)
> signature = signature_seq[0].to_bytes(32) + signature_seq[1].to_bytes(32)
>
> DSS.new(pubkey, "fips-186-3").verify(SHA256.new(message_to_sign), signature)
> print("Verified OK")
> ```
