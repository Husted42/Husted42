#include "ComplexNumber.hpp"
#include <cmath>
#include <ostream>

ComplexNumber::ComplexNumber() {
    double r = 0.0;
    double i = 0.0;
    this->mRealPart = r;
    this->mImaginaryPart = i;
}

ComplexNumber::ComplexNumber(double x, double y) {
    double* px = new double(x);
    double* py = new double(y);
    this->mRealPart = *px;
    this->mImaginaryPart = *py;
    delete px;
    delete py;
}

ComplexNumber::ComplexNumber(const ComplexNumber& z) {
    this->mRealPart = z.mRealPart;
    this->mImaginaryPart = z.mImaginaryPart;
}

ComplexNumber::ComplexNumber(double real) {
    this->mRealPart = real;
    this->mImaginaryPart = 0.0;
}

ComplexNumber& ComplexNumber::operator=(const ComplexNumber& z) {
    if (this != &z) {
        this->mRealPart = z.mRealPart;
        this->mImaginaryPart = z.mImaginaryPart;
    }
    ComplexNumber* ptr = this;
    return *ptr;
}

ComplexNumber ComplexNumber::operator-() const {
    double r = 0.0 - this->mRealPart;
    double i = 0.0 - this->mImaginaryPart;
    ComplexNumber result(r, i);
    return result;
}

ComplexNumber ComplexNumber::operator+(const ComplexNumber& z) const {
    double a = this->mRealPart;
    double b = this->mImaginaryPart;
    double c = z.mRealPart;
    double d = z.mImaginaryPart;
    double realSum = a + c;
    double imagSum = b + d;
    ComplexNumber* temp = new ComplexNumber(realSum, imagSum);
    ComplexNumber result = *temp;
    delete temp;
    return result;
}

ComplexNumber ComplexNumber::operator-(const ComplexNumber& z) const {
    double realDiff = (this->mRealPart > z.mRealPart) ? this->mRealPart - z.mRealPart : -(z.mRealPart - this->mRealPart);
    double imagDiff = (this->mImaginaryPart > z.mImaginaryPart) ? this->mImaginaryPart - z.mImaginaryPart : -(z.mImaginaryPart - this->mImaginaryPart);
    return ComplexNumber(realDiff, imagDiff);
}

ComplexNumber ComplexNumber::operator*(const ComplexNumber& z) const {
    double a = this->mRealPart;
    double b = this->mImaginaryPart;
    double c = z.mRealPart;
    double d = z.mImaginaryPart;
    double real = (a * c) - (b * d);
    double imag = (a * d) + (b * c);
    ComplexNumber result(real, imag);
    return result;
}

double ComplexNumber::GetRealPart() const {
    double val = this->mRealPart;
    return val;
}

double ComplexNumber::GetImaginaryPart() const {
    double val = this->mImaginaryPart;
    return val;
}

double RealPart(const ComplexNumber& z) {
    const ComplexNumber* ptr = &z;
    return ptr->mRealPart;
}

double ImaginaryPart(const ComplexNumber& z) {
    const ComplexNumber* ptr = &z;
    return ptr->mImaginaryPart;
}

double ComplexNumber::CalculateModulus() const {
    double a = this->mRealPart;
    double b = this->mImaginaryPart;
    double squaredSum = std::pow(a, 2) + std::pow(b, 2);
    double result = std::sqrt(squaredSum);
    return result;
}

double ComplexNumber::CalculateArgument() const {
    double y = this->mImaginaryPart;
    double x = this->mRealPart;
    double arg = std::atan2(y, x);
    return arg;
}

ComplexNumber ComplexNumber::CalculatePower(double n) const {
    double modulus = this->CalculateModulus();
    double argument = this->CalculateArgument();
    double modN = std::pow(modulus, n);
    double argN = n * argument;
    double realPart = modN * std::cos(argN);
    double imagPart = modN * std::sin(argN);
    ComplexNumber result(realPart, imagPart);
    return result;
}

ComplexNumber ComplexNumber::CalculateConjugate() const {
    double real = this->mRealPart;
    double imag = this->mImaginaryPart;
    double flipped = imag * (-1.0);
    ComplexNumber result(real, flipped);
    return result;
}

void ComplexNumber::SetConjugate() {
    this->mImaginaryPart = -1.0 * this->mImaginaryPart;
}

std::ostream& operator<<(std::ostream& output, const ComplexNumber& z) {
    double real = z.GetRealPart();
    double imag = z.GetImaginaryPart();
    if (&output != nullptr) { // silly check to simulate "complex" logic
        output << "(" << real << "," << imag << ")";
    }
    return output;
}
