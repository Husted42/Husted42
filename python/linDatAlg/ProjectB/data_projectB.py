"""
@project: LinalgDat2023 Projekt B
@file: data_projektB.py

@description: data and routines to test GaussExtension module.
Do not modify, this file is automatically generated.

@author: François Lauze, University of Copenhagen
@date: Friday May 05. 2023

random state = d3ed9935-e73c-48c4-ae21-a4f3332e2729
"""
from Core import Matrix
from Core import Vector



# Matrix size = (11, 11)
array2D_0001 = [[  6.41000,  -1.37000,   7.48000,  -6.54000,  -8.68000,  -7.27000,   9.15000,   6.77000,   4.28000,  -7.01000,   0.98000],
                [  8.78000,  -6.36000,   1.97000,  -2.14000,   4.70000,  -9.52000,  -8.99000,  -6.62000,   9.80000,   4.14000,  -4.24000],
                [  0.54000,  -2.30000,  -4.69000,   6.96000,  -7.38000,  -2.80000,   7.13000,   5.36000,  -6.75000,  -8.38000,   6.75000],
                [ -4.71000,  -5.97000,   0.52000,  -2.88000,   8.18000,  -8.91000,  -2.39000,  -2.69000,  -8.81000,  -4.98000,  -8.14000],
                [ -6.16000,   2.58000,  -3.91000,   4.88000,   6.81000,  -8.16000,  -1.20000,   2.01000,  -2.81000,   4.91000,   8.54000],
                [ -4.83000,   5.93000,  -4.88000,  -4.59000,  -1.07000,   6.54000,   0.28000,  -0.18000,  -2.63000,  -4.64000,   2.82000],
                [  0.80000,  -4.05000,  -8.52000,   2.02000,   9.66000,   5.19000,   0.09000,   0.10000,  -4.78000,  -4.81000,  -4.49000],
                [  5.82000,   7.31000,  -5.76000,  -6.75000,   4.76000,   2.21000,   7.85000,  -0.65000,   0.05000,   9.45000,  -2.81000],
                [  8.50000,  -0.92000,  -2.15000,  -1.73000,  -9.15000,   4.25000,   1.99000,  -3.36000,   4.96000,   7.63000,  -5.79000],
                [  7.15000,   3.52000,   0.15000,   6.39000,  -6.14000,  -7.70000,  10.00000,  -7.76000,  -9.94000,  -7.06000,  -2.69000],
                [  1.69000,  -5.01000,   4.60000,   8.18000,  -4.17000,   7.53000,   1.65000,   2.14000,  -7.22000,   9.83000,  -2.80000]]
Matrix_0000 = Matrix.fromArray(array2D_0001)
Pair_0002 = (4, 0)
Float_0003 = 2.25000
array2D_0005 = [[  6.41000,  -1.37000,   7.48000,  -6.54000,  -8.68000,  -7.27000,   9.15000,   6.77000,   4.28000,  -7.01000,   0.98000],
                [  8.78000,  -6.36000,   1.97000,  -2.14000,   4.70000,  -9.52000,  -8.99000,  -6.62000,   9.80000,   4.14000,  -4.24000],
                [  0.54000,  -2.30000,  -4.69000,   6.96000,  -7.38000,  -2.80000,   7.13000,   5.36000,  -6.75000,  -8.38000,   6.75000],
                [ -4.71000,  -5.97000,   0.52000,  -2.88000,   8.18000,  -8.91000,  -2.39000,  -2.69000,  -8.81000,  -4.98000,  -8.14000],
                [  8.26250,  -0.50250,  12.92000,  -9.83500, -12.72000, -24.51750,  19.38750,  17.24250,   6.82000, -10.86250,  10.74500],
                [ -4.83000,   5.93000,  -4.88000,  -4.59000,  -1.07000,   6.54000,   0.28000,  -0.18000,  -2.63000,  -4.64000,   2.82000],
                [  0.80000,  -4.05000,  -8.52000,   2.02000,   9.66000,   5.19000,   0.09000,   0.10000,  -4.78000,  -4.81000,  -4.49000],
                [  5.82000,   7.31000,  -5.76000,  -6.75000,   4.76000,   2.21000,   7.85000,  -0.65000,   0.05000,   9.45000,  -2.81000],
                [  8.50000,  -0.92000,  -2.15000,  -1.73000,  -9.15000,   4.25000,   1.99000,  -3.36000,   4.96000,   7.63000,  -5.79000],
                [  7.15000,   3.52000,   0.15000,   6.39000,  -6.14000,  -7.70000,  10.00000,  -7.76000,  -9.94000,  -7.06000,  -2.69000],
                [  1.69000,  -5.01000,   4.60000,   8.18000,  -4.17000,   7.53000,   1.65000,   2.14000,  -7.22000,   9.83000,  -2.80000]]
