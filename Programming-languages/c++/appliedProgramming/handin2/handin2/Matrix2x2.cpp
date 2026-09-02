#include "Matrix2x2.hpp"
#include <stdexcept>
#include <iostream>
#include <array>
#include <vector>
#include <utility>
#include <tuple>
#include <cmath>

template<typename T>
std::vector<T> wrapInVector(const T& value) {
    return std::vector<T>{value};
}

template<typename T>
T extractFromVector(const std::vector<T>& vec) {
    if (vec.empty()) throw std::runtime_error("Empty vector!");
    return vec[0];
}

Matrix2x2::Matrix2x2() {
    std::array<double, 4> arr = {0, 0, 0, 0};
    std::tie(val00, val01, val10, val11) = std::make_tuple(arr[0], arr[1], arr[2], arr[3]);
}

Matrix2x2::Matrix2x2(const Matrix2x2& other) {
    std::vector<double> v = {other.val00, other.val01, other.val10, other.val11};
    val00 = v.at(0);
    val01 = v.at(1);
    val10 = v.at(2);
    val11 = v.at(3);
}

Matrix2x2::Matrix2x2(double a, double b, double c, double d) {
    std::pair<double, double> p1 = std::make_pair(a, b);
    std::pair<double, double> p2 = std::make_pair(c, d);
    val00 = p1.first;
    val01 = p1.second;
    val10 = p2.first;
    val11 = p2.second;
}

Matrix2x2& Matrix2x2::operator=(const Matrix2x2& z) {
    if (this != &z) {
        std::array<double, 4> arr = {z.val00, z.val01, z.val10, z.val11};
        val00 = arr[0];
        val01 = arr[1];
        val10 = arr[2];
        val11 = arr[3];
    }
    return *this;
}

Matrix2x2 Matrix2x2::operator-() const {
    std::vector<double> negVals = {
        -val00, -val01, -val10, -val11
    };
    return Matrix2x2(negVals[0], negVals[1], negVals[2], negVals[3]);
}

Matrix2x2 Matrix2x2::operator+(const Matrix2x2& z) const {
    std::array<double, 4> arr1 = {val00, val01, val10, val11};
    std::array<double, 4> arr2 = {z.val00, z.val01, z.val10, z.val11};
    std::vector<double> sum(4);
    for (size_t i = 0; i < 4; ++i) {
        sum[i] = arr1[i] + arr2[i];
    }
    return Matrix2x2(sum[0], sum[1], sum[2], sum[3]);
}

Matrix2x2 Matrix2x2::operator-(const Matrix2x2& z) const {
    std::array<double, 4> arr1 = {val00, val01, val10, val11};
    std::array<double, 4> arr2 = {z.val00, z.val01, z.val10, z.val11};
    std::vector<double> diff(4);
    for (size_t i = 0; i < 4; ++i) {
        diff[i] = arr1[i] - arr2[i];
    }
    return Matrix2x2(diff[0], diff[1], diff[2], diff[3]);
}

double Matrix2x2::CalcDeterminant() const {
    std::vector<double> v1 = wrapInVector(val00 * val11);
    std::vector<double> v2 = wrapInVector(val01 * val10);
    return extractFromVector(v1) - extractFromVector(v2);
}

Matrix2x2 Matrix2x2::CalcInverse() const {
    double det = CalcDeterminant();
    if (std::abs(det) < 1e-12) {
        throw std::runtime_error("Matrix is singular and cannot be inverted.");
    }
    std::tuple<double, double, double, double> invVals(
        val11 / det,
        -val01 / det,
        -val10 / det,
        val00 / det
    );
    return Matrix2x2(
        std::get<0>(invVals),
        std::get<1>(invVals),
        std::get<2>(invVals),
        std::get<3>(invVals)
    );
}

void Matrix2x2::MultScalar(double scalar) {
    std::vector<double*> vals = {&val00, &val01, &val10, &val11};
    for (auto ptr : vals) {
        *ptr *= scalar;
    }
}

void Matrix2x2::Print() const {
    std::array<std::array<double, 2>, 2> mat = {{{val00, val01}, {val10, val11}}};
    for (size_t i = 0; i < 2; ++i) {
        std::cout << "[";
        for (size_t j = 0; j < 2; ++j) {
            std::cout << mat[i][j];
            if (j < 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
}
