---
date: '2017-02-18T05:35:59+08:00'
description: 介绍 Lua C API 使用方法，详细说明了 Lua 栈的操作
series:
- Lua C API
title: Lua C API 简介
---

# Lua C Api Intro

#lua

%%TOC%%

公司主要用 skynet 和 cocos2d-x Lua 来开发游戏。两者都采用了嵌入 Lua 来开发。因为性能，要和原生代码交互等原因，需要在 Lua 和其它语言之间进行交互。最近做了挺多这样的工作，积累了一些心得，会陆续总结分享出来。

这一篇是 Lua C API 的简单介绍。

<!--more-->

使用 Lua C API 有两个场景。一是把 Lua 嵌入在其它语言中，只要能链接 C 库并调用 C 方法都可以使用。另一种是开发 Lua C 模块。

## Lua C API

先介绍如何在 C 中嵌入 Lua。下面的例子中初始化了 Lua 虚拟机，并执行了一段 Lua 代码。

※ [lua-c-api-template.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/master/lua-c-api-template.c)

``` c
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

#define QUOTE(...) #__VA_ARGS__
static const char *lua_code = QUOTE(
  print("Hello, Lua C API")
);

int main(int argc, char* argv[]) {
  int status = 0;

  lua_State *L = luaL_newstate();
  luaL_openlibs(L);

  status = luaL_loadstring(L, lua_code) || lua_pcall(L, 0, 0, 0);
  if (status) {
    fprintf(stderr, "%s", lua_tostring(L, -1));
    lua_pop(L, 1);
  }

  lua_close(L);
  return status;
}
```

上面代码要求使用至少 Lua 5.1，否则 `luaL_newstate` 需要改成 `lua_open`, `luaL_openlibs` 要拆成单独的各个标准库加载方法比如 `luaopen_io`。

