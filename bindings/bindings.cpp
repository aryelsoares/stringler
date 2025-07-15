#include "../src/stringler.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(Stringler, s) {
    s.doc() = "NLP: Stringler";
    
    py::class_<Stringler>(s, "Stringler")
        .def(py::init<std::string&>())
        .def("getArr", &Stringler::getArr, "Word array")
        .def("getSize", &Stringler::getSize, "Word size")
        .def("largest", &Stringler::largest, "Largest string")
        .def("mean", &Stringler::mean, "Average of words")
        .def("std", &Stringler::std, "Standard deviation of words")
        .def("skew", &Stringler::skew, "Asymmetry coefficient")
        .def("kurtosis", &Stringler::kurtosis, "Kurtosis coefficient")
        .def("jarqueBera", &Stringler::jarqueBera, "JB Coefficient")
        .def("typeTokenRatio", &Stringler::typeTokenRatio, "Lexical diversity")
        .def("polygrams", &Stringler::polygrams, py::arg("words") = 1, "Word count")
        .def("fashion", &Stringler::fashion, "Most common string")
        .def("emotion", &Stringler::emotion, "Emotion counting")
        .def("reaction", &Stringler::reaction, "Reaction counting");
}