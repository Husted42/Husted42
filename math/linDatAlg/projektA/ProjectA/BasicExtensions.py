"""
@Project: LinalgDat2023
@File: BasicExtensions.py

@Description: Project A basic extensions.

"""
import math
import sys

sys.path.append('../Core')
from Vector import Vector
from Matrix import Matrix

__author__ = "François Lauze, University of Copenhagen"
__date__ = "3/28/22"
__version__ = "0.0.1"


def AugmentRight(A: Matrix, v: Vector) -> Matrix:
    """
    Create an augmented matrix from a matrix A and a vector v.

    See page 12 in 'Linear Algebra for Engineers and Scientists'
    by K. Hardy.

    :param A: a matrix of size M-by-N.
    :param v: a column vector of size M.

    :return: a matrix of size M-by-(N + 1)
    """
    M = A.M_Rows
    N = A.N_Cols
    B = Matrix(M, N + 1)
    for i in range(M):
        for j in range(N):
            B[i, j] = A[i, j]
    for i in range(M):
        B[i, N] = v[i]

    return B

''' returns the sum of an array'''
def _sum(input):
    sum = 0
    for i in input:
        sum = sum + i
    return sum

def MatVecProduct(A: Matrix, v: Vector) -> Vector:
    """
    This function computes the matrix-vector product of a matrix A
    and a column vector v

    See page 68 in "Linear Algebra for Engineers and Scientists"
    by K. Hardy.
    :param A: an M-by-N Matrix.
    :param v: a size N Vector.

    :return: a size M Vector y such that y = A.v
    """
    array = []
    for j in range(0, len(A.Column(0))):
        lst = []
        for i in range (0, (len(A.Row(0)))):
            lst.append(A.Row(j)[i] * v[i])
        array.append(_sum(lst))
    return(Vector.fromArray(array))


def MatrixProduct(A: Matrix, B: Matrix) -> Matrix:
    """
    Compute the Matrix product of two given matrices A and B.

    See page 58 in "Linear Algebra for Engineers and Scientists"
    by K. Hardy.

    :param A: an M-by-N Matrix.
    :param B: an N-by-P Matrix.

    :returns: the M-by-P Matrix A*B.
    """
    raise NotImplementedError("MatrixProduct is not implemented!")


def Transpose(A: Matrix) -> Matrix:
    """
    Computes the transpose of a given Matrix.

    See page 69 in "Linear Algebra for Engineers and Scientists"
    by K. Hardy.

    :param A: A M-by-N Matrix.
    :returns: A N-by-M Matrix B such that B = A^T.
    """
    raise NotImplementedError("Transpose is not implemented!")


def VectorNorm(v: Vector) -> float:
    """
    Computes the Euclidean Vector norm of a given Vector.

    See page 197 in "Linear Algebra for Engineers and Scientists"
    by K.Hardy.

    :param v: An N - dimensional Vector.
    :return: The Euclidean norm of the Vector.
    """
    raise NotImplementedError("VectorNorm is not implemented!")
