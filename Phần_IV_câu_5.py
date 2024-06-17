import numpy as np

# Định nghĩa các ma trận biến đổi cơ bản
def M(i, lambda_, size):
    matrix = np.eye(size)
    matrix[i, i] = lambda_
    return matrix

def E(i, j, size):
    matrix = np.eye(size)
    matrix[i, i] = 0
    matrix[j, j] = 0
    matrix[i, j] = 1
    matrix[j, i] = 1
    return matrix

def S(i, j, lambda_, size):
    matrix = np.eye(size)
    matrix[i, j] = lambda_
    return matrix

def GaussianElimination(A, b):
    A0 = A.copy()
    b0 = b.copy()
    T_list = []

    m, n = A0.shape
    
    for j in range(min(m, n)):
        pivot_row = j
        for i in range(j+1, m):
            if abs(A0[i, j]) > abs(A0[pivot_row, j]):
                pivot_row = i
        
        if pivot_row != j:
            A0 = E(pivot_row, j, m) @ A0
            b0 = E(pivot_row, j, m) @ b0
            T_list.append(E(pivot_row, j, m))
        
        for i in range(j + 1, m):
            if A0[i, j] != 0:
                multiplier = -A0[i, j] / A0[j, j]
                A0 = S(i, j, multiplier, m) @ A0
                b0 = S(i, j, multiplier, m) @ b0
                T_list.append(S(i, j, multiplier, m))
    
    for i in range(min(m, n)):
        if A0[i, i] != 1 and A0[i, i] != 0:
            multiplier = 1 / A0[i, i]
            A0 = M(i, multiplier, m) @ A0
            b0 = M(i, multiplier, m) @ b0
            T_list.append(M(i, multiplier, m))
    
    return T_list, A0, b0

# Hệ phương trình ban đầu
A = np.array([[2, 3, 1], [4, 6, 1], [1, 5, 1]], dtype=float)
b = np.array([11, 19, 14], dtype=float)

# Khử Gauss để tìm dãy các ma trận T^(k) và hệ trung gian
T_list, A_k, b_k = GaussianElimination(A, b)

# In kết quả
print("Dãy các ma trận T^(k):")
for i, T in enumerate(T_list):
    print(f"T^{i+1}:")
    print(T)

print("\nHệ phương trình sau khi khử Gauss (dạng bậc thang):")
print("A^(k):")
print(A_k)
print("b^(k):")
print(b_k)

# Giải hệ phương trình bậc thang
def back_substitution(A, b):
    m, n = A.shape
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i, j] * x[j]
        x[i] /= A[i, i]
    return x

# Giải hệ phương trình
x = back_substitution(A_k, b_k)
print("\nNghiệm của hệ phương trình là:")
print(x)
