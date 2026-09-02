#include "3_3.h"
#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>
#include <cassert>
#include <fstream>

void implicit_Euler(int n){
    assert(n > 1);
    double y0 = 1; 
    n = n - 1; 
    double h = 1.0 / n; 

    double* x = new double[n + 1];
    double* y = new double[n + 1];

    x[0] = 0;
    y[0] = y0;

    for (int i = 1; i <= n; ++i) {
        x[i] = i * h;
        y[i] = y[i - 1] / (1 + h);
    }

    std::ofstream write_output("xy.dat");
    assert(write_output.is_open());
    for (int i = 0; i <= n; i++) {
        write_output << x[i] << "," << y[i] << "\n";
    }
    write_output.close();

    // Free allocated memory
    delete[] x;
    delete[] y;
}