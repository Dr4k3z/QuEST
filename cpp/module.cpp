#include <nanobind/nanobind.h>
#include <nanobind/eigen/dense.h>
#include <Eigen/Core>

namespace nb = nanobind;
using namespace nb::literals;

int add(const int a, const int b) { return a + b; }

double vector_dot(const Eigen::Ref<const Eigen::VectorXd>& x,
                  const Eigen::Ref<const Eigen::VectorXd>& y) {
    if (x.size() != y.size()) {
        throw nb::value_error("vector_dot expects vectors with the same length");
    }
    return x.dot(y);
}

NB_MODULE(_quest_core, m) {
    m.doc() = "QuEST nanobind extension module";
    m.def("add", &add, "a"_a, "b"_a, "Add two integers");
    m.def("vector_dot", &vector_dot, "x"_a, "y"_a, "Compute the dot product of two vectors");
}
