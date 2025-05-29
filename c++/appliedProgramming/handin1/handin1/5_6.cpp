#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <cassert>

void Multiply(double **res, double **A, double **B, int ARows, int ACols, int BRows, int BCols){
    // Check if the number of columns in A is equal to the number of rows in B
    assert(ACols == BRows);
    
    // Initialize the result matrix with zeros
    for (int i = 0; i < ARows; ++i) {
        for (int j = 0; j < BCols; ++j) {
            res[i][j] = 0;
        }
    }

    // Perform matrix multiplication
    for (int i = 0; i < ARows; ++i) {
        for (int j = 0; j < BCols; ++j) {
            for (int k = 0; k < ACols; ++k) {
                res[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void Multiply(double *res, double *A, double **B, int ACols, int BRows, int BCols){
    // Check if the number of columns in A is equal to the number of rows in B
    assert(ACols == BRows);
    
    // Initialize the result vector with zeros
    for (int i = 0; i < BCols; ++i) {
        res[i] = 0;
    }

    // Perform matrix-vector multiplication
    for (int i = 0; i < BCols; ++i) {
        for (int j = 0; j < ACols; ++j) {
            res[i] += A[j] * B[j][i];
        }
    }
}
void Multiply(double *res, double **A, double *B, int ARows, int ACols, int BRows){
    // Check if the number of columns in A is equal to the number of rows in B
    assert(ACols == BRows);
    
    // Initialize the result vector with zeros
    for (int i = 0; i < ARows; ++i) {
        res[i] = 0;
    }

    // Perform matrix-vector multiplication
    for (int i = 0; i < ARows; ++i) {
        for (int j = 0; j < ACols; ++j) {
            res[i] += A[i][j] * B[j];
        }
    }
}
void Multiply(double **res, double scalar, double **B, int BRows, int BCols){
    // Initialize the result matrix with zeros
    for (int i = 0; i < BRows; ++i) {
        for (int j = 0; j < BCols; ++j) {
            res[i][j] = 0;
        }
    }

    // Perform scalar multiplication
    for (int i = 0; i < BRows; ++i) {
        for (int j = 0; j < BCols; ++j) {
            res[i][j] = scalar * B[i][j];
        }
    }
}
void Multiply(double **res, double **B, double scalar, int BRows, int BCols){
    // Initialize the result matrix with zeros
    for (int i = 0; i < BRows; ++i) {
        for (int j = 0; j < BCols; ++j) {
            res[i][j] = 0;
        }
    }

    // Perform scalar multiplication
    for (int i = 0; i < BRows; ++i) {
        for (int j = 0; j < BCols; ++j) {
            res[i][j] = B[i][j] * scalar;
        }
    }
}
