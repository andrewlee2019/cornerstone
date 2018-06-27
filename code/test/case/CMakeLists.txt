
add_subdirectory(smp)
add_subdirectory(ssp)

set(stone-test-case
  # stone-test-case-smp
  ${stone-test-case-ssp}
  PARENT_SCOPE
)