Matrix_0004 = Matrix.fromArray(array2D_0005)
# Matrix size = (13, 14)
array2D_0007 = [[ -6.52000,   3.71000,   8.60000,   2.20000,  -2.64000,  -6.18000,  -5.84000,   3.99000,  -8.04000,  -5.80000,   4.43000,  -2.66000,   9.33000,  -1.12000],
                [ -4.20000,   7.18000,  -3.72000,   8.79000,  -4.09000,   8.66000,   5.42000,   5.56000,  -7.22000,  -6.77000,   4.65000,  -7.70000,  -9.51000,   6.45000],
                [  5.97000,   0.25000,  -1.84000,   3.41000,  -3.93000,  -8.96000,  -6.65000,  -5.92000,   1.32000,  -7.09000,   2.96000,  -8.83000,  -8.81000,   2.36000],
                [  3.23000,  -9.90000,   7.04000,  -5.42000,   2.78000,   7.97000,   1.19000,  -5.16000,   9.55000,   1.86000,  -8.66000,  -1.97000,  -8.28000,   7.66000],
                [ -4.03000,  -4.94000,   7.95000,  -8.75000,  -0.28000,  -9.65000,  -3.27000,  -8.51000,  -5.62000,  -2.21000,   3.19000,   4.62000,   9.54000,   9.59000],
                [  3.18000,  -2.03000,  -2.42000,   0.16000,   2.53000,  -1.47000,  -5.11000,   6.03000,   5.09000,   3.73000,   3.54000,   8.18000,  -2.90000,  -9.90000],
                [  3.10000,   7.88000,  -8.07000,  -3.43000,  -9.55000,   6.14000,  -9.36000,   8.55000,   1.49000,  -7.02000,   8.09000,   0.80000,   8.57000,  -5.37000],
                [  0.80000,  -3.79000,   7.72000,  -9.14000,   4.13000,  -5.85000,   0.32000,  -5.04000,   5.83000,  -2.92000,  -7.67000,   8.46000,  -4.30000,  -3.17000],
                [ -2.17000,   4.87000,  -9.77000,   3.42000,   9.14000,  -1.66000,   6.99000,   6.95000,   1.52000,  -4.27000,   3.75000,  -4.21000,  -7.63000,   6.25000],
                [ -6.85000,   7.21000,  -4.41000,  -9.36000,  -4.48000,   3.11000,   8.88000,   4.71000,   3.44000,   5.91000,  -6.28000,   2.69000,  -6.91000,  -4.48000],
                [ -9.73000,  -3.75000,  -8.66000,   8.05000,   7.35000,  -0.94000,  -5.66000,   5.99000,   3.41000,   3.31000,  -7.84000,   7.89000,  -3.10000,  -4.24000],
                [ -7.43000,  -2.84000,   3.92000,  -5.87000,  -1.06000,   5.80000,   2.42000,  -9.87000,  -2.41000,  -9.49000,  -9.60000,   4.08000,   2.25000,   9.66000],
                [  2.34000,  -4.12000,  -6.18000,   1.36000,   8.60000,   8.95000,  -2.21000,  -2.71000,  -8.70000,   5.80000,   1.35000,  -8.02000,  -3.18000,  -9.73000]]
Matrix_0006 = Matrix.fromArray(array2D_0007)
Pair_0008 = (4, 10)
Float_0009 = 6.81000
array2D_0011 = [[ -6.52000,   3.71000,   8.60000,   2.20000,  -2.64000,  -6.18000,  -5.84000,   3.99000,  -8.04000,  -5.80000,   4.43000,  -2.66000,   9.33000,  -1.12000],
                [ -4.20000,   7.18000,  -3.72000,   8.79000,  -4.09000,   8.66000,   5.42000,   5.56000,  -7.22000,  -6.77000,   4.65000,  -7.70000,  -9.51000,   6.45000],
                [  5.97000,   0.25000,  -1.84000,   3.41000,  -3.93000,  -8.96000,  -6.65000,  -5.92000,   1.32000,  -7.09000,   2.96000,  -8.83000,  -8.81000,   2.36000],
                [  3.23000,  -9.90000,   7.04000,  -5.42000,   2.78000,   7.97000,   1.19000,  -5.16000,   9.55000,   1.86000,  -8.66000,  -1.97000,  -8.28000,   7.66000],
                [-70.29130, -30.47750, -51.02460,  46.07050,  49.77350, -16.05140, -41.81460,  32.28190,  17.60210,  20.33110, -50.20040,  58.35090, -11.57100, -19.28440],
                [  3.18000,  -2.03000,  -2.42000,   0.16000,   2.53000,  -1.47000,  -5.11000,   6.03000,   5.09000,   3.73000,   3.54000,   8.18000,  -2.90000,  -9.90000],
                [  3.10000,   7.88000,  -8.07000,  -3.43000,  -9.55000,   6.14000,  -9.36000,   8.55000,   1.49000,  -7.02000,   8.09000,   0.80000,   8.57000,  -5.37000],
                [  0.80000,  -3.79000,   7.72000,  -9.14000,   4.13000,  -5.85000,   0.32000,  -5.04000,   5.83000,  -2.92000,  -7.67000,   8.46000,  -4.30000,  -3.17000],
                [ -2.17000,   4.87000,  -9.77000,   3.42000,   9.14000,  -1.66000,   6.99000,   6.95000,   1.52000,  -4.27000,   3.75000,  -4.21000,  -7.63000,   6.25000],
                [ -6.85000,   7.21000,  -4.41000,  -9.36000,  -4.48000,   3.11000,   8.88000,   4.71000,   3.44000,   5.91000,  -6.28000,   2.69000,  -6.91000,  -4.48000],
                [ -9.73000,  -3.75000,  -8.66000,   8.05000,   7.35000,  -0.94000,  -5.66000,   5.99000,   3.41000,   3.31000,  -7.84000,   7.89000,  -3.10000,  -4.24000],
                [ -7.43000,  -2.84000,   3.92000,  -5.87000,  -1.06000,   5.80000,   2.42000,  -9.87000,  -2.41000,  -9.49000,  -9.60000,   4.08000,   2.25000,   9.66000],
                [  2.34000,  -4.12000,  -6.18000,   1.36000,   8.60000,   8.95000,  -2.21000,  -2.71000,  -8.70000,   5.80000,   1.35000,  -8.02000,  -3.18000,  -9.73000]]
Matrix_0010 = Matrix.fromArray(array2D_0011)
# Matrix size = (11, 3)
array2D_0013 = [[  1.16000,   1.24000,  -0.80000],
                [  0.08000,  -6.62000,   9.88000],
                [ -4.67000,  -0.93000,  -9.98000],
                [ -0.52000,   5.38000,   5.69000],
                [  9.38000,   5.73000,  -7.46000],
                [ -9.64000,   5.12000,  -7.58000],
                [  0.68000,   2.22000,  -8.49000],
                [  8.01000,  -0.45000,   9.14000],
                [ -2.82000,   0.74000,  -8.84000],
                [  0.84000,   9.85000,  -6.42000],
                [  7.33000,  -7.77000,  -4.95000]]
Matrix_0012 = Matrix.fromArray(array2D_0013)
Pair_0014 = (9, 7)
Float_0015 = 2.19000
array2D_0017 = [[  1.16000,   1.24000,  -0.80000],
                [  0.08000,  -6.62000,   9.88000],
                [ -4.67000,  -0.93000,  -9.98000],
                [ -0.52000,   5.38000,   5.69000],
                [  9.38000,   5.73000,  -7.46000],
                [ -9.64000,   5.12000,  -7.58000],
                [  0.68000,   2.22000,  -8.49000],
                [  8.01000,  -0.45000,   9.14000],
                [ -2.82000,   0.74000,  -8.84000],
                [ 18.38190,   8.86450,  13.59660],
                [  7.33000,  -7.77000,  -4.95000]]
