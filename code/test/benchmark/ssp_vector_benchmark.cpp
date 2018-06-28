#include "benchmark.h"
#include "ssp_vector.h"

static void bm_vector_push_back(benchmark::State& state)
{
  stone::vector<uint32_t> a;
  for (auto _ : state)
    a.push_back(1u);
}

BENCHMARK(bm_vector_push_back);
