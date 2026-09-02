#include <iostream>
#include <complex>
#include "handout/Vector.hpp"
#include "handout/Matrix.hpp"

template <typename T>
void testMatrix() {
    std::cout << "\n--- Testing Matrix<" << typeid(T).name() << "> ---\n";

    // Initialize 2x2 matrix
    Matrix<T> m1(2, 2);
    m1(0, 0) = static_cast<T>(1);
    m1(0, 1) = static_cast<T>(2);
    m1(1, 0) = static_cast<T>(3);
    m1(1, 1) = static_cast<T>(4);

    // Show dimensions
    std::cout << "Rows: " << m1.GetNumberOfRows() << ", Cols: " << m1.GetNumberOfColumns() << "\n";

    // Print matrix
    std::cout << "m1:\n";
    for (int i = 0; i < m1.GetNumberOfRows(); ++i) {
        for (int j = 0; j < m1.GetNumberOfColumns(); ++j) {
            std::cout << m1(i, j) << " ";
        }
        std::cout << "\n";
    }

    // Unary minus
    auto m_neg = -m1;
    std::cout << "-m1:\n";
    for (int i = 0; i < m_neg.GetNumberOfRows(); ++i) {
        for (int j = 0; j < m_neg.GetNumberOfColumns(); ++j) {
            std::cout << m_neg(i, j) << " ";
        }
        std::cout << "\n";
    }

    // Addition
    auto m_add = m1 + m1;
    std::cout << "m1 + m1:\n";
    for (int i = 0; i < m_add.GetNumberOfRows(); ++i) {
        for (int j = 0; j < m_add.GetNumberOfColumns(); ++j) {
            std::cout << m_add(i, j) << " ";
        }
        std::cout << "\n";
    }

    // Subtraction
    auto m_sub = m1 - m1;
    std::cout << "m1 - m1:\n";
    for (int i = 0; i < m_sub.GetNumberOfRows(); ++i) {
        for (int j = 0; j < m_sub.GetNumberOfColumns(); ++j) {
            std::cout << m_sub(i, j) << " ";
        }
        std::cout << "\n";
    }

    // Scalar multiplication
    auto m_scaled = m1 * 2;
    std::cout << "m1 * 2:\n";
    for (int i = 0; i < m_scaled.GetNumberOfRows(); ++i) {
        for (int j = 0; j < m_scaled.GetNumberOfColumns(); ++j) {
            std::cout << m_scaled(i, j) << " ";
        }
        std::cout << "\n";
    }

    // Matrix * Vector
    Vector<T> v1(2);
    v1[0] = static_cast<T>(1);
    v1[1] = static_cast<T>(1);
    auto mv = m1 * v1;
    std::cout << "m1 * v1:\n";
    for (int i = 0; i < mv.size(); ++i) {
        std::cout << mv[i] << " ";
    }
    std::cout << "\n";

    // Vector * Matrix
    auto vm = v1 * m1;
    std::cout << "v1 * m1:\n";
    for (int i = 0; i < vm.size(); ++i) {
        std::cout << vm[i] << " ";
    }
    std::cout << "\n";

    // Underlying storage
    const auto& storage = m1.getStorage();
    std::cout << "Underlying storage (row-major): ";
    for (const auto& val : storage) {
        std::cout << val << " ";
    }
    std::cout << "\n";
}

int main() {
    testMatrix<double>();
    testMatrix<int>();
    testMatrix<std::complex<double>>();

    return 0;
}