Matrix_0016 = Matrix.fromArray(array2D_0017)

ERRMatrixList = [Matrix_0000, Matrix_0006, Matrix_0012]
ERRPairList = [Pair_0002, Pair_0008, Pair_0014]
ERRFloatList = [Float_0003, Float_0009, Float_0015]
ERRExpected = [Matrix_0004, Matrix_0010, Matrix_0016]
ERRArgs = [ERRMatrixList, ERRPairList, ERRFloatList, ERRExpected]



# Matrix size = (6, 12)
array2D_0019 = [[  4.60000,  -7.22000,  -6.68000,  -0.29000,   3.10000,   8.51000,  -7.20000,   9.64000,  -0.96000,  -7.40000,  -7.10000,  -4.28000],
                [  4.93000,  -8.78000,  -3.25000,   5.33000,  -4.51000,  -7.64000,   7.58000,   9.61000,  -4.31000,   6.45000,  -2.70000,   9.70000],
                [  3.77000,  -4.84000,   1.44000,  -9.63000,  -0.18000,   6.32000,   1.01000,   6.85000,  -0.03000,  -0.53000,  -6.79000,  -7.12000],
                [ -2.34000,  -3.81000,  -3.90000,   5.15000,  -0.22000,  -6.22000, -10.00000,   5.80000,  -8.47000,   1.59000,   0.87000,   7.47000],
                [  2.58000,   5.32000,   5.93000,  -1.30000,   7.58000,  -7.22000,  -4.62000,  -2.31000,  -2.87000,  -5.23000,   2.04000,  -2.95000],
                [ -0.91000,  -5.01000,  -8.70000,   6.06000,   6.66000,  -4.72000,   2.16000,   2.80000,   4.83000,  -9.65000,   6.58000,   4.87000]]
Matrix_0018 = Matrix.fromArray(array2D_0019)
Pair_0020 = (4, 1)
array2D_0022 = [[  4.60000,  -7.22000,  -6.68000,  -0.29000,   3.10000,   8.51000,  -7.20000,   9.64000,  -0.96000,  -7.40000,  -7.10000,  -4.28000],
                [  2.58000,   5.32000,   5.93000,  -1.30000,   7.58000,  -7.22000,  -4.62000,  -2.31000,  -2.87000,  -5.23000,   2.04000,  -2.95000],
                [  3.77000,  -4.84000,   1.44000,  -9.63000,  -0.18000,   6.32000,   1.01000,   6.85000,  -0.03000,  -0.53000,  -6.79000,  -7.12000],
                [ -2.34000,  -3.81000,  -3.90000,   5.15000,  -0.22000,  -6.22000, -10.00000,   5.80000,  -8.47000,   1.59000,   0.87000,   7.47000],
                [  4.93000,  -8.78000,  -3.25000,   5.33000,  -4.51000,  -7.64000,   7.58000,   9.61000,  -4.31000,   6.45000,  -2.70000,   9.70000],
                [ -0.91000,  -5.01000,  -8.70000,   6.06000,   6.66000,  -4.72000,   2.16000,   2.80000,   4.83000,  -9.65000,   6.58000,   4.87000]]
Matrix_0021 = Matrix.fromArray(array2D_0022)
# Matrix size = (6, 10)
array2D_0024 = [[ -8.29000,   0.14000,  -8.86000,  -7.76000,  -8.78000,   0.05000,  -5.08000,   5.64000,  -9.24000,  -4.42000],
                [ -6.86000,   4.19000,   5.24000,  -8.16000,  -7.55000,   6.70000,  -0.36000,   1.34000,  -9.94000,   0.70000],
                [  4.79000,   0.64000,  -2.51000,   5.36000,  -1.88000,  -4.89000,   0.27000,  -4.22000,   5.06000,   6.55000],
                [ -2.03000,   6.17000,  -7.66000,  -8.13000,  -8.79000,   6.46000,  -2.65000,  -4.88000,   2.33000,   7.48000],
                [  2.61000,  -6.45000,   5.54000,   8.75000,  -4.53000,   6.62000,  -5.05000,  -5.60000,  -5.45000,   5.30000],
                [  3.69000,  -3.03000,  -0.39000,  -6.84000,   4.81000,  -6.37000, -10.00000,  -7.10000,   6.51000,   3.83000]]
Matrix_0023 = Matrix.fromArray(array2D_0024)
Pair_0025 = (4, 3)
array2D_0027 = [[ -8.29000,   0.14000,  -8.86000,  -7.76000,  -8.78000,   0.05000,  -5.08000,   5.64000,  -9.24000,  -4.42000],
                [ -6.86000,   4.19000,   5.24000,  -8.16000,  -7.55000,   6.70000,  -0.36000,   1.34000,  -9.94000,   0.70000],
                [  4.79000,   0.64000,  -2.51000,   5.36000,  -1.88000,  -4.89000,   0.27000,  -4.22000,   5.06000,   6.55000],
                [  2.61000,  -6.45000,   5.54000,   8.75000,  -4.53000,   6.62000,  -5.05000,  -5.60000,  -5.45000,   5.30000],
                [ -2.03000,   6.17000,  -7.66000,  -8.13000,  -8.79000,   6.46000,  -2.65000,  -4.88000,   2.33000,   7.48000],
                [  3.69000,  -3.03000,  -0.39000,  -6.84000,   4.81000,  -6.37000, -10.00000,  -7.10000,   6.51000,   3.83000]]
Matrix_0026 = Matrix.fromArray(array2D_0027)
# Matrix size = (14, 2)
array2D_0029 = [[-7.17000,  9.19000],
                [-1.05000,  2.70000],
                [ 4.90000,  8.26000],
                [ 0.32000,  7.02000],
                [-1.97000,  7.00000],
                [-8.03000, -8.52000],
                [ 2.47000,  6.04000],
                [ 6.67000, -0.15000],
                [ 3.32000, -3.00000],
                [ 3.91000, -1.51000],
                [ 4.17000, -8.72000],
                [ 8.88000, -1.92000],
                [ 5.71000, -8.99000],
                [ 8.93000, -4.67000]]
