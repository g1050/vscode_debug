#include "arithmetic.h"
#include<iostream>
int main()
{
    int a = 6;
    int b = 2;
    int c = my_add(a,b);
    c = my_sub(a,b);
    c = my_mul(a,b);
    c = my_div(a,b);
    std::cout << "c = " << c << std::endl;
    return 0;
}