#include <iostream>
#include <sstream>
#include <ctime>
#include <random>
#include <cmath>
#include <stdio.h>
#include <cassert>

#include <cassert>
#include <cmath>
#include <algorithm> // For std::swap

void guassian_elimination(double **A, double *b, double *u, int n) {
    assert(A != nullptr && b != nullptr && u != nullptr);
    assert(n > 0);

    // Forward elimination with partial pivoting
    for (int i = 0; i < n - 1; ++i) {
        // Find the row with the largest pivot in column i
        int max_row = i;
        for (int k = i + 1; k < n; ++k) {
            if (std::fabs(A[k][i]) > std::fabs(A[max_row][i])) {
                max_row = k;
            }
        }

        // Swap rows in A and b
        if (max_row != i) {
            std::swap(A[i], A[max_row]);
            std::swap(b[i], b[max_row]);
        }

        // Eliminate entries below pivot
        for (int j = i + 1; j < n; ++j) {
            if (A[i][i] == 0) continue; // Prevent division by zero
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