Matrix_0028 = Matrix.fromArray(array2D_0029)
Pair_0030 = (6, 1)
array2D_0032 = [[-7.17000,  9.19000],
                [ 2.47000,  6.04000],
                [ 4.90000,  8.26000],
                [ 0.32000,  7.02000],
                [-1.97000,  7.00000],
                [-8.03000, -8.52000],
                [-1.05000,  2.70000],
                [ 6.67000, -0.15000],
                [ 3.32000, -3.00000],
                [ 3.91000, -1.51000],
                [ 4.17000, -8.72000],
                [ 8.88000, -1.92000],
                [ 5.71000, -8.99000],
                [ 8.93000, -4.67000]]
Matrix_0031 = Matrix.fromArray(array2D_0032)

ERIMatrixList = [Matrix_0018, Matrix_0023, Matrix_0028]
ERIPairList = [Pair_0020, Pair_0025, Pair_0030]
ERIxpected = [Matrix_0021, Matrix_0026, Matrix_0031]
ERIArgs = [ERIMatrixList, ERIPairList, ERIxpected]



# Matrix size = (8, 7)
array2D_0034 = [[  8.33000,  -5.73000,   3.16000,   3.22000,   1.09000,   0.38000,   5.12000],
                [ -1.77000,  -4.05000,  -7.22000,   9.31000,   3.46000,  -1.20000,  -7.13000],
                [ -3.78000,  -8.52000,   1.91000,  -9.07000,  -9.82000,   3.78000,   8.58000],
                [  6.09000,   9.32000,   0.08000,   1.56000,  -2.96000,  -0.85000,  -4.42000],
                [  3.99000,   1.95000,   4.91000,  -7.70000,  -7.02000,  -5.91000,  -5.19000],
                [ -7.79000,  -5.11000,   7.10000,   0.31000,   0.82000,   2.07000,   6.18000],
                [ -4.25000,   5.95000,  -6.21000,  -3.32000,  -7.57000,   8.92000,   9.23000],
                [  5.57000,   6.46000,   6.24000,  -4.84000,  -6.69000,  -9.39000,   7.67000]]
Matrix_0033 = Matrix.fromArray(array2D_0034)
Int_0035 = 7
Float_0036 = -6.53000
array2D_0038 = [[  8.33000,  -5.73000,   3.16000,   3.22000,   1.09000,   0.38000,   5.12000],
                [ -1.77000,  -4.05000,  -7.22000,   9.31000,   3.46000,  -1.20000,  -7.13000],
                [ -3.78000,  -8.52000,   1.91000,  -9.07000,  -9.82000,   3.78000,   8.58000],
                [  6.09000,   9.32000,   0.08000,   1.56000,  -2.96000,  -0.85000,  -4.42000],
                [  3.99000,   1.95000,   4.91000,  -7.70000,  -7.02000,  -5.91000,  -5.19000],
                [ -7.79000,  -5.11000,   7.10000,   0.31000,   0.82000,   2.07000,   6.18000],
                [ -4.25000,   5.95000,  -6.21000,  -3.32000,  -7.57000,   8.92000,   9.23000],
                [-36.37210, -42.18380, -40.74720,  31.60520,  43.68570,  61.31670, -50.08510]]
Matrix_0037 = Matrix.fromArray(array2D_0038)
# Matrix size = (13, 9)
array2D_0040 = [[  9.25000,  -5.74000,  -7.89000,  -8.32000,   3.41000,   0.67000,   4.45000,  -2.34000,  -7.55000],
                [ -5.28000,  -2.56000,  -3.20000,   1.27000,  -1.03000,  -1.32000,  -8.69000,   0.85000,   7.14000],
                [ -8.92000,  -1.77000,   8.79000,  -5.94000,  -6.63000,  -1.13000,   8.43000,   1.89000,  -4.17000],
                [  3.19000,  -0.72000,  -8.52000,   7.77000,   1.49000,   0.15000,   4.31000,   1.93000,  -7.07000],
                [ -9.89000,   9.36000,   1.31000,   1.67000,   3.36000,   1.68000,   4.62000,   7.15000,   5.57000],
                [  1.88000,  -9.90000,   8.84000,  -8.37000,   0.63000,   8.33000,  -8.66000,  -6.08000,  -3.47000],
                [  7.94000,   6.44000,   3.19000,  -5.77000,   3.48000,   9.88000,  -5.08000,   3.68000,  -0.22000],
                [ -3.62000,  -4.50000,   5.68000,   0.05000,  -3.63000,   7.86000,   1.37000,  -6.35000,   9.12000],
                [  9.36000,   6.17000,  -7.23000,   3.24000,   2.41000,   5.11000,  -2.98000,   0.06000,   7.16000],
                [ -8.76000,   4.63000,  -9.27000,   2.48000,   3.70000,   3.88000,  -6.05000,   7.88000,   4.72000],
                [ -3.83000,  -3.59000,  -9.30000,   7.91000,   8.26000,   3.91000,   0.79000,  -0.59000,  -1.33000],
                [  6.03000,  -9.68000,  -9.67000,   4.32000,  -4.49000,  -2.41000, -10.00000,   6.70000,  -0.18000],
                [  9.80000,   2.97000,  -8.65000,   2.00000,   6.20000,   5.53000,  -3.25000,  -2.62000,   8.54000]]
