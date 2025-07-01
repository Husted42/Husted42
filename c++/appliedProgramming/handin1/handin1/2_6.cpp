#include "2_6.h"
#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>


// g++ -o output main.cpp ./handin1/2_6.cpp
// ./output
// math functions at page 28

double f(double x) {
    return exp(x) + pow(x, 3) - 5;
}

double f_prime(double x) {
    return exp(x) + 3 * pow(x, 2);
}

double newton_Raphson(double initialGuess, double epsilon){
    double x_prev = initialGuess;
    for (int i = 0; i < 100; ++i) {
        double x_next = x_prev - f(x_prev) / f_prime(x_prev);
        if (fabs(x_next - x_prev) < epsilon) {
            return x_next;
        }
        // When we change a variable, we shouldn't declare it again.
        x_prev = x_next;
    }
    
    return x_prev;
}
