
# 支持 glog
include_directories(${THIRDPARTY_PATH}/apache/libevent)
option(EVENT__DISABLE_OPENSSL
    "Define if libevent should build without support for OpenSSL encrpytion" ON)
add_subdirectory("${THIRDPARTY_PATH}/apache/libevent" "${BUILD_PATH}/libevent")