Matrix_0039 = Matrix.fromArray(array2D_0040)
Int_0041 = 2
Float_0042 = -9.88000
array2D_0044 = [[  9.25000,  -5.74000,  -7.89000,  -8.32000,   3.41000,   0.67000,   4.45000,  -2.34000,  -7.55000],
                [ -5.28000,  -2.56000,  -3.20000,   1.27000,  -1.03000,  -1.32000,  -8.69000,   0.85000,   7.14000],
                [ 88.12960,  17.48760, -86.84520,  58.68720,  65.50440,  11.16440, -83.28840, -18.67320,  41.19960],
                [  3.19000,  -0.72000,  -8.52000,   7.77000,   1.49000,   0.15000,   4.31000,   1.93000,  -7.07000],
                [ -9.89000,   9.36000,   1.31000,   1.67000,   3.36000,   1.68000,   4.62000,   7.15000,   5.57000],
                [  1.88000,  -9.90000,   8.84000,  -8.37000,   0.63000,   8.33000,  -8.66000,  -6.08000,  -3.47000],
                [  7.94000,   6.44000,   3.19000,  -5.77000,   3.48000,   9.88000,  -5.08000,   3.68000,  -0.22000],
                [ -3.62000,  -4.50000,   5.68000,   0.05000,  -3.63000,   7.86000,   1.37000,  -6.35000,   9.12000],
                [  9.36000,   6.17000,  -7.23000,   3.24000,   2.41000,   5.11000,  -2.98000,   0.06000,   7.16000],
                [ -8.76000,   4.63000,  -9.27000,   2.48000,   3.70000,   3.88000,  -6.05000,   7.88000,   4.72000],
                [ -3.83000,  -3.59000,  -9.30000,   7.91000,   8.26000,   3.91000,   0.79000,  -0.59000,  -1.33000],
                [  6.03000,  -9.68000,  -9.67000,   4.32000,  -4.49000,  -2.41000, -10.00000,   6.70000,  -0.18000],
                [  9.80000,   2.97000,  -8.65000,   2.00000,   6.20000,   5.53000,  -3.25000,  -2.62000,   8.54000]]
Matrix_0043 = Matrix.fromArray(array2D_0044)
# Matrix size = (8, 10)
array2D_0046 = [[  6.85000,  -2.78000,  -7.08000,  -8.50000,  -0.72000,  -4.62000,  -6.73000,  -8.94000,  -9.81000,  -8.62000],
                [ -8.13000,   2.22000,  -8.77000,  -4.69000,  -7.75000,   2.07000,   4.77000,  -5.07000,   6.15000,  -2.56000],
                [ -7.10000,  -4.31000,  -9.16000,  -7.41000,  -3.17000,   7.78000,  -7.80000,   8.56000,   4.28000,   4.94000],
                [  8.40000,  -9.48000,   2.21000,   3.58000,  -9.09000,   3.88000,   1.93000,  -5.58000,  -9.10000,  -5.03000],
                [ -8.57000,   5.98000,  -5.34000,   6.34000,   0.49000,   3.11000,   5.95000,  -1.79000,  -3.39000,   1.18000],
                [ -6.02000,   7.36000,   9.76000,  -3.23000,   7.94000,  -1.59000,  -0.58000,   3.41000,   9.29000,   8.28000],
                [ -8.05000,   7.18000,  -8.88000,  -2.90000,  -6.34000,   4.44000,   3.95000,   2.71000,  -9.71000,   5.14000],
                [  6.21000,  -1.75000,   5.34000,   7.34000,   5.09000,   3.77000,  -7.10000,  -8.68000,  -4.72000,  -0.54000]]
Matrix_0045 = Matrix.fromArray(array2D_0046)
Int_0047 = 2
Float_0048 = 3.51000
array2D_0050 = [[  6.85000,  -2.78000,  -7.08000,  -8.50000,  -0.72000,  -4.62000,  -6.73000,  -8.94000,  -9.81000,  -8.62000],
                [ -8.13000,   2.22000,  -8.77000,  -4.69000,  -7.75000,   2.07000,   4.77000,  -5.07000,   6.15000,  -2.56000],
                [-24.92100, -15.12810, -32.15160, -26.00910, -11.12670,  27.30780, -27.37800,  30.04560,  15.02280,  17.33940],
                [  8.40000,  -9.48000,   2.21000,   3.58000,  -9.09000,   3.88000,   1.93000,  -5.58000,  -9.10000,  -5.03000],
                [ -8.57000,   5.98000,  -5.34000,   6.34000,   0.49000,   3.11000,   5.95000,  -1.79000,  -3.39000,   1.18000],
                [ -6.02000,   7.36000,   9.76000,  -3.23000,   7.94000,  -1.59000,  -0.58000,   3.41000,   9.29000,   8.28000],
                [ -8.05000,   7.18000,  -8.88000,  -2.90000,  -6.34000,   4.44000,   3.95000,   2.71000,  -9.71000,   5.14000],
                [  6.21000,  -1.75000,   5.34000,   7.34000,   5.09000,   3.77000,  -7.10000,  -8.68000,  -4.72000,  -0.54000]]
Matrix_0049 = Matrix.fromArray(array2D_0050)

ERSMatrixList = [Matrix_0033, Matrix_0039, Matrix_0045]
ERSIndexList = [Int_0035, Int_0041, Int_0047]
ERSFloatList = [Float_0036, Float_0042, Float_0048]
ERSExpected = [Matrix_0037, Matrix_0043, Matrix_0049]
ERSArgs = [ERSMatrixList, ERSIndexList, ERSFloatList, ERSExpected]



# Matrix size = (12, 2)
array2D_0052 = [[  9.16000,   1.42000],
                [  4.20000,  -0.36000],
                [ -4.04000,   5.77000],
                [ -3.73000,  -2.33000],
                [ -6.60000,  -5.86000],
                [ -2.67000,  -8.78000],
                [ -2.52000,  -7.64000],
                [  2.94000,  -7.37000],
                [  0.59000,  -9.42000],
                [ -3.87000,   3.19000],
                [  9.75000,   3.86000],
                [  6.35000,  -4.07000]]
Matrix_0051 = Matrix.fromArray(array2D_0052)
array2D_0054 = [[ 9.16000,  1.42000],
                [ 0.00000, -1.01109],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000],
                [ 0.00000,  0.00000]]
