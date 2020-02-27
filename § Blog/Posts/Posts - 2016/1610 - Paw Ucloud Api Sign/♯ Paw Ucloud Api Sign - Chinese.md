---
date: 2016-10-25
title: Paw 里进行 UCloud API 签名验证
---

# Paw Ucloud Api Sign

#powerTool #api

UCloud API 需要把所有请求参数[拼接起来进行签名](https://docs.ucloud.cn/api/summary/signature)。在 [Paw](https://paw.cloud) 中测试 API 时可以添加 URL Params 参数 Signature，使用 JS Script 的 Dynamic Value 进行拼接，组装上 private key 之后再用内置的 SHA1 就能得到最终的签名了。

拼接使用的 JavaScript 代码如下：

```
// context docs: https://paw.cloud/docs/reference/ExtensionContext
// request docs: https://paw.cloud/docs/reference/Request

function evaluate(context){
    var req = context.getCurrentRequest();
    return req.getUrlParametersNames().filter(function(k) { return k != "Signature" }).sort().map(function(k) {
        return k + req.getUrlParameterByName(k);
    }).join("");
}
```

Paw 会提示 URL Params 使用 JS Script 会有递归依赖的问题，忽略掉就可以。不过注意在上面的 JavaScript 代码中需要跳过 Signature 参数。
