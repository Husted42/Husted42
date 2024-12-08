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

# NB - Koden er foklaret i afleveringen

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

    :param A: an M-by-N Matrix.
    :param v: a size N Vector.

    :return: a size M Vector y such that y = A.v
    """
    array = []
    for j in range(0, len(A.Column(0))): #Iterate throgh columns
        lst = []
        for i in range (0, (len(A.Row(0)))):  #Iterate throgh rows
            lst.append(A.Row(j)[i] * v[i])
        array.append(_sum(lst))
    return(Vector.fromArray(array))


def MatrixProduct(A: Matrix, B: Matrix) -> Matrix:
    """
    Compute the Matrix product of two given matrices A and . B.

    :param A: an M-by-N Matrix.
    :param B: an N-by-P Matrix.

    :returns: the M-by-P Matrix A*B.
    """
    Arow = A.M_Rows
    Acol = A.N_Cols
    Bcol = B.N_Cols
    result = Matrix( Arow, Bcol ) # 0-matrix of size MxP

    #Iterate over rows
    for k in range (0, Arow):
        #Iterate over columns / through rows
        for j in range (0, Bcol):
            elmLst = []
            #Calculate element
            for i in range (0, Acol):
                elmLst.append(A.__getitem__((k,i)) * B.__getitem__((i,j)))
            result.__setitem__((k,j), _sum(elmLst))
    return result

def Transpose(A: Matrix) -> Matrix:
    """
    Computes the transpose of a given Matrix.

    :param A: A N-by-M Matrix.
    :returns: A M-by-N Matrix B such that B = A^T.
    """
    n = A.M_Rows
    m = A.N_Cols
    result = Matrix( m, n )
    for j in range (0, A.M_Rows): #Iterate throgh rows
        for i in range(0, A.N_Cols): #Iterate throgh columns
            result.__setitem__((i, j), A.__getitem__((j,i)))
    return(result)


def VectorNorm(v: Vector) -> float:
    """
    Computes the Euclidean Vector norm of a given Vector.

    :param v: An N - dimensional Vector.
    :return: The Euclidean norm of the Vector.
    """

    lst = [] # Array of every element squared
    for i in range (0, v.__len__()):
        lst.append((v[i]) ** 2)
    return(math.sqrt(_sum(lst)))

