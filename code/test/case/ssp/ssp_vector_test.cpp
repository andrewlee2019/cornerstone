#include "gtest.h"
#include "ssp_vector.h"
using namespace testing;

TEST(vector, case1)
{
  stone::vector<uint32_t> a;
  a.push_back(1u);
  EXPECT_FALSE(a.empty());
}
