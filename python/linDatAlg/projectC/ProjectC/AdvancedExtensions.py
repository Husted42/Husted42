# -*- coding: utf-8 -*-
"""
@Project: LinalgDat2022
@File: AdvancedExtensions.py

@Description: Project C Determinant and Gram-Schmidt extensions.

"""

import math
import sys

from Core import Matrix, Vector

Tolerance = 1e-6


def SquareSubMatrix(A: Matrix, i: int, j: int) -> Matrix:
    """
    This function creates the square submatrix given a square matrix as
    well as row and column indices to remove from it.

    Remarks:
        See page 246-247 in "Linear Algebra for Engineers and Scientists"
        by K. Hardy.

    Parameters:
        A:  N-by-N matrix
        i: int. The index of the row to remove.
        j: int. The index of the column to remove.

    Return: 
        The resulting (N - 1)-by-(N - 1) submatrix.
    """
    m = A.M_Rows
    n = A.N_Cols
    row, col = i, j
    supA = Matrix(n - 1, m - 1)
    for k in range(n): 
        if k == row: continue #Skip element for columns to be removed
        else:
            for l in range(m): #Skip element for rows to be removed
                if l == col: continue
                else: supA[k - (k > row), l - (l > col)] = A[k, l]
    return supA 


#Determinants of order 2 
def detToByTo(A: Matrix) -> Matrix:
    return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

def Determinant(A: Matrix) -> float:
    """
    This function computes the determinant of a given square matrix.

    Remarks:
        * See page 247 in "Linear Algebra for Engineers and Scientists"
        by K. Hardy.
        * Hint: Use SquareSubMatrix.

    Parameter:
        A: N-by-N matrix.

    Return:
        The determinant of the matrix.
    """
    m = A.M_Rows
    n = A.N_Cols
    det = 0

    if m == 2: return detToByTo(A) 

    #Recursive formular
    for j in range(n):
        det += (-1)**j * A[0, j] * Determinant(SquareSubMatrix(A, 0, j))
    return det 


def VectorNorm(v: Vector) -> float:
    """
    This function computes the Euclidean norm of a Vector. This has been implemented
    in Project A and is provided here for convenience

    Parameter:
         v: Vector

    Return:
         Euclidean norm, i.e. (\sum v[i]^2)^0.5
    """
    nv = 0.0
    for i in range(len(v)):
        nv += v[i]**2 
    return math.sqrt(nv) 


def SetColumn(A: Matrix, v: Vector, j: int) -> Matrix:
    """
    This function copies Vector 'v' as a column of Matrix 'A'
    at column position j.

    Parameters:
        A: M-by-N Matrix.
        v: size M vector
        j: int. Column number.

    Return:
        Matrix A  after modification.

    Raise:
        ValueError if j is out of range or if len(v) != A.M_Rows.
    """
    return None


def GramSchmidt(A: Matrix) -> tuple:
    """
    This function computes the Gram-Schmidt process on a given matrix.

    Remarks:
        See page 229 in "Linear Algebra for Engineers and Scientists"
        by K. Hardy.

    Parameter:
        A: M-by-N matrix. All columns are implicitly assumed linear
        independent.

    Return:
        tuple (Q,R) where Q is a M-by-N orthonormal matrix and R is an
        N-by-N upper triangular matrix.
    """
    m = A.M_Rows
    n = A.N_Cols
    Q, R = Matrix(m, n),  Matrix(n, n)
    v = Vector(m) 

    for j in range(n): 
        for i in range(m): v[i] = A[i, j]  # q_j = u_j

        for i in range(j): 
            q = Vector.fromArray(Q.Column(i)) #Q^T_i
            R[i, j] = q @ v #r_ij = q^T u_j
            v -= R[i, j] * q #q_j  = q_j - r_ij q_i

        if v == 0: continue
        R[j, j] = VectorNorm(v) # r_jj = ||q_j|| 
        for i in range(m): #q_j = q_j / r_jj
            Q[i, j] = v[i] / R[j, j] 

    return (Q, R)