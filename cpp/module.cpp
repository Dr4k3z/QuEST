#include <nanobind/nanobind.h>
#include <iostream>

namespace nb = nanobind;
using namespace nb::literals;

int add(const int a, const int b) {
    std::cout << "This is from C++\n";
    return a + b;
}

NB_MODULE(_quest_core, m) {
    m.doc() = "QuEST nanobind extension module";
    m.def("add", &add, "a"_a, "b"_a, "Add two integers");
}
