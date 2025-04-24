#include "2_6.h"
#include <cmath>
#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <cassert>
#include <fstream>


// n = Number of grid points
// h = Step size
void implicit_Euler(int n) {
    assert(n > 1 && "We need at least 1 grid point");
    double h = 1.0 / n;
    double x = 0.0;
    double y = 1.0;

    std::ofstream write_file("xy.dat");
    // Write numbers as +x.<13digits>e+00 (width 20)
    write_file.setf(std::ios::scientific);
    write_file.setf(std::ios::showpos);
    write_file.precision(13);

    for (int i = 0; i < n; ++i) {
        x += h;
        y = y / (1 + h * y);
        std::cout << "x: " << x << ", y: " << y << "\n";
        write_file << x << " " << y << "\n";
    }

    write_file.close();
}
