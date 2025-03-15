cmake_minimum_required(VERSION 3.12)

include(pybind11.cmake)

pybind11_add_module(cpp_bindings bindings.cpp)  # first argument will be Python module name (used to do `import X` in python), needs to be the same as in bindings.cpp