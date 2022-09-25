---
comment: true
date: '2017-03-05T12:13:07+08:00'
description: "Vcpkg is a C/C++ libraries management tool in Windows provided by Microsoft. It is easy to be integrated with CMake, but static linking requires extra steps."
katex: false
share: true
title: Vcpkg static linking
---

# Vcpkg static linking

#cpp #windows

[Vcpkg][1] is a tool published by Microsoft, which is used to manage C/C++ libraries in Windows. It makes libraries installation easier, and it works well with CMake.

But it is not straitforward to staticly link the depdendent libraries using vcpkg.

<!--more-->

Under Linux，static linking just need to use `.a` files instead of `.so` files (similar in macOS). Use `boost` as an example, the bundled `FindBoost` returns found static library files in `Boost_LIBRARIES` when setting following flags.

``` cmake
set(Boost_USE_STATIC_LIBS ON)
set(Boost_USE_STATIC_RUNTIME ON)
```

Then just use `Boost_LIBRARIES` in `link_libraries` or `target_link_libraries` to statically link boost.

But when these two flags are set in Windows using vcpkg, CMake will complain that it cannot find static libraries of boost. It seems a constraint of VC compiler, so [vcpkg requires install the static version of libraries explicitly][2]. For example, to install boost static 64bit libraries:

    vcpkg install zlib:x64-windows-static

And `VCPKG_TARGET_TRIPLET` is required to generate VC project:

    cmake .. \
      -DCMAKE_TOOLCHAIN_FILE=/path/to/vcpkg.cmake \
      -DVCPKG_TARGET_TRIPLET=x64-windows-static \
      -G "Visual Studio 14 2015 Win64"

But the project generated throws error in linking. It can be fixed referring this Stack Overflow thread: [CMake compile with /MT instead of /MD][3]. Here is the final CMake sample:

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
