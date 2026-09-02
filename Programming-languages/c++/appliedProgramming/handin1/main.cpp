#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>
#include <cassert>
#include <iomanip>

#include "./handin1/2_6.h"
#include "./handin1/3_3.h"
#include "./handin1/5_3.h"
#include "./handin1/5_4.h"
#include "./handin1/5_6.h"
#include "./handin1/5_9.h"
#include "./handin1/5_10.h"


int test_5_10() {
    const int n = 3;

    // Allocate memory for A (3x3 matrix)
    double **A = new double*[n];
    for (int i = 0; i < n; ++i) {
        A[i] = new double[n];
    }

    // Example system:
    // 2x + y - z = 8
    // -3x - y + 2z = -11
    // -2x + y + 2z = -3

    A[0][0] = 2;  A[0][1] = 1;  A[0][2] = -1;
    A[1][0] = -3; A[1][1] = -1; A[1][2] = 2;
    A[2][0] = -2; A[2][1] = 1;  A[2][2] = 2;

    double b[n] = {8, -11, -3};
    double u[n]; // Solution vector

    guassian_elimination(A, b, u, n);

    // Output solution
    std::cout << "Solution vector u:\n";
    for (int i = 0; i < n; ++i) {
        std::cout << "u[" << i << "] = " << std::setprecision(6) << u[i] << "\n";
    }

    // Clean up memory
    for (int i = 0; i < n; ++i) {
        delete[] A[i];
    }
    delete[] A;

    return 0;
}

int main(int argc, char* argv[])
{
    // 2.6 double newton_Raphson(double initialGuess, double epsilon);
    double newton = newton_Raphson(0,  0.0001);
    std::cout << newton <<"\n";

    newton = newton_Raphson(0,  0.001);
    std::cout << newton <<"\n";

    newton = newton_Raphson(0,  0.01);
    std::cout << newton <<"\n";

    // 3.3
    std::cout << "euler\n";
    int n = 100000;
    implicit_Euler(n);

    // 5.3
    double x = 1;
    double y = 2;
    std::cout << "Before swap_pointe0r: x = " << x << ", y = " << y << std::endl;
    swap_pointer(&x, &y);
    std::cout << "After swap_pointer:  x = " << x << ", y = " << y << std::endl;

    x = 1;
    y = 2;
    std::cout << "\nBefore swap_ref: x = " << x << ", y = " << y << std::endl;
    swap_ref(x, y);
    std::cout << "After swap_ref:  x = " << x << ", y = " << y << std::endl;
    
    // 5.4
    double a[] = {1, 2, 3, 4, 5};
    // double b[] = {1, 2, 1, 2, 1};
    
    std::cout << "Standard deviation of a: " << calc_std(a, 5) << std::endl;
    // std::cout << "Standard deviation of b: " << calc_std(b, 5) << std::endl;

    test_5_10();

    return 0;
}