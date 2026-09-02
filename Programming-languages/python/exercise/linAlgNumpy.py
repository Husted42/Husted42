##### -- Imports -- #####
import numpy as np

##### -- Variables -- #####
#Arrays
a1 = np.array([4,8,16])
a2 = np.zeros((2,3))
a3 = np.zeros((2,3))
a4 = np.zeros((6,5,7,8))
a5 = np.array([1,2,3])

#Matricies
m1 = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
m2 = np.matrix([[7,9,13], [42,69,420], [6,6,6]])
m3 = np.matrix([[1,2,3], [4,5,6]])
m4 = np.matrix([[-2,0,1], [-1,7,1], [5,-1,1]])

##### -- Functions -- #####
'''
    :param A: a matrix of size M-by-N.
    :return : Boolean value
'''
def isNull(A):
    if A.all() != 0: return False
    else: return True

'''
    :param A: a matrix of size M-by-N.
    :param v: a column vector of size M.
    :return: a matrix of size M-by-(N + 1)    
'''
def augmentRight(A, v):
    A = np.c_[A, v]
    return A

'''
    :param A: an M-by-N Matrix.
    :param v: a size N Vector.
    :return: a size M Vector y such that y = A.v
'''
def matVecProduct(A, v):
    return A.dot(v)

'''
:param A: an M-by-N Matrix.
:param B: an N-by-P Matrix.

:returns: the M-by-P Matrix A*B.
'''
def MatrixProduct(A,B):
    return A*B

'''
:param A: A N-by-M Matrix.
:returns: A M-by-N Matrix B such that B = A^T.
'''
def transpose(A):
    return np.transpose(A)

'''
:param v: An N - dimensional Vector.
:return: The Euclidean norm of the Vector.
'''
def vectorNorm(v):
    return np.linalg.norm(v)

'''
Parameters:
    A: M-by-N Matrix
    i: int, index of the row to be replaced
    m: float, the multiple of row j to be added to row i
    j: int, index or replacing row.

Returns:
    A modified in-place after row replacement.
'''
def elementaryRowReplacement(A, i, m, j):
    A[i, :] = A[i, :] + A[j, :] * m
    return A

'''
Parameters:
        A: M-by-N Matrix
        i: int, index of the first row to be interchanged
        j: int, index the second row to be interchanged.

    Returns:
        A modified in-place after row interchange
'''
def elementaryRowInterchange(A, i, j):
    i,j = i-1,j-1
    A[[i,j]] = A[[j,i]]
    return A

'''
Parameters:
    A: M-by-N Matrix
    i: int, index of the row to be replaced
    c: float, the scaling factor

Returns:
    A modified in-place after row scaling.
'''
def elementaryRowScaling(A, i, c):
    A[i,:] = A[i,:] * c 
    return A

'''
Parameters:
    A:  M-by-N augmented matrix
returns
    M-by-N matrix which is the row-echelon form of A (performed in-place,
    i.e., A is modified directly).
'''
def forwardReduction(A):
    mRow, nCol = A.shape
    entry = 0
    for j in range(0, mRow):
        for i in range(entry, mRow):
            if A[i, j] != 0:
                A = elementaryRowInterchange(A, i, entry) 
                for k in range(entry+1, mRow):
                    if A[i,j] != 0:
                        A = elementaryRowReplacement(A, k, (-1 * A[k, j] / A[i,j]), entry)
                entry = entry + 1
                break
    return A

'''
Parameters:
    A:  M-by-N augmented matrix in row-echelon form
returns
    M-by-N matrix which is the reduced form of A (performed in-place,
    i.e., A is modified directly).
'''
def backwardReduction(A):
    A = transpose(A)
    A = forwardReduction(A)
    A = transpose(A)
    return A

'''
Parameters:
    A: M-by_N coefficient matrix of the system
Return:
    identity matrix.
'''
def gaussElimination(A):
    mRow, nCol = A.shape
    A = forwardReduction(A)
    A = backwardReduction(A)
    for i in range (nCol):
        A[i,i] = 1/A[i,i] * A[i,i]
    return A

##### -- Calls -- #####
print('isNull: ', isNull(a1), isNull(a2), isNull(a3), isNull(a4))
print('augmentRight:\n', augmentRight(m1, a5), '\n')
print('matVecProduct:\n',matVecProduct(m1, a5), '\n')
print('MatrixProduct:\n',MatrixProduct(m1, m2), '\n')
print('transpose:\n',transpose(m1), '\n')
print('vectorNorm:\n',vectorNorm(m1), '\n')
print('augmentRight:\n', elementaryRowReplacement(m1, 2, 3, 1), '\n')
print('elementaryRowInterchange:\n', elementaryRowInterchange(m1, 1, 2), '\n')
print('elementaryRowScaling:\n', elementaryRowScaling(m1, 1, 2), '\n')
print('forwardReduction:\n', forwardReduction(m1), '\n')
print('backwardReduction:\n', backwardReduction(m1), '\n')
print('gaussElimination:\n', gaussElimination(m4), '\n')