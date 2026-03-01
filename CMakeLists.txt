cmake_minimum_required(VERSION 3.20)
project(quest LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN ON)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
add_subdirectory(extern/nanobind)

nanobind_add_module(_quest_core cpp/module.cpp)
install(
    TARGETS _quest_core
    LIBRARY DESTINATION quest
    RUNTIME DESTINATION quest
    ARCHIVE DESTINATION quest
)
