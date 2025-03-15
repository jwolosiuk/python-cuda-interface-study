#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../cpp/src/main.cpp"


namespace py = pybind11;    
    
PYBIND11_MODULE(cpp_bindings, m) {  // first argument will be Python module name (used to do `import X` in python), needs to be the same as in CMakeLists.txt
    m.def("get_result", &get_result, "get_result");
}