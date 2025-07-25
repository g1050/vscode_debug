cmake_minimum_required(VERSION 3.10)
project(arithmetic_demo)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_BUILD_TYPE Debug)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

add_library(arithmetic SHARED src/arithmetic.cpp)

target_include_directories(arithmetic PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

install(TARGETS arithmetic
    LIBRARY DESTINATION ${CMAKE_SOURCE_DIR}/release/lib
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
    DESTINATION ${CMAKE_SOURCE_DIR}/release/include
) 