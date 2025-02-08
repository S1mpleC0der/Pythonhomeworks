import numpy as np

vector = np.arange(10, 50)
print("Vector:\n", vector)

matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix:\n", matrix_3x3)

identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_matrix)

random_3x3x3 = np.random.rand(3, 3, 3)
print("\n3x3x3 Random Array:\n", random_3x3x3)

random_10x10 = np.random.rand(10, 10)
min_value, max_value = random_10x10.min(), random_10x10.max()
print("\nMin and Max in 10x10 Array:", min_value, max_value)

random_vector = np.random.rand(30)
mean_value = random_vector.mean()
print("\nMean of Random Vector:", mean_value)

random_5x5 = np.random.rand(5, 5)
normalized_matrix = (random_5x5 - np.min(random_5x5)) / (np.max(random_5x5) - np.min(random_5x5))
print("\nNormalized 5x5 Matrix:\n", normalized_matrix)

matrix_A = np.random.rand(5, 3)
matrix_B = np.random.rand(3, 2)
product_AB = np.dot(matrix_A, matrix_B)
print("\nProduct of 5x3 and 3x2 Matrices:\n", product_AB)

matrix_X = np.random.rand(3, 3)
matrix_Y = np.random.rand(3, 3)
dot_product = np.dot(matrix_X, matrix_Y)
print("\nDot Product of Two 3x3 Matrices:\n", dot_product)

matrix_4x4 = np.random.rand(4, 4)
transpose_matrix = matrix_4x4.T
print("\nTranspose of 4x4 Matrix:\n", transpose_matrix)

matrix_3x3_det = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of 3x3 Matrix:", determinant)

matrix_A = np.random.rand(3, 4)
matrix_B = np.random.rand(4, 3)
matrix_product = np.dot(matrix_A, matrix_B)
print("\nMatrix Product of 3x4 and 4x3 Matrices:\n", matrix_product)

matrix_3x3 = np.random.rand(3, 3)
vector_3 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3)
print("\nMatrix-Vector Product:\n", matrix_vector_product)

A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("\nSolution to Ax = b:\n", x)

matrix_5x5 = np.random.rand(5, 5)
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)
print("\nRow-wise Sums:\n", row_sums)
print("\nColumn-wise Sums:\n", column_sums)
