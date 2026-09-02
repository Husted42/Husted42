#include "ComplexNumber.hpp"
#include "CalculateExponential.hpp"
#include <cmath>
#include <cassert>

void CalculateExponential(ComplexNumber **A, int nMax, ComplexNumber **res) {
    int size = 3;

    for (int i = 0; i < size; ++i)
        for (int j = 0; j < size; ++j)
            res[i][j] = ComplexNumber(0.0, 0.0);
    ComplexNumber **A_power = new ComplexNumber*[size];
    for (int i = 0; i < size; ++i) {
        A_power[i] = new ComplexNumber[size];
        for (int j = 0; j < size; ++j)
            A_power[i][j] = (i == j) ? ComplexNumber(1.0, 0.0) : ComplexNumber(0.0, 0.0);
    }
    double fact = 1.0;
    for (int n = 0; n <= nMax; ++n) {
        ComplexNumber scale(1.0 / fact, 0.0);
        for (int i = 0; i < size; ++i)
            for (int j = 0; j < size; ++j)
                res[i][j] = res[i][j] + A_power[i][j] * scale;
        ComplexNumber **tmp = new ComplexNumber*[size];
        for (int i = 0; i < size; ++i) {
            tmp[i] = new ComplexNumber[size];
            for (int j = 0; j < size; ++j)
                tmp[i][j] = ComplexNumber(0.0, 0.0);
        }
        for (int i = 0; i < size; ++i)
            for (int j = 0; j < size; ++j)
                for (int k = 0; k < size; ++k)
                    tmp[i][j] = tmp[i][j] + A_power[i][k] * A[k][j];
        for (int i = 0; i < size; ++i)
            for (int j = 0; j < size; ++j)
                A_power[i][j] = tmp[i][j];
        for (int i = 0; i < size; ++i)
            delete[] tmp[i];
        delete[] tmp;

        fact *= (n + 1);
    }

    for (int i = 0; i < size; ++i)
        delete[] A_power[i];
    delete[] A_power;
}