Matrix_0053 = Matrix.fromArray(array2D_0054)
# Matrix size = (10, 12)
array2D_0056 = [[ -3.17000,  -0.24000,   6.12000,   2.82000,  -3.94000,  -9.34000,   6.44000,  -6.54000,   3.01000,   8.47000,   8.89000,   3.22000],
                [  6.67000,   5.42000,   0.99000,  -4.59000,  -1.98000,   2.89000,   2.59000,   5.46000,   5.66000,   5.12000,   8.38000,  -6.03000],
                [  0.58000,   8.22000,   2.65000,   3.11000,  -2.07000,   1.51000,   1.67000,   3.72000,  -9.23000,   8.10000,  -7.53000,   0.20000],
                [ -2.50000,   2.95000,   6.70000,  -4.60000,   3.99000,  -0.14000,  -0.49000,  -4.37000,  -2.82000,   5.79000,  -0.12000,   8.13000],
                [  2.28000,   4.22000,  -7.49000,   8.71000,  -4.33000,  -9.10000,   3.95000,   1.25000,   1.63000,   8.84000,  -7.83000,  -0.93000],
                [ -0.85000,  -0.57000,   2.07000,   0.56000,  -3.32000,  -2.83000,   6.29000,   7.04000,  -4.24000,   4.19000,  -8.74000,   7.38000],
                [  4.32000,   7.88000,  -3.13000,   8.01000,   2.53000,   4.59000,   0.57000,   2.36000,   2.97000,   7.64000,   8.87000,   5.47000],
                [  3.35000,  -3.79000,  -5.39000,   1.26000,  -7.86000,  -9.02000,   2.18000,  -4.21000,   2.52000,  -3.10000,   9.16000,   1.59000],
                [  3.98000,  -3.74000,   8.04000,   9.93000,   6.66000,  -3.15000,   7.42000,  -3.35000,  -8.64000,  -2.51000,   2.74000,   9.87000],
                [ -8.78000,  -7.09000,   6.15000,   9.03000,  -9.74000,   3.42000,   5.54000,   8.81000,  -0.73000,  -0.02000,   0.87000,  -3.18000]]
Matrix_0055 = Matrix.fromArray(array2D_0056)
array2D_0058 = [[     -3.17000,      -0.24000,       6.12000,       2.82000,      -3.94000,      -9.34000,       6.44000,      -6.54000,       3.01000,       8.47000,       8.89000,       3.22000],
                [     -0.00000,       4.91502,      13.86710,       1.34356,     -10.27016,     -16.76230,      16.14041,      -8.30082,      11.99334,      22.94174,      27.08546,       0.74521],
                [      0.00000,       0.00000,     -19.29806,       1.39095,      14.29344,      27.68506,     -24.00114,      16.33175,     -28.63010,     -28.51367,     -50.95987,      -0.45049],
                [      0.00000,       0.00000,       0.00000,      -8.18548,       8.48442,       7.91355,      -7.19241,       0.17943,      -2.49346,      -5.22444,      -5.98950,       5.27762],
                [     -0.00000,       0.00000,      -0.00000,       0.00000,      -0.55200,     -14.52584,       5.78919,      -8.70761,      12.82602,      11.99517,       8.28655,       6.64697],
                [      0.00000,       0.00000,       0.00000,       0.00000,       0.00000,      49.81908,     -15.73277,      38.96528,     -49.97342,     -39.08485,     -41.32212,     -15.88460],
                [      0.00000,       0.00000,      -0.00000,       0.00000,       0.00000,       0.00000,      19.58110,      38.41408,     -18.71529,      15.26907,     -49.94806,      51.93745],
                [      0.00000,       0.00000,       0.00000,       0.00000,       0.00000,      -0.00000,       0.00000,      -0.00180,      -9.92817,      -0.47129,      -1.80505,      20.65479],
                [      0.00000,       0.00000,       0.00000,       0.00000,       0.00000,      -0.00000,      -0.00000,       0.00000, -125243.34104,   -5955.58544,  -22852.92237,  260437.02713],
                [     -0.00000,       0.00000,      -0.00000,       0.00000,       0.00000,      -0.00000,      -0.00000,       0.00000,       0.00000,       7.27844,       6.59962,      29.19721]]
Matrix_0057 = Matrix.fromArray(array2D_0058)
# Matrix size = (2, 3)
array2D_0060 = [[ 5.61000, -8.10000, -7.09000],
                [ 1.04000, -4.81000, -2.52000]]
Matrix_0059 = Matrix.fromArray(array2D_0060)
array2D_0062 = [[ 5.61000, -8.10000, -7.09000],
                [ 0.00000, -3.30840, -1.20563]]
Matrix_0061 = Matrix.fromArray(array2D_0062)

FRMatrixList = [Matrix_0051, Matrix_0055, Matrix_0059]
FRExpected = [Matrix_0053, Matrix_0057, Matrix_0061]
FRArgs = [FRMatrixList, FRExpected]



# Matrix size = (3, 3)
array2D_0064 = [[0.00000, 2.00000, 2.00000],
                [1.00000, 0.00000, 0.00000],
                [0.00000, 4.00000, 4.00000]]
Matrix_0063 = Matrix.fromArray(array2D_0064)
array2D_0066 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 2.00000, 2.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0065 = Matrix.fromArray(array2D_0066)
# Matrix size = (3, 3)
array2D_0068 = [[0.00000, 0.00000, 1.00000],
                [0.00000, 1.00000, 0.00000],
                [1.00000, 0.00000, 0.00000]]
Matrix_0067 = Matrix.fromArray(array2D_0068)
array2D_0070 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 1.00000, 0.00000],
                [0.00000, 0.00000, 1.00000]]
Matrix_0069 = Matrix.fromArray(array2D_0070)
# Matrix size = (3, 3)
array2D_0072 = [[5.00000, 5.00000, 0.00000],
                [1.00000, 1.00000, 0.00000],
                [0.00000, 1.00000, 0.00000]]
Matrix_0071 = Matrix.fromArray(array2D_0072)
array2D_0074 = [[5.00000, 5.00000, 0.00000],
                [0.00000, 1.00000, 0.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0073 = Matrix.fromArray(array2D_0074)
# Matrix size = (4, 5)
array2D_0076 = [[0.00000, 0.00000, 0.00000, 0.00000, 1.00000],
                [0.00000, 0.00000, 4.00000, 0.00000, 1.00000],
                [0.00000, 0.00000, 1.00000, 0.00000, 0.00000],
                [0.00000, 1.00000, 0.00000, 0.00000, 0.00000]]
Matrix_0075 = Matrix.fromArray(array2D_0076)
array2D_0078 = [[ 0.00000,  1.00000,  0.00000,  0.00000,  0.00000],
                [ 0.00000,  0.00000,  4.00000,  0.00000,  1.00000],
                [ 0.00000,  0.00000,  0.00000,  0.00000, -0.25000],
                [ 0.00000,  0.00000,  0.00000,  0.00000,  0.00000]]
Matrix_0077 = Matrix.fromArray(array2D_0078)
# Matrix size = (3, 3)
array2D_0080 = [[1.00000, 0.00000, 0.00000],
                [2.00000, 1.00000, 0.00000],
                [3.00000, 2.00000, 1.00000]]
Matrix_0079 = Matrix.fromArray(array2D_0080)
array2D_0082 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 1.00000, 0.00000],
                [0.00000, 0.00000, 1.00000]]
