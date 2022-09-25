---
comment: true
date: '2017-03-05T12:13:07+08:00'
description: Vcpkg 是微软推出的在 Windows 上管理 C/C++ 库的工具，和 CMake 能很好的集成。不过想要静态链接依赖库需要特殊处理。
katex: false
share: true
title: 使用 vcpkg 链接静态库
---

# Vcpkg Static Linking

#cpp #windows

[Vcpkg][1] 是微软推出的用于在 Windows 上管理 C/C++ 库的工具。通过它能够方便的安装常用的 C/C++ 库，而且提供了 CMake 的集成。这使得使用 CMake 的项目在 Windows 下构建方便了很多，不需要自己手动去指定在 Windows 下如何找到依赖的库了。

不过实际使用中还是碰到一些问题。为了减少依赖，直接复制一个可执行程序就能在其它机器上运行，经常会需要静态链接依赖的库。而在 Windows 上使用 vcpkg 静态链接需要一些特殊的操作。

<!--more-->

在 Linux 下，只需要在链接中使用 `.a` 的静态库就行了。以 `boost` 为例，CMake 自带的 `FindBoost` 就可以指定搜索静态库

``` cmake
set(Boost_USE_STATIC_LIBS ON)
set(Boost_USE_STATIC_RUNTIME ON)
```

这样 `Boost_LIBRARIES` 中包含的就是静态库了，按平常方式使用 `link_libraries` 或者 `target_link_libraries` 就可以了。

但是设置了上面的参数后，在 Windows 下使用 vcpkg 会提示找不到静态库。看来是 Windows 下没有办法同时提供静态和动态库，所以 [vcpkg 需要额外安装静态库的版本][2]，以 boost 的 64 位的静态库为例，安装命令如下：

    vcpkg install zlib:x64-windows-static

而在使用 CMake 生成 Visual Studio 项目的时候也需要指定 `VCPKG_TARGET_TRIPLET`

    cmake .. \
      -DCMAKE_TOOLCHAIN_FILE=/path/to/vcpkg.cmake \
      -DVCPKG_TARGET_TRIPLET=x64-windows-static \
      -G "Visual Studio 14 2015 Win64"

不过这样生成的项目在链接阶段会报错的，因为 VC 的编译器在生成 obj 文件的时候就需要指定链接时是使用动态链接还是静态链接，默认 CMake 生成的项目都是使用动态链接，导致链接时 obj 文件和库的格式不符，这个可以参考 Stack Overflow 上这个问题 [CMake compile with /MT instead of /MD][3] 的回答来修改，最终的 CMake 如下

``` cmake
cmake_minimum_required(VERSION 3.0)

project(static_link_test CXX)

set(CMAKE_CXX_STANDARD 11)

if(MSVC)
  string(REPLACE "/MD" "/MT" CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS})
  string(REPLACE "/MD" "/MT" CMAKE_CXX_FLAGS_DEBUG ${CMAKE_CXX_FLAGS_DEBUG})
  string(REPLACE "/MD" "/MT" CMAKE_CXX_FLAGS_RELEASE ${CMAKE_CXX_FLAGS_RELEASE})
else(MSVC)
  set(Boost_USE_STATIC_LIBS ON)
  set(Boost_USE_STATIC_RUNTIME ON)
endif(MSVC)

find_package(Boost 1.36.0 REQUIRED COMPONENTS filesystem program_options)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}/src
  ${Boost_INCLUDE_DIRS}
)

link_libraries(
  ${Boost_LIBRARIES}
)

add_executable(static_link_test
  src/main.cpp
)

install(TARGETS static_link_test RUNTIME DESTINATION bin)
```

[1]:    https://github.com/Microsoft/vcpkg
[2]:    https://blogs.msdn.microsoft.com/vcblog/2016/11/01/vcpkg-updates-static-linking-is-now-available/
[3]:    http://stackoverflow.com/questions/14172856/cmake-compile-with-mt-instead-of-md
