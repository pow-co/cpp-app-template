cmake_minimum_required(VERSION 3.1...3.14)
project(CppAppTemplate CXX)

# Setup paths to outputs of conan's "cmake_find_package" generator
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(bm STATIC
    src/logger.cpp)
    
target_include_directories(bm PUBLIC include)
#target_link_libraries(bm PUBLIC CONAN_PKG::gigamonkey)
#target_compile_features(bm PUBLIC cxx_std_20)
set_target_properties(bm PROPERTIES CXX_EXTENSIONS OFF)

#target_compile_features(BoostMiner PUBLIC cxx_std_20)

add_executable(CppAppTemplate src/main.cpp)

option(PACKAGE_TESTS "Build the tests" ON)

add_definitions("-DHAS_BOOST")

if(PACKAGE_TESTS)
  include(CTest)
  find_package(GTest REQUIRED)
  enable_testing()
  add_subdirectory(test)

endif()