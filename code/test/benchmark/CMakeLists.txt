# 一般而言，benchmark 比较少，所以就不再区分目录了

aux_source_directory(. DIR_SRCS)

add_library(stone-test-benchmark-obj OBJECT ${DIR_SRCS})

set(stone-test-benchmark
  $<TARGET_OBJECTS:stone-test-benchmark-obj>

  PARENT_SCOPE
)