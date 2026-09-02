#ifndef MATRIXHEADERDEF
#define MATRIXHEADERDEF

#include "Vector.hpp"
#include <vector>
#include <cassert>
#include <cmath>

template <typename T>
class Matrix
{
private:
    std::vector<T> mData; // flattened row-major storage
    int mNumRows, mNumCols; // dimensions

public:
    // copy constructor (defaulted)
    Matrix(const Matrix& otherMatrix) = default;

    Matrix(int numRows, int numCols)
    {
        assert(numRows > 0);
        assert(numCols > 0);

        mNumRows = numRows;
        mNumCols = numCols;
        mData.resize(mNumRows * mNumCols, T());
    }

    // destructor (defaulted)
    ~Matrix() = default;

    int GetNumberOfRows() const
    {
        return mNumRows;
    }

    int GetNumberOfColumns() const
    {
        return mNumCols;
    }

    T& operator()(int i, int j)
    {
        assert(i >= 0 && i < mNumRows);
        assert(j >= 0 && j < mNumCols);

        return mData[i * mNumCols + j];
    }

    const T& operator()(int i, int j) const
    {
        assert(i >= 0 && i < mNumRows);
        assert(j >= 0 && j < mNumCols);

        return mData[i * mNumCols + j];
    }

    // overloaded assignment operator (defaulted)
    Matrix& operator=(const Matrix& otherMatrix) = default;

    Matrix operator-() const // unary -
    {
        Matrix mat(mNumRows, mNumCols);
        for (int i = 0; i < mNumRows; i++)
        {
            for (int j = 0; j < mNumCols; j++)
            {
                mat(i, j) = -(*this)(i, j);
            }
        }
        return mat;
    }

    Matrix operator+(const Matrix& m1) const // binary +
    {
        assert(mNumRows == m1.mNumRows);
        assert(mNumCols == m1.mNumCols);

        Matrix mat(mNumRows, mNumCols);
        for (int i = 0; i < mNumRows; i++)
        {
            for (int j = 0; j < mNumCols; j++)
            {
                mat(i, j) = (*this)(i, j) + m1(i, j);
            }
        }
        return mat;
    }

    Matrix operator-(const Matrix& m1) const // binary -
    {
        assert(mNumRows == m1.mNumRows);
        assert(mNumCols == m1.mNumCols);

        Matrix mat(mNumRows, mNumCols);
        for (int i = 0; i < mNumRows; i++)
        {
            for (int j = 0; j < mNumCols; j++)
            {
                mat(i, j) = (*this)(i, j) - m1(i, j);
            }
        }
        return mat;
    }

    // scalar multiplication
    Matrix operator*(T a) const
    {
        Matrix mat(mNumRows, mNumCols);
        for (int i = 0; i < mNumRows; i++)
        {
            for (int j = 0; j < mNumCols; j++)
            {
                mat(i, j) = a * (*this)(i, j);
            }
        }
        return mat;
    }

    // new: provide const reference to internal storage
    const std::vector<T>& getStorage() const
    {
        return mData;
    }
};

// matrix-vector multiplications (template)
template <typename T>
Vector<T> operator*(const Matrix<T>& m, const Vector<T>& v)
{
    int original_vector_size = v.size();
    assert(m.GetNumberOfColumns() == original_vector_size);

    int new_vector_length = m.GetNumberOfRows();
    Vector<T> new_vector(new_vector_length);

    for (int i = 0; i < new_vector_length; i++)
    {
        for (int j = 0; j < original_vector_size; j++)
        {
            new_vector[i] += m(i, j) * v[j];
        }
    }

    return new_vector;
}

template <typename T>
Vector<T> operator*(const Vector<T>& v, const Matrix<T>& m)
{
    int original_vector_size = v.size();
    assert(m.GetNumberOfRows() == original_vector_size);

    int new_vector_length = m.GetNumberOfColumns();
    Vector<T> new_vector(new_vector_length);

    for (int i = 0; i < new_vector_length; i++)
    {
        for (int j = 0; j < original_vector_size; j++)
        {
            new_vector[i] += v[j] * m(j, i);
        }
    }

    return new_vector;
}

#endif
