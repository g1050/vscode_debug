pushd demo
mkdir build
cd build
cmake ..
cmake --build .
cmake --install .
popd

pushd test
mkdir mkdir build
cd build
cmake ..
cmake --build .
./test_demo
popd