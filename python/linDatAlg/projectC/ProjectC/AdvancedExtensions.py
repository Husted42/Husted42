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
    M_Rows = A.M_Rows
    N_Cols = A.N_Cols

    if M_Rows != N_Cols:
        raise ValueError("Matrix is not square")

    if i < 0 or i >= M_Rows:
        raise ValueError("Row index out of range")
    
    if j < 0 or j >= N_Cols:
        raise ValueError("Column index out of range")
    
    if M_Rows == 1: # If the matrix is 1-by-1, return an empty matrix
        return Matrix(0, 0) # Return an empty matrix
    
    B = Matrix(M_Rows - 1, N_Cols - 1) # Initialize the submatrix
    for k in range(M_Rows): # Loop over rows
        if k == i: # If the row is the one to remove, skip it
            continue
        for l in range(N_Cols): # Loop over columns
            if l == j: # If the column is the one to remove, skip it
                continue
            B[k - (k > i), l - (l > j)] = A[k, l] # Set the (k - (k > i))-th row and (l - (l > j))-th column of B to A[k, l]
    return B # Return the submatrix


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
    if A.M_Rows != A.N_Cols:
        raise ValueError("Matrix is not square")
    if A.M_Rows == 1: # If the matrix is 1-by-1, return the only entry
        return A[0, 0] # Return the only entry of the matrix
    if A.M_Rows == 2: # If the matrix is 2-by-2, return the determinant
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0] # Compute the determinant of a 2-by-2 matrix
    det = 0.0 # Initialize the determinant
    for j in range(A.N_Cols): # Loop over columns
        det += (-1)**j * A[0, j] * Determinant(SquareSubMatrix(A, 0, j)) # Compute the determinant of the j-th submatrix and add it to det
    return det # Return the determinant


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
    for i in range(len(v)): # Loop over entries
        nv += v[i]**2 # Add the square of the i-th entry to nv
    return math.sqrt(nv) # Return the square root of nv


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
    if len(v) != A.M_Rows:
        raise ValueError("Vector length mismatch")
    if j < 0 or j >= A.N_Cols:
        raise ValueError("Column index out of range")
    
    for i in range(A.M_Rows): # Loop over rows
        A[i, j] = v[i] # Set the i-th row of column j to v[i]
    return A # Return the modified matrix


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
    M, N = A.M_Rows, A.N_Cols
    Q = Matrix(M, N)  # Initialize Q as an M-by-N matrix
    R = Matrix(N, N)  # Initialize R as an N-by-N matrix

    for j in range(N): # Loop over columns
        v = Vector(M)  # Create a new Vector of length M
        for i in range(M): # Loop over rows
            v[i] = A[i, j]  # Assign the values from the j-th column of A to the Vector

        for i in range(j): # Loop over columns
            q = Vector.fromArray(Q.Column(i))  # Get the i-th column of Q as a Vector
            R[i, j] = q @ v  # Compute the inner product q @ v
            v -= q * R[i, j]  # Subtract the projection of v onto q

        R[j, j] = VectorNorm(v)  # Compute the norm of the updated v
        for i in range(M):
            Q[i, j] = v[i] / R[j, j]  # Normalize v and set the j-th column of Q

    return Q, R # Return the tuple (Q, R)