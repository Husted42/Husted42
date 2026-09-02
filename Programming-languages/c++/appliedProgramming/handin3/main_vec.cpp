#include <iostream>
#include <complex>
#include "handout/Vector.hpp"

template <typename T>
void testVector() {
    std::cout << "\n--- Testing Vector<" << typeid(T).name() << "> ---\n";

    // Initialize vector
    Vector<T> v1(3);
    v1[0] = static_cast<T>(1);
    v1[1] = static_cast<T>(2);
    v1[2] = static_cast<T>(3);

    // Test size
    std::cout << "Size: " << v1.size() << "\n";

    // Test element access
    std::cout << "v1: ";
    for (int i = 0; i < v1.size(); ++i) {
        std::cout << v1[i] << " ";
    }
    std::cout << "\n";

    // Test unary minus
    Vector<T> v_neg = -v1;
    std::cout << "-v1: ";
    for (int i = 0; i < v_neg.size(); ++i) {
        std::cout << v_neg[i] << " ";
    }
    std::cout << "\n";

    // Test addition
    Vector<T> v_add = v1 + v1;
    std::cout << "v1 + v1: ";
    for (int i = 0; i < v_add.size(); ++i) {
        std::cout << v_add[i] << " ";
    }
    std::cout << "\n";

    // Test subtraction
    Vector<T> v_sub = v1 - v1;
    std::cout << "v1 - v1: ";
    for (int i = 0; i < v_sub.size(); ++i) {
        std::cout << v_sub[i] << " ";
    }
    std::cout << "\n";

    // Test scalar multiplication
    Vector<T> v_scaled = v1 * 2;
    std::cout << "v1 * 2: ";
    for (int i = 0; i < v_scaled.size(); ++i) {
        std::cout << v_scaled[i] << " ";
    }
    std::cout << "\n";

    // Test norm (only meaningful for numeric types)
    if constexpr (std::is_arithmetic_v<T> || std::is_same_v<T, std::complex<double>>) {
        double norm = v1.CalculateNorm();
        std::cout << "||v1|| (p=2): " << norm << "\n";
    }

    // Test getStorage()
    const std::vector<T>& storage = v1.getStorage();
    std::cout << "Underlying storage: ";
    for (const auto& val : storage) {
        std::cout << val << " ";
    }
    std::cout << "\n";
}

int main() {
    testVector<double>();
    testVector<int>();
    testVector<std::complex<double>>();

    return 0;
}
