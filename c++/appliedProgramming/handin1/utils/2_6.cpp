#include "2_6.h"
#include <cmath>
#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>

// 
double newton_Raphson(double initialGuess, double epsilon) {
    double x_prev, x_next;
    x_prev = initialGuess;

    while (true) {
        double f = exp(x_prev) + pow(x_prev, 3) - 5;
        double f_prime = exp(x_prev) + 3 * pow(x_prev, 2);

        x_next = x_prev - f / f_prime;

        std::cout << x_next << "\n";

        if (fabs(x_next - x_prev) < epsilon) {
            break;
        }

        x_prev = x_next;
    }

    return x_next;
}