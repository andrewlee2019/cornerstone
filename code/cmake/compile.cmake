
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -lpthread")
set(${CMAKE_CXX_FLAGS} "${CMAKE_CXX_FLAGS} -Wl,--whole-archive")