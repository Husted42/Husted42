# -*- coding: utf-8 -*-
"""
@Project: LinalgDat2022
@File: GaussExtensions.py

@Description: Project B Gauss extensions

"""

import math
import sys

from Core import Matrix, Vector


def AugmentRight(A: Matrix, v: Vector) -> Matrix:
    """
    Create an augmented matrix from a matrix and a vector.

    This function creates a new matrix by concatenating matrix A
    and vector v. See page 12 in "Linear Algebra for Engineers and
    Scientists", K. Hardy.

    Parameters:
         A: M-by-N Matrix
         v: M-size Vector
    Returns:
        the M-by-(N+1) matrix (A|v)
    """
    M = A.M_Rows
    N = A.N_Cols
    if v.size() != M:
        raise ValueError("number of rows of A and length of v differ.")

    B = Matrix(M, N + 1)
    for i in range(M):
        for j in range(N):
            B[i, j] = A[i, j]
        B[i, N] = v[i]
    return B

#array2D_0007
def ElementaryRowReplacement(A: Matrix, i: int, m: float, j: int) -> Matrix:
    """
    Replace row i of A by row i of A + m times row j of A.

    Parameters:
        A: M-by-N Matrix
        i: int, index of the row to be replaced
        m: float, the multiple of row j to be added to row i
        j: int, index or replacing row.

    Returns:
        A modified in-place after row replacement.
    """
    N = A.N_Cols
    B = A.__copy__()
    lst = []
    lst2 = []
    for elm in A.Row(j):
        lst.append(elm)
    for elm in A.Row(i):
        lst2.append(elm)
    for num in range (0, len(lst)):
        lst[num] = lst2[num] + m * lst[num]
    for num2 in range (N):
        B[i, num2] = lst[num2]
    return B


def ElementaryRowInterchange(A: Matrix, i: int, j : int) -> Matrix:
    """
    Interchange row i and row j of A.

    Parameters:
        A: M-by-N Matrix
        i: int, index of the first row to be interchanged
        j: int, index the second row to be interchanged.

    Returns:
        A modified in-place after row interchange
    """
    B = A.__copy__()
    N = A.N_Cols
    for num in range(N):
        B[i, num] = A[j, num] #r_j -> r_i
        B[j, num] = A[i, num] #r_i -> r_j
    return B


def ElementaryRowScaling(A: Matrix, i: int, c: float) -> Matrix:
    """
    Replace row i of A c * row i of A.

    Parameters:
        A: M-by-N Matrix
        i: int, index of the row to be replaced
        c: float, the scaling factor

    Returns:
        A modified in-place after row scaling.
    """
    B = A.__copy__()
    N = A.N_Cols
    for num in range(N):
        B[i, num] = c * B[i, num]
    return B


def ForwardReduction(A: Matrix) -> Matrix:
    """
    Forward reduction of matrix A.

    This function performs the forward reduction of A provided in the
    assignment text to achieve row echelon form of a given (augmented)
    matrix.

    Parameters:
        A:  M-by-N augmented matrix
    returns
        M-by-N matrix which is the row-echelon form of A (performed in-place,
        i.e., A is modified directly).
    """
    M = A.M_Rows
    N = A.N_Cols
    r1 = 0
    for j in range(N):
        for i in range(r1, M): 
            ifNotZero = A[i, j] != 0
            if ifNotZero: #First non-zero
                A = ElementaryRowInterchange(A, i, r1) 
                for row in range(r1 + 1, M):
                    ifNotZero2 = A[i, j] != 0
                    if ifNotZero2:
                        scalarMultiple  = -1 * A[row, j] / A[i,j]
                        A = ElementaryRowReplacement(A, row, scalarMultiple, r1) #row operation to get A[row, j] == 0
                r1 = r1 + 1
                break
    return A


def BackwardReduction(A: Matrix) -> Matrix:
    """
    Backward reduction of matrix A.

    This function performs the forward reduction of A provided in the
    assignment text given a matrix A in row echelon form.

    Parameters:
        A:  M-by-N augmented matrix in row-echelon form
    returns
        M-by-N matrix which is the reduced form of A (performed in-place,
        i.e., A is modified directly).
    """
    raise NotImplementedError()


def GaussElimination(A: Matrix, v: Vector) -> Vector:
    """
    Perform Gauss elimination to solve for Ax = v.

    This function performs Gauss elimination on a linear system given
    in matrix form by a coefficient matrix and a right-hand-side vector.
    It is assumed that the corresponding linear system is consistent and
    has exactly one solution.

    Hint: combine AugmentRight, ForwardReduction and BackwardReduction!

    Parameters:
         A: M-by_N coefficient matrix of the system
         v: N-size vector v, right-hand-side of the system.
    Return:
         M-size solution vector of the system.
    """
    raise NotImplementedError()
