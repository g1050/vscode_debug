cmake_minimum_required(VERSION 3.10)
project(test_demo)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_BUILD_TYPE Debug)

include_directories(${CMAKE_SOURCE_DIR}/../demo/release/include)
link_directories(${CMAKE_SOURCE_DIR}/../demo/release/lib)

add_executable(test_demo test_demo.cpp)
target_link_libraries(test_demo arithmetic) 