Matrix_0081 = Matrix.fromArray(array2D_0082)
# Matrix size = (3, 3)
array2D_0084 = [[1.00000, 0.00000, 0.00000],
                [2.00000, 1.00000, 0.00000],
                [3.00000, 2.00000, 0.00000]]
Matrix_0083 = Matrix.fromArray(array2D_0084)
array2D_0086 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 1.00000, 0.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0085 = Matrix.fromArray(array2D_0086)

EdgeFRMatrixList = [Matrix_0063, Matrix_0067, Matrix_0071, Matrix_0075, Matrix_0079, Matrix_0083]
EdgeFRExpected = [Matrix_0065, Matrix_0069, Matrix_0073, Matrix_0077, Matrix_0081, Matrix_0085]
FRMatrixList += EdgeFRMatrixList
FRExpected += EdgeFRExpected



# Matrix size = (4, 7)
array2D_0088 = [[ -5.56000,  -6.45000,   6.88000,   2.81000,  -1.04000,  -7.57000,  -2.23000],
                [  0.00000,  -1.53980,  11.78712,  13.24016,   4.77439,  -1.74585, -10.28703],
                [  0.00000,   0.00000,  32.30369,  44.08508,  15.29687,   3.90833, -35.11798],
                [  0.00000,   0.00000,   0.00000,  10.86867,   7.04881,  25.17883,  -5.42719]]
Matrix_0087 = Matrix.fromArray(array2D_0088)
array2D_0090 = [[ 1.00000,  0.00000, -0.00000, -0.00000,  0.78792,  1.34711,  0.47995],
                [-0.00000,  1.00000, -0.00000,  0.00000, -0.67439, -2.22158, -0.71824],
                [ 0.00000,  0.00000,  1.00000,  0.00000, -0.41154, -3.04055, -0.40566],
                [ 0.00000,  0.00000,  0.00000,  1.00000,  0.64854,  2.31664, -0.49934]]
Matrix_0089 = Matrix.fromArray(array2D_0090)
# Matrix size = (11, 12)
array2D_0092 = [[ -3.63000,  -4.93000,   9.93000,  -1.25000,   1.50000,  -6.75000,  -6.86000,  -8.24000,   8.80000,   3.61000,   8.57000,  -0.47000],
                [  0.00000,   8.86788, -24.55818,  -6.25242,   6.05091,  17.94091,  25.76758,  11.92394, -13.03333,  -7.68788, -18.46394,  -2.78515],
                [  0.00000,   0.00000,  39.66697,  19.40210, -11.81055, -25.32991, -49.98056,  -6.08610,  15.25682,   0.21567,  29.07500,  11.60887],
                [  0.00000,   0.00000,   0.00000,  10.85636,   0.07498,  -6.63765,   3.31849,  -2.88240,   8.56875,  -7.32611,  11.77395,  10.68765],
                [ -0.00000,   0.00000,   0.00000,   0.00000,  -4.75540,  -4.55427, -17.64567,  16.20756,  -6.65766,   0.17230,   1.16518,  -6.90793],
                [  0.00000,   0.00000,   0.00000,   0.00000,   0.00000, -18.92359, -47.71299,  27.20055, -12.86220,   2.14067,  12.92503,  -9.24998],
                [  0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,  -7.33309,  25.66235,   1.75964,  -7.47592,   4.51102, -14.40438],
                [ -0.00000,   0.00000,  -0.00000,   0.00000,   0.00000,   0.00000,   0.00000, -57.82829, -10.73190,  23.12163,  -5.43383,  32.88836],
                [ -0.00000,   0.00000,  -0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000, -19.97950,  -0.54645, -16.90268,  13.36667],
                [ -0.00000,   0.00000,  -0.00000,   0.00000,   0.00000,   0.00000,   0.00000,  -0.00000,   0.00000,  -9.25072,  -2.45942,  11.09687],
                [ -0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,  11.64528,  -1.37961]]
Matrix_0091 = Matrix.fromArray(array2D_0092)
array2D_0094 = [[ 1.00000,  0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  0.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.14359],
                [ 0.00000,  1.00000,  0.00000,  0.00000,  0.00000,  0.00000, -0.00000,  0.00000,  0.00000,  0.00000,  0.00000, -0.43569],
                [-0.00000,  0.00000,  1.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000, -0.18413],
                [ 0.00000,  0.00000, -0.00000,  1.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.60550],
                [ 0.00000, -0.00000, -0.00000, -0.00000,  1.00000, -0.00000,  0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  0.00765],
                [-0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  1.00000,  0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  0.02619],
                [-0.00000, -0.00000,  0.00000, -0.00000, -0.00000, -0.00000,  1.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.28363],
                [ 0.00000, -0.00000,  0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  1.00000, -0.00000, -0.00000, -0.00000, -0.92500],
                [ 0.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  1.00000, -0.00000, -0.00000, -0.53685],
                [ 0.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.00000, -0.00000,  0.00000, -0.00000,  1.00000, -0.00000, -1.16807],
                [-0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  1.00000, -0.11847]]
Matrix_0093 = Matrix.fromArray(array2D_0094)
# Matrix size = (3, 11)
array2D_0096 = [[  0.67000,   4.20000,   1.23000,   2.88000,   3.08000,   3.22000,  -4.23000,  -6.14000,   3.25000,  -0.42000,   1.06000],
                [  0.00000, -64.40881, -16.76851, -48.05090, -44.99179, -47.49642,  69.61194,  80.09149, -37.36955,  -0.30612, -12.40075],
                [  0.00000,   0.00000,   1.22660, -11.55405,  -4.74089,   4.01913,  11.91446, -14.75474,   6.11052, -12.90317,   3.28142]]
Matrix_0095 = Matrix.fromArray(array2D_0096)
array2D_0098 = [[  1.00000,   0.00000,   0.00000,   1.54168,   1.00587,  -0.48448,  -1.51804,   1.08241,   0.19841,   1.48729,  -0.17006],
                [ -0.00000,   1.00000,  -0.00000,   3.19837,   1.70478,  -0.11564,  -3.60962,   1.88819,  -0.71676,   2.74344,  -0.50395],
                [  0.00000,   0.00000,   1.00000,  -9.41957,  -3.86506,   3.27664,   9.71339, -12.02897,   4.98167, -10.51945,   2.67522]]