编译需要引用 Lua 头文件并链接 Lua 库。本文所有示例和编译脚本都放在 [这个 Git 仓库](https://coding.net/u/doitian/p/lua-c-api-intro/git) 中。

Lua C API 的核心就是操作栈，所有的操作都是通过栈实现的。访问栈可以用正数或者负数。每次函数调用会标记当前栈顶的位置，之后压入的元素位置从 1 开始。下面会提到函数的参数会首先压入栈，所以正数 i 引用的栈位置就是第 i 个参数。负数就是从栈顶开始数的位置，-1 就是栈顶元素，-2 就是栈顶下面一个元素，依此类推。

使用栈要注意，谁负责压入就要负责弹出，很多 Lua C API 出现错误都是栈操作不当引起的。

![[lua_stack.png|Lua 栈]]

查看 C API 的文档重要一部分就是查看其对栈操作的约定。 以设置全局变量的 API `lua_setglobal` 为例

> `void lua_setglobal (lua_State *L, const char *name);`
>
> Pops a value from the stack and sets it as the new value of global name.

执行该方法需要把全局变量的值压入栈，调用成功后会被自动弹出。下面是使用的例子，注释中是等价的 Lua 代码。完整代码点击文件名查看。

※ [globals.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/master/globals.c)

``` c
// g_int = 10
lua_pushinteger(L, 10);
lua_setglobal(L, "g_int");

// g_number = 3.14
lua_pushnumber(L, (lua_Number)3.14);
lua_setglobal(L, "g_number");

// g_true = true
// g_false = false
lua_pushboolean(L, 1);
lua_setglobal(L, "g_true");
lua_pushboolean(L, 0);
lua_setglobal(L, "g_false");

// g_string = "global set from C API"
lua_pushstring(L, "global set from C API");
lua_setglobal(L, "g_string");

// g_table = { name = "table set from C API" }
lua_newtable(L);
lua_pushstring(L, "table set from C API");
lua_setfield(L, -2, "name");
lua_setglobal(L, "g_table");
```

以最复杂的 `g_table` 为例说明栈的变化。

![[lua_setglobal.png|Lua 栈变化示例]]

## Function

### C 中调用 Lua 方法

上面的例子用到了 integer, float, boolean, string, table 等数据类型。Lua 和 C 之间还可以通过函数互调来共享逻辑。

C 中调用 Lua 方法或者其它 C 模块定义的方法可以使用 `lua_call` 或者 `lua_pcall`。

调用的栈约定是一致的，先把要调用的函数入栈，然后按顺序从第 1 个参数开始压入栈，有多个参数的话这个时候栈顶应该是最后一个参数。

然后使用 `lua_call` 或者 `lua_pcall`。需要手动指定参数的个数和要保留的返回结果的个数。和在 Lua 中方法调用相同，指定的个数小于实际返回结果个数的话，多余的被丢弃，指定的个数多于实际个数的话，多出来的赋值 nil。

调用的函数没有出现错误的话，结果是一致的，函数和所有参数被弹出栈，指定数量的返回结果被依次压入栈，也就是最后一个返回结果会在栈顶。

如果出错了，`lua_call` 行为和 Lua 中直接调用一个方法然后出错一致，会直接通过 `longjump` 直接跳到被 `pcall/xpcall` 被捕获的地方。

而 `lua_pcall` 和 `xpcall` 一致

- 如果最后一个参数不为 0，则会调用对应栈位置的函数来处理错误
- 把函数和所有参数弹出栈，再把错误压入栈。

举例说明，首先定义一个方法方便演示

``` lua
function identity(...)
  return table.unpack({...})
end
```

下面是 `lua_call` 和 `lua_pcall` 的例子。

※ [call-lua-function.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/master/call-lua-function.c)

``` c
lua_getglobal(L, "identity"); // identity
lua_pushinteger(L, 1); // identity, 1
lua_call(L, 1, 2);
// r1, r2 = identity(1)
// stack: 1, nil
printf(
    "r1, r2 = %d, %s\n",
    (int)lua_tointeger(L, -2),
    lua_isnil(L, -1) ? "nil" : "not nil"
    );
lua_pop(L, 2);

lua_getglobal(L, "identity"); // identity
lua_pushinteger(L, 1); // identity, 1
lua_pushinteger(L, 2); // identity, 1, 2
status = lua_pcall(L, 2, 1, 0);
if (status) {
  fprintf(stderr, "%s", lua_tostring(L, -1));
  lua_pop(L, 1);
} else {
  printf("r1 = %d\n", (int)lua_tointeger(L, -1));
  lua_pop(L, 1);
}
```

其中 `lua_call` 调用的方法实际返回一个结果，但是声明了要两个返回结果，所以第二个是 nil。而 `lua_pcall` 通过 C 返回值来判断是否有错误。这两个方法都可以通过传 `LUA_MULTRET` 作为返回结果的数量，这样所有实际的返回值都会留在栈上，调用者需要自己对比栈上元素数量差来判断有多少个实际的返回值。

### Lua C 方法

通过 `lua_pushcfunction` 可以把 C 方法压入栈中，在使用上和 Lua 实现的方法完全一样。

一个 Lua 的 C 方法定义如下：

    typedef int (*lua_CFunction) (lua_State *L);

API `lua_pushcfunction` 的使用本身比较简单，关键是如果实现 C 方法。在进入 C 方法后，栈的状态是有 n 个元素在栈顶，位置从 1 到 n 分别对应第 1 到第 n 个参数。这时通过 `lua_gettop` 可以获得参数的数量。

然后可以在 C 方法里做任何事情，在方法返回前遵循约定操作栈：

- 把返回的 Lua value 依次压入栈，第一个返回结果最先入栈。
- 将结果个数作为 C 方法的返回值返回，0 个返回结果就返回 0

![[lua_cfunction.png|Lua C 方法]]

下面是一个用 C 实现的 `string_split` 方法示例，其中 `string_split` 的具体实现可以点击文件名查看完整文件。

※ [cfunction.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/master/cfunction.c)

``` c
/***
 * Split 字符串.
 *
 * @param str 字符串
 * @param sep 分隔符，只会使用第一个字符
 * @param[opt] count 最多进行 count - 1 次分隔，默认不限制。小于 1 的值都当成 1
 * @return ... 以多值的方式返回各部分
 */
static int l_string_split(lua_State* L) {
  size_t len = 0;
  const char* str = NULL;
  const char* sep = NULL;
  lua_Integer count = LUA_MAXINTEGER;

  int argc = lua_gettop(L);
  if (argc == 0) {
    return 0;
  }
  if (argc > 1) {
    sep = lua_tostring(L, 2);
  }
  if (argc > 2) {
    count = lua_tointeger(L, 3);
  }

  if (sep != NULL && count > 1) {
    str = lua_tolstring(L, 1, &len);
    if (str != NULL) {
      return string_split(L, str, len, *sep, count);
    }
  }

  // just returns str
  lua_pushvalue(L, 1);
  return 1;
}
```

### Lua C 闭包方法

API `lua_pushcclosure` 同样将一个 C Function 压入栈，不过可以关联一些在多次调用间共享的变量，也就是 Lua 中的闭包。而这些被绑定的变量在 Lua 中被称作 upvalue。

在 C 方法中想要绑定 upvalue 必须把它们全压入栈，API `lua_pushcclosure` 中指定 upvalue 的数量和要绑定 C 方法，并把完成绑定的方法压入栈。

在 C 方法中要访问这些绑定的 upvalue 要借助 `pseudo-index`。在 Lua 会分配一些数字为 `pseudo-index`。使用这些数字作为参数，不是根据位置是查找栈上元素，而是访问约定的特殊位置的元素。比如 `LUA_REGISTRYINDEX` 就是一个 `pseudo-index`，它指向一个全局的 table。像 Lua 里的全局变量实际都是存放在 `LUA_REGISTRYINDEX` 里的一个子 table 中的。

使用 `lua_upvalueindex` 会返回 upvalue 的 `pseudo-index`。从 1 开始按照入栈顺序编号。通过 `lua_to*` 和 `lua_replace` 就可以读取和修改这些在多次调用间共享的变量了。

![[lua_cclosure.png|Lua C 闭包方法]]

下面是一个用 C 闭包实现的随机数发生器的例子。

※ [cclosure.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/master/cclosure.c)

``` c
// 算法提取自 POSIX.1-2001 rand()实现
static int l_random_next(lua_State* L) {
  uint32_t seed = (uint32_t)lua_tointeger(L, lua_upvalueindex(1));
  int32_t next_number;
  seed = seed * (uint32_t)1103515245 + (uint32_t)12345;
  next_number = (int32_t)((uint32_t)seed / (int32_t)65536) % (int32_t)32768;

  // update upvalue
  lua_pushinteger(L, seed);
  lua_replace(L, lua_upvalueindex(1));

  lua_pushinteger(L, next_number);
  return 1;
}

/***
 * 给 Lua 返回一个用来生成随机序列的函数.
 *
 * @function random_generator
 * @tparam integer seed 随机种子
 * @treturn function generator 每次调用返回一个 `[0, 32768)` 区间内的随机数
 */
static int l_random_generator(lua_State* L) {
  lua_Integer seed = (lua_Integer)lua_tointeger(L, 1);

  lua_pushinteger(L, seed);
  lua_pushcclosure(L, l_random_next, 1);

  return 1;
}
```

## C 模块

上面都是以嵌入 Lua 直接操作栈来进行交互，Lua 中也可以把 C 编译成动态链接库使用 `require` 来加载。

    require "cjson"

上面这行 Lua 代码会去 `LUA_CPATH` 指定的目录下去查找名字是 cjson (cjson.so 或者 cjson.dll 等等) 的动态链接库。如果找到了，会动态加载并将其中的 `luaopen_cjson` 作为 Lua C Function 调用。调用返回的结果就是上面这行 `require` 的返回结果。当然已经加载过的模块是不会重复调用的。

有时候需要把大模块分拆，如果都分开编译成不同的动态链接库维护起来会很麻烦。所以不同于普通的 Lua 模块查找逻辑，当碰到含点的模块名时会对 C 模块做特殊处理。

``` lua
require "cjson.safe"
```

上面的代码如果没有找到 `cjson/safe.so` 的话，会再去查找 `cjson.so`，这样 `cjson`, `cjson.safe`, `cjson.another.module` 都可以共享一个动态链接库。对应的入口函数就是把点全部替换成下划线，然后在前面加上 `luaopen_`，比如 `luaopen_cjson_safe`。

下面把之前的 `string_split` 变成模块作为示例。这里只贴出了入口方法，完整文件点击文件名查看。其中的 `l_string_split` 就是上面定义的 C Function。注意入口方法必须 export 才能被动态加载，DLL 应该用 `__declspec(dllexport)`，so 应该用 `extern`。下面的例子定义了一个宏 `STRING_SPLIT_EXPORT`

※ [string_split.c](https://coding.net/u/doitian/p/lua-c-api-intro/git/blob/master/csrc/string_split.c)

``` c
#ifdef _MSC_VER
#define STRING_SPLIT_EXPORT    __declspec(dllexport)
#else
#define STRING_SPLIT_EXPORT    extern
#endif
STRING_SPLIT_EXPORT int luaopen_string_split(lua_State *L) {
  lua_createtable(L, 0, 1);

  lua_pushcfunction(L, l_string_split);
  lua_setfield(L, -2, "string_split");

  /** 方法很多的时候可以用 luaL_newlib 来注册
  luaL_Reg l[] = {
    { "string_split", l_string_split },
    { NULL, NULL }
  };
  luaL_newlib(L, l);
  */

  return 1;
}
```

测试的话，在编译出来的动态链接库所在目录执行正确版本的 Lua：

``` lua
local string_split = require "string_split".string_split
local parts = {string_split("Hello, Lua C API", " ", 2)}
print(#parts) --> 2
for i = 1, #parts do
  print(parts[i])
end
--> Hello,
--> Lua C API
```

## 通过 preload 注册 C 模块

像在 cocos2d-x 中，单独编译动态链接库并不是个很方便的选择，因为必须为所有可能用到的平台都生成对应的动态库，这种情况下可以把 C 代码和项目一起编译，使用 Lua C API 来注册。

一般会用到两种方法。

一种是 cocos2d-x Lua 中采用的直接把模块应该返回的 table 注册成全局变量，使用时不需要 `require` 直接用全局变量就可以了，所以有一堆的全局变量，`cc`, `display` 等等。

滥用全局变量会有很多问题，luacheck 静态检查工具需要手动加入例外像，造成 `_G` 表查找变慢等等。其实 Lua 提供了很好的解决方案，一个是 `package.loaded`，一个是 `package.preload`。

表 `package.loaded` 是所有通过 `require` 加载过的模块的返回值。重复 `require` 会直接返回 `package.loaded` 中以模块名为 key 的值。如果使用 C API 直接把模块的返回值以模块名为 key 添加到这个表中，那么 `require` 就会返回预先填入的值。不过这种方法有个问题就是一般在开发环境中会实现代码重新加载的功能，这个功能一般就是清空 `package.loaded`，这样之后的 `require` 就会重新从文件中读取。如果有模块是直接在这里添加的，需要在清空后再次添加。

而 `package.preload` 是更加推荐的做法。这个表也是使用模块名为 key，不过对应的值必须是 function。当 `package.loaded` 查找失败后，`require` 会优先查找 `package.preload` 这个表，如果找到了对应的 key，则会调用其对应的方法，而方法的返回值就作为 `require` 的返回值，并同时插入到 `package.loaded` 中。

下面的例子就是通过 `preload` 来注册 `string_split` 模块，这样 `string_split` 就可以和主程序一起编译了。

``` c
lua_getglobal(L, "package");
lua_getfield(L, -1, "preload");

lua_pushcfunction(L, luaopen_string_split);
lua_setfield(L, -2, "string_split");

lua_pop(L, 2);
```
