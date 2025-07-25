#include "arithmetic.h"
#include <iostream>
int my_add(int a, int b) {
    std::cout << "a + b" << std::endl;
    return a + b;
}

int my_sub(int a, int b) {
    std::cout << "a - b" << std::endl;
    return a - b;
}

int my_mul(int a, int b) {
    std::cout << "a * b" << std::endl;
    return a * b;
}

double my_div(int a, int b) {
    std::cout << "a / b" << std::endl;
    if (b == 0) return 0.0; // 简单处理除零
    return (double)a / b;
}
