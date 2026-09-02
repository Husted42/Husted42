#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>


// Write a function that swaps the values of two double precision floating point
// numbers, so that these changes are visible in the code that has called this function
void swap_pointer(double *a, double *b){
    double temp = *a;
    *a = *b;
    *b = temp;
}

void swap_ref(double &a, double &b){
    double temp = a;
    a = b;
    b = temp;
}
