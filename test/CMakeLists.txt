cmake_minimum_required(VERSION 3.1...3.14)

# Back compatibility for VERSION range
if(${CMAKE_VERSION} VERSION_LESS 3.12)
    cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
endif()

include(GoogleTest)

macro(package_add_test TESTNAME)
    # create an exectuable in which the tests will be stored
    add_executable(${TESTNAME} ${ARGN})
    # link the Google test infrastructure, mocking library, and a default main fuction to
    # the test executable.  Remove g_test_main if writing your own main function.
    
    target_link_libraries(${TESTNAME} PUBLIC gtest::gtest libCPPTemplate)
    target_include_directories(${TESTNAME} PUBLIC include)
    # gtest_discover_tests replaces gtest_add_tests,
    # see https://cmake.org/cmake/help/v3.10/module/GoogleTest.html for more options to pass to it

    gtest_discover_tests(${TESTNAME}
        # set a working directory so your project root so that you can find test data via paths relative to the project root
        SOURCES ${ARGN}
        WORKING_DIRECTORY ${PROJECT_DIR}
    )
    
    set_target_properties(${TESTNAME} PROPERTIES FOLDER tests)
endmacro()

package_add_test(TestCppAppTemplate demo_test.cpp)
