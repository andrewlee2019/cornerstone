
set(TEST_PATH ${CODE_PATH}/test)
include(cmake/gtest.cmake)
include(cmake/benchmark.cmake)
include(cmake/include.cmake)

add_subdirectory(case)
add_subdirectory(stub)
add_subdirectory(benchmark)

add_executable(stone_test ${stone-test-case})
target_link_libraries(stone_test gtest_main gtest)

add_executable(stone_benchmark ${stone-test-benchmark})
target_link_libraries(stone_benchmark benchmark benchmark_main)
