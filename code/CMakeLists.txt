
set(CMAKE_PATH ${CODE_PATH}/cmake)

project(cornerstone)

include(${CMAKE_PATH}/project/${PROJECT}.cmake)
include(${CMAKE_PATH}/include.cmake)
include(${CMAKE_PATH}/compile.cmake)

add_subdirectory(source)

set(BUILD_TEST ON)

if (BUILD_TEST)
  add_subdirectory(test)
endif()
