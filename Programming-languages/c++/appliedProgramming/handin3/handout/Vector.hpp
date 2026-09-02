#ifndef VECTORHEADERDEF
#define VECTORHEADERDEF

#include <cassert>
#include <cmath>
#include <vector>

template <typename T>
class Vector
{
private:
    std::vector<T> mData; // data stored in vector

public:
    // copy constructor (let compiler handle it, but kept for exact interface)
    Vector(const Vector& otherVector) = default;

    Vector(int size)
    {
        assert(size > 0);
        mData.resize(size, T());
    }

    // destructor (let compiler handle it)
    ~Vector() = default;

    int size() const
    {
        return static_cast<int>(mData.size());
    }

    T& operator[](int i)
    {
        assert(i >= 0 && i < static_cast<int>(mData.size()));
        return mData[i];
    }

    const T& operator[](int i) const
    {
        assert(i >= 0 && i < static_cast<int>(mData.size()));
        return mData[i];
    }

    // assignment operator (let compiler handle it)
    Vector& operator=(const Vector& otherVector) = default;

    // overloading the unary - operator
    Vector operator-() const
    {
        Vector v(mData.size());
        for (int i = 0; i < static_cast<int>(mData.size()); i++)
        {
            v[i] = -mData[i];
        }
        return v;
    }

    // overloading the binary + operator
    Vector operator+(const Vector& v1) const
    {
        assert(mData.size() == v1.mData.size());

        Vector v(mData.size());
        for (int i = 0; i < static_cast<int>(mData.size()); i++)
        {
            v[i] = mData[i] + v1.mData[i];
        }
        return v;
    }

    // overloading the binary - operator
    Vector operator-(const Vector& v1) const
    {
        assert(mData.size() == v1.mData.size());

        Vector v(mData.size());
        for (int i = 0; i < static_cast<int>(mData.size()); i++)
        {
            v[i] = mData[i] - v1.mData[i];
        }
        return v;
    }

    // scalar multiplication (fixed to use T type instead of double)
    Vector operator*(T a) const
    {
        Vector v(mData.size());
        for (int i = 0; i < static_cast<int>(mData.size()); i++)
        {
            v[i] = a * mData[i];
        }
        return v;
    }

    // p-norm method (still works if T is numeric)
    double CalculateNorm(int p = 2) const
    {
        double sum = 0.0;
        for (int i = 0; i < static_cast<int>(mData.size()); i++)
        {
            sum += pow(std::abs(mData[i]), p);
        }
        return pow(sum, 1.0 / static_cast<double>(p));
    }

    // new: provide const reference to internal storage
    const std::vector<T>& getStorage() const
    {
        return mData;
    }
};

#endif
