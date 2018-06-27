aux_source_directory(. DIR_SRCS)

add_library(stone-test-case-ssp-obj OBJECT ${DIR_SRCS})

set(stone-test-case-ssp
  $<TARGET_OBJECTS:stone-test-case-ssp-obj>

  PARENT_SCOPE
)
