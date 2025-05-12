# -*- coding: utf-8 -*-
"""
@Project: LinalgDat23
@File: ldtonumpy.py

@Description: LinalgDat toNumpy Vector/Matrix conversion

"""

import numpy as np
import Matrix
import Vector

__author__ = "François Lauze, University of Copenhagen"
__date__ = "4/19/23"
__version__ = "0.0.1"


def to_numpy_vector(vector: Vector) -> np.ndarray:
    """Convert a Vector to a (n,1) or (1,n) numpy array."""
    n = len(vector)
    v = np.zeros(n)
    for i in range(n):
        v[i] = vector[i]
    if vector.mode == 'column':
        v.shape = n, 1
    else:
        v.shape = 1, n
    return v

def to_numpy_matrix(matrix: Matrix) -> np.ndarray:
    """Convert a Matrix to a 2D numpy array."""
    m = matrix.M_Rows()
    n = matrix.N_Cols()
    M = np.zeros((m, n))
    for i in range(m):
       for j in range(n):
           M[i, j] = matrix[i, j]
    return m



def toNumpy(array) -> np.ndarray:
    """Convert array to numpy when a is either a Vector or a Matrix."""
    t_array = type(array)
    if t_array not in (Vector, Matrix):
        raise TypeError(f"Expected a Matrix or a Vector, got a {str(t_array)} instead.")
    return to_numpy_vector(array) if t_array == Vector else to_numpy_matrix(array)
    