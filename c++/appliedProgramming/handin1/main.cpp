#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>

#include "./utils/2_6.h"
#include "./utils/3_3.h"
#include "./utils/5_3.h"
#include "./utils/5_4.h"
#include "./utils/5_6.h"
#include "./utils/5_9.h"
#include "./utils/5_10.h"


int main(int argc, char* argv[])
{
    // 2.6 double newton_Raphson(double initialGuess, double epsilon);
    // clang++ -o main main.cpp utils/2_6.cpp
    double newton = newton_Raphson(0,  0.0001);
    std::cout << newton <<"\n";

    implicit_Euler(10);

    return 0;
}