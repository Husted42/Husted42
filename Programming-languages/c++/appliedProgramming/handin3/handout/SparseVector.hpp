#ifndef SPARSE_VECTOR_HPP
#define SPARSE_VECTOR_HPP

#include "Vector.hpp"
#include "Matrix.hpp"
#include <vector>
#include <algorithm>
#include <cassert>

template <class T>
class SparseVector {
private:
    unsigned int mDim;  // total dimensionality
    std::vector<unsigned int> mIndices; // indices of nonzero elements (sorted)
    std::vector<T> mValues;             // corresponding nonzero values

public:
    SparseVector() : mDim(0) {}

    SparseVector(unsigned int dim) : mDim(dim) {}

    void setValue(unsigned int index, T value) {
        assert(index < mDim);
        auto it = std::lower_bound(mIndices.begin(), mIndices.end(), index);
        if (it != mIndices.end() && *it == index) {
            // overwrite existing value
            mValues[it - mIndices.begin()] = value;
        } else {
            // insert new index & value
            auto pos = it - mIndices.begin();
            mIndices.insert(it, index);
            mValues.insert(mValues.begin() + pos, value);
        }
    }

    T getValue(unsigned int index) const {
        assert(index < mDim);
        auto it = std::lower_bound(mIndices.begin(), mIndices.end(), index);
        if (it != mIndices.end() && *it == index) {
            return mValues[it - mIndices.begin()];
        }
        return T();  // return zero
    }

    unsigned int size() const {
        return mDim;
    }

    unsigned int nonZeroes() const {
        return static_cast<unsigned int>(mIndices.size());
    }

    unsigned int indexNonZero(unsigned int i) const {
        assert(i < mIndices.size());
        return mIndices[i];
    }

    T valueNonZero(unsigned int i) const {
        assert(i < mValues.size());
        return mValues[i];
    }

    SparseVector<T>& operator+=(const SparseVector<T>& x) {
        assert(mDim == x.mDim);
        for (unsigned int i = 0; i < x.nonZeroes(); ++i) {
            unsigned int idx = x.indexNonZero(i);
            T val = getValue(idx) + x.valueNonZero(i);
            setValue(idx, val);
        }
        return *this;
    }

    SparseVector<T>& operator-=(const SparseVector<T>& x) {
        assert(mDim == x.mDim);
        for (unsigned int i = 0; i < x.nonZeroes(); ++i) {
            unsigned int idx = x.indexNonZero(i);
            T val = getValue(idx) - x.valueNonZero(i);
            setValue(idx, val);
        }
        return *this;
    }
};

// computes z = x + y
template <class T>
SparseVector<T> operator+(const SparseVector<T>& x, const SparseVector<T>& y) {
    assert(x.size() == y.size());
    SparseVector<T> z = x;
    z += y;
    return z;
}

// computes z = x - y
template <class T>
SparseVector<T> operator-(const SparseVector<T>& x, const SparseVector<T>& y) {
    assert(x.size() == y.size());
    SparseVector<T> z = x;
    z -= y;
    return z;
}

// computes z = A * x (dense matrix * sparse vector → dense vector)
template <class T>
Vector<T> operator*(const Matrix<T>& A, const SparseVector<T>& x) {
    assert(A.GetNumberOfColumns() == static_cast<int>(x.size()));
    Vector<T> result(A.GetNumberOfRows());

    for (int i = 0; i < A.GetNumberOfRows(); ++i) {
        for (unsigned int j = 0; j < x.nonZeroes(); ++j) {
            unsigned int idx = x.indexNonZero(j);
            result[i] += A(i, idx) * x.valueNonZero(j);
        }
    }
    return result;
}

// computes z = x^T * A (sparse vector * dense matrix → dense vector)
template <class T>
Vector<T> operator*(const SparseVector<T>& x, const Matrix<T>& A) {
    assert(A.GetNumberOfRows() == static_cast<int>(x.size()));
    Vector<T> result(A.GetNumberOfColumns());

    for (unsigned int j = 0; j < x.nonZeroes(); ++j) {
        unsigned int idx = x.indexNonZero(j);
        T val = x.valueNonZero(j);
        for (int i = 0; i < A.GetNumberOfColumns(); ++i) {
            result[i] += val * A(idx, i);
        }
    }
    return result;
}

#endif
