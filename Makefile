# Variables
MODULE = Stringler
BUILD_DIR = build
BINDINGS = bindings/bindings.cpp
CXX = c++
CXXFLAGS = -O3 -Wall -shared -std=c++20 -fPIC ${shell python3 -m pybind11 --includes}
EXT_SUFFIX = $(shell python3-config --extension-suffix)

# Build
build:
	mkdir -p build input
	$(CXX) $(CXXFLAGS) ${BINDINGS} -o $(BUILD_DIR)/$(MODULE)$(EXT_SUFFIX)

# Test
test:
	PYTHONPATH=$(BUILD_DIR) pytest tests

# Compile
all: build test

# Cleaning
clean:
	rm -rf ${BUILD_DIR} input output *.egg-info __pycache__ */__pycache__ .pytest_cache

.PHONY: build test all clean
