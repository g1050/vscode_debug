#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    int x = 1;
    int y = 2;
    int result = add(x, y);
    std::cout << x << " + " << y << " = " << result << std::endl;
    return 0;
}
