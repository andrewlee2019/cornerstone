########################################################################
# CMake build script for cornerstone.
#

cmake_minimum_required (VERSION 3.0)

set(ROOT_PATH ${CMAKE_SOURCE_DIR})
set(CODE_PATH ${ROOT_PATH}/code)
set(THIRDPARTY_PATH ${ROOT_PATH}/thirdparty)
set(BUILD_PATH ${ROOT_PATH}/build/${PROJECT})

set(EXECUTABLE_OUTPUT_PATH ${BUILD_PATH}/exe)
set(LIBRARY_OUTPUT_PATH ${BUILD_PATH}/lib)

include_directories(${THIRDPARTY_PATH}/google/googletest/googletest/include)
add_subdirectory(code)
