
set(CMAKE_PATH ${CODE_PATH}/cmake)

project(cornerstone)

include(${CMAKE_PATH}/project/${PROJECT}.cmake)
include(${CMAKE_PATH}/include.cmake)
include(${CMAKE_PATH}/compile.cmake)
include(${CMAKE_PATH}/thirdparty/libevent.cmake)
include(${CMAKE_PATH}/thirdparty/glog.cmake)

add_subdirectory(source)

set(BUILD_TEST ON)

if (BUILD_TEST)
  add_subdirectory(test)
endif()
