#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <cassert>

void solve3by3(double **A, double *b, double *u) {
    int n = 3;
    int pivot[3] = {0, 1, 2};

    // Partial pivoting
    for (int i = 0; i < n; ++i) {
        int maxRow = i;
        for (int k = i + 1; k < n; ++k) {
            if (fabs(A[k][i]) > fabs(A[maxRow][i])) {
                maxRow = k;
            }
        }

        // Swap rows in A
        if (maxRow != i) {
            double *tempRow = A[i];
            A[i] = A[maxRow];
            A[maxRow] = tempRow;

            // Swap entries in b
            double tempVal = b[i];
            b[i] = b[maxRow];
            b[maxRow] = tempVal;
        }

        // Forward elimination
        for (int j = i + 1; j < n; ++j) {
            double factor = A[j][i] / A[i][i];
            for (int k = i; k < n; ++k) {
                A[j][k] -= factor * A[i][k];
            }
            b[j] -= factor * b[i];
        }
    }

    // Back substitution
    for (int i = n - 1; i >= 0; --i) {
        u[i] = b[i];
        for (int j = i + 1; j < n; ++j) {
            u[i] -= A[i][j] * u[j];
        }
        u[i] /= A[i][i];
    }
}