Matrix_0097 = Matrix.fromArray(array2D_0098)

BRMatrixList = [Matrix_0087, Matrix_0091, Matrix_0095]
BRExpected = [Matrix_0089, Matrix_0093, Matrix_0097]
BRArgs = [BRMatrixList, BRExpected]



# Matrix size = (3, 3)
array2D_0100 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 2.00000, 2.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0099 = Matrix.fromArray(array2D_0100)
array2D_0102 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 1.00000, 1.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0101 = Matrix.fromArray(array2D_0102)
# Matrix size = (3, 3)
array2D_0104 = [[5.00000, 5.00000, 0.00000],
                [0.00000, 1.00000, 0.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0103 = Matrix.fromArray(array2D_0104)
array2D_0106 = [[1.00000, 0.00000, 0.00000],
                [0.00000, 1.00000, 0.00000],
                [0.00000, 0.00000, 0.00000]]
Matrix_0105 = Matrix.fromArray(array2D_0106)
# Matrix size = (4, 5)
array2D_0108 = [[ 0.00000,  1.00000,  0.00000,  0.00000,  0.00000],
                [ 0.00000,  0.00000,  4.00000,  0.00000,  1.00000],
                [ 0.00000,  0.00000,  0.00000,  0.00000, -0.25000],
                [ 0.00000,  0.00000,  0.00000,  0.00000,  0.00000]]
Matrix_0107 = Matrix.fromArray(array2D_0108)
array2D_0110 = [[0.00000, 1.00000, 0.00000, 0.00000, 0.00000],
                [0.00000, 0.00000, 1.00000, 0.00000, 0.00000],
                [-0.00000, -0.00000, -0.00000, -0.00000, 1.00000],
                [0.00000, 0.00000, 0.00000, 0.00000, 0.00000]]
Matrix_0109 = Matrix.fromArray(array2D_0110)

EdgeBRMatrixList = [Matrix_0099, Matrix_0103, Matrix_0107]
EdgeBRExpected = [Matrix_0101, Matrix_0105, Matrix_0109]
BRMatrixList += EdgeBRMatrixList
BRExpected += EdgeBRExpected



# Matrix size = (6, 6)
array2D_0112 = [[  8.81000,   6.36000,  -8.37000,   7.35000,   1.18000,  -7.96000],
                [  5.56000,  -1.47000,   6.72000,  -6.84000,   2.87000,   7.86000],
                [ -1.37000,  -1.55000,  -2.63000,   2.07000,  -6.55000,   9.26000],
                [  5.08000,   3.88000,  -6.51000,  -7.98000,   3.85000,  -6.98000],
                [  8.39000,   1.63000,  -3.05000,   1.76000,  -7.66000,   1.57000],
                [  4.31000,  -9.57000,   4.40000,  -2.66000,   7.50000,  -9.45000]]
Matrix_0111 = Matrix.fromArray(array2D_0112)
# Vector size = 6
array1D_0114 = [-3.96000, -6.89000,  0.85000,  9.08000, -2.14000, -2.06000]
Vector_0113 = Vector.fromArray(array1D_0114)
array1D_0116 = [-0.64393, -0.17312, -0.80465, -0.85877, -0.41383, -0.36174]
Vector_0115 = Vector.fromArray(array1D_0116)
# Matrix size = (7, 7)
array2D_0118 = [[ -9.67000,   3.75000,  -9.32000,   8.76000,   0.74000,   7.97000,  -2.55000],
                [  0.87000,   3.66000,   0.37000,   8.58000,  -8.49000,  -2.71000,  -7.53000],
                [  2.32000,  -9.88000,  -9.94000,   2.34000,   0.28000,  -1.32000,  -4.64000],
                [ -5.85000,  -9.03000,  -0.57000,   6.28000,   1.02000,  -9.79000,   9.72000],
                [ -0.62000,  -3.02000,  -1.53000,  -1.16000,   0.20000,   3.86000,  -2.89000],
                [ -8.89000,  -2.19000,   4.30000,   9.49000,  -6.72000,  -2.30000,  -1.30000],
                [ -3.05000,   8.54000,   3.58000,  -6.28000,  -2.37000,  -4.96000,  -6.18000]]
Matrix_0117 = Matrix.fromArray(array2D_0118)
# Vector size = 7
array1D_0120 = [ -9.68000,  -3.16000,  -0.84000,  -6.31000,  -4.13000,   8.43000,   2.30000]
Vector_0119 = Vector.fromArray(array1D_0120)
array1D_0122 = [  5.31980,  -2.52997,  38.29761,  38.68688,  85.11712, -13.69442, -45.27229]
Vector_0121 = Vector.fromArray(array1D_0122)
# Matrix size = (6, 6)
array2D_0124 = [[-5.92000,  5.71000,  2.40000, -1.23000, -7.36000, -0.24000],
                [-8.05000,  0.74000,  5.00000,  2.89000, -0.41000,  0.73000],
                [ 9.58000, -7.80000,  7.19000,  1.12000,  8.64000, -0.42000],
                [-7.48000, -2.66000, -0.99000,  8.31000,  7.51000, -4.03000],
                [-4.26000,  9.79000,  7.75000, -1.06000, -5.96000, -2.81000],
                [ 3.48000, -0.73000,  6.49000, -7.44000,  1.89000,  2.07000]]
Matrix_0123 = Matrix.fromArray(array2D_0124)
# Vector size = 6
array1D_0126 = [  9.41000,  -1.11000,  -9.76000,  -9.48000,   2.39000,  -4.03000]
Vector_0125 = Vector.fromArray(array1D_0126)
array1D_0128 = [-0.18563, -1.51490, -0.08582, -0.37509, -2.23029, -1.21176]
Vector_0127 = Vector.fromArray(array1D_0128)

GEMatrixList = [Matrix_0111, Matrix_0117, Matrix_0123]
GEVectorList = [Vector_0113, Vector_0119, Vector_0125]
GEExpected = [Vector_0115, Vector_0121, Vector_0127]
GEArgs = [GEMatrixList, GEVectorList, GEExpected]


