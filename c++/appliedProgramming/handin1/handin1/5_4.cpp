#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>


double calc_mean(double a[], int length){
    double sum = 0.0;
    for (int i = 0; i < length; ++i) {
        sum += a[i];
    }
    return sum / length;
}

double calc_std(double a[], int length){
    double mean = calc_mean(a, length);
    double sum = 0.0;
    if (length <= 1) {
        return 0.0; // Standard deviation is not defined for a single value
    }
    for (int i = 0; i < length; i++) {
        sum += pow((a[i] - mean), 2);
    }
    return sqrt(sum / (length - 1));
}