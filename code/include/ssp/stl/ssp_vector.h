// 包装 stl 的 vector
#pragma once

#include <vector>

#include "stone_define.h"

stone_namespace_begin

template<typename T>
using vector = std::vector<T>;

stone_namespace_end
