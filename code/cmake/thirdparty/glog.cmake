
# 支持 glog
include_directories(${THIRDPARTY_PATH}/google/glog/src/glog)
add_subdirectory("${THIRDPARTY_PATH}/google/glog" "${BUILD_PATH}/glog")
