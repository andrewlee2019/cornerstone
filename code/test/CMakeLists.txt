
set(TEST_PATH ${CODE_PATH}/test)
include(${TEST_PATH}/cmake/include.cmake)

add_subdirectory(case)
add_subdirectory(stub)

add_executable(stone_test ${stone-test-case})
target_link_libraries(stone_test gtest gtest_main)
