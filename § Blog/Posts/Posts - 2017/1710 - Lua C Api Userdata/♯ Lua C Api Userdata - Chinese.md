---
date: '2017-10-29T16:58:27+08:00'
description: 介绍 Lua C API 中的 userdata 和 light userdata
series:
- Lua C API
title: Lua C API userdata 和 light userdata
toc: true
---

# Lua C Api Userdata

#lua

填半年前挖的坑。分享 Lua C API 中的 userdata 和 light userdata。

在编程过程中，经常会需要给一块数据分配一个唯一句柄，通过句柄能够读取或者操作这块数据。原因主要有：

- 数据内聚性很强，封装在一起方便传递，减少参数数量。
- 隐藏数据的内部结构，通过 API 提供操作接口。
- 减少数据拷贝。

最典型的就是 C 中的指针了。但句柄并不一定就必须是指针，比如 Linux 系统中的 fd 可以当作是 IO 设备的句柄。

在 Lua C API 中提供了 userdata 和 light userdata 可以让 C 返回一个句柄给 Lua，而 Lua 可以将句柄再通过在 C 中注册的方法传回 C。

/lua-c-api-userdata.png "Lua Userdata"

<!--more-->

## 区别

Userdata 和 light userdata 的区别是 Userdata 通过 Lua API 分配一片内存，这片内存通过 Lua GC 自动回收。而 light userdata 只是一个 `void *` 类型的值，具体这个值怎么产生，怎么回收需要自己管理。

虽说叫 light userdata，但是其实 Userdata 也是非常轻量的，相比 light userdata 只是多了内存分配和 GC 时的内存回收。因为自动回收的特性，特别适合数据生命周期和 userdata 对象在 Lua 中存活周期一致的场景。

而 light userdata 适合数据周期大于 userdata 对象存活周期的场景，在 Lua 中只是获得数据的引用，但是并不管理数据的生命周期。比如在 Cocos2d-X 中有自己的 GC 机制，所以应该使用 light userdata 将 node 的指针返回给 Lua。还有一种情况是句柄并不是指针，但是可以强转成 `void*` 也是可以通过 light userdata 的，比如将 fd 封装成 light userdata，比如在没有 64 位整数的 Lua 版本但 `void*` 是 64 位的环境下实现 64 位整数库。

另一个区别是整个 Lua 虚拟机中的所有 light userdata 是共享一个元表的，而 userdata 可以单独设置。如果需要元表也必须使用 userdata。

## 示例

以下所有示例代码和编译脚本都可以在该 [Git 仓库的 userdata 分支](https://coding.net/u/doitian/p/lua-c-api-intro/git/tree/userdata/)找到。

### Userdata 示例

Userdata 的 API 主要是 `lua_newuserdata` 和 `lua_touserdata`。

以实现简单的复数为例，创建时调用 `lua_newuserdata` 分配内存并把新的 userdata 压入栈。然后通过返回的内存指针进行初始化。


※ [userdata.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/userdata/userdata.c)

``` c
struct Complex {
  lua_Number real;
  lua_Number imag;
};

typedef struct Complex Complex;

static int complex_new(lua_State* L) {
  Complex* comp = lua_newuserdata(L, sizeof(Complex));
  comp->real = lua_tonumber(L, 1);
  comp->imag = lua_tonumber(L, 2);
  return 1;
}
```

通过  `lua_touserdata` 获得栈上的 userdata 对应的内存指针。下面是俩个复数相加返回一个新的复数的例子

``` c
static int complex_add(lua_State* L) {
  Complex* a = lua_touserdata(L, 1);
  Complex* b = lua_touserdata(L, 2);
  Complex* comp = lua_newuserdata(L, sizeof(Complex));
  comp->real = a->real + b->real;
  comp->imag = a->imag + b->imag;
  return 1;
}
```


### Light userdata 示例


Light userdata 的 API 主要是 `lua_pushlightuserdata` 和 `lua_touserdata`。注意获取栈上的 userdata 或者 light userdata 对应的指针式相同的 API。

以封装 C FILE API 为例，打开文件时将 `FILE *` 作为 lightuser data 返回。这里因为 `FILE *` 是由 libc 来管理生命周期的，所以不能使用 `lua_newuserdata` 来分配内存再初始化。

※ [light_userdata.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/userdata/light_userdata.c)

``` c
static int file_open(lua_State* L) {
  const char* path = lua_tostring(L, 1);
  const char* mode = "w+";
  FILE* file = fopen(path, mode);
  if (file == NULL) {
    lua_pushstring(L, strerror(errno));
    lua_error(L);
    return 0;
  }
  lua_pushlightuserdata(L, file);
  return 1;
}
```

为了释放资源，必须提供相应的 API，在使用完毕时调用。

```c
static int file_close(lua_State* L) {
  FILE* f = lua_touserdata(L, 1);
  if (f != NULL) {
    fclose(f);
  }
  return 0;
}
```

当然这个例子中，更安全的方法是用 userdata，把 FILE* 设置在 userdata 分配的内存中，并通过元表设置在 GC 是自动调用 `fclose`。
