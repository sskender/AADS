import numpy as np

vector_a = np.array([1, 3, 5])
vector_b = np.array([[2], [4], [6]])

mat_mul = np.outer(vector_a, vector_b)
print(mat_mul)

vect_dot = np.dot(vector_a, vector_b)
print(vect_dot)

max_exp = np.power(mat_mul, 2)
print(max_exp)

sub_mat = max_exp[-2:, -2:]
print(sub_mat)
