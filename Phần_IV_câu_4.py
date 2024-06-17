function GaussianElimination(A, b):
    # Khởi tạo A^(0) và b^(0)
    A0 = A
    b0 = b
    
    # Khởi tạo danh sách để lưu các ma trận biến đổi
    T_list = []
    
    # Số hàng và số cột
    m, n = dimensions(A0)
    
    for j from 0 to min(m, n) - 1:
        # Tìm hàng có phần tử trụ trong cột j bắt đầu từ hàng j
        pivot_row = j
        for i from j+1 to m - 1:
            if abs(A0[i, j]) > abs(A0[pivot_row, j]):
                pivot_row = i
        
        # Hoán đổi hàng nếu pivot_row không phải là hàng hiện tại
        if pivot_row != j:
            A0 = E(pivot_row, j) * A0
            b0 = E(pivot_row, j) * b0
            T_list.append(E(pivot_row, j))
        
        # Khử các phần tử dưới phần tử trụ
        for i from j + 1 to m - 1:
            if A0[i, j] != 0:
                multiplier = -A0[i, j] / A0[j, j]
                A0 = S(i, j, multiplier) * A0
                b0 = S(i, j, multiplier) * b0
                T_list.append(S(i, j, multiplier))
    
    # Chuẩn hóa các hàng để phần tử trụ bằng 1
    for i from 0 to min(m, n) - 1:
        if A0[i, i] != 1 and A0[i, i] != 0:
            multiplier = 1 / A0[i, i]
            A0 = M(i, multiplier) * A0
            b0 = M(i, multiplier) * b0
            T_list.append(M(i, multiplier))
    
    # Trả về dãy các ma trận biến đổi
    return T_list, A0, b0

# Định nghĩa các ma trận biến đổi cơ bản

function M(i, lambda):
    matrix = IdentityMatrix(m)
    matrix[i, i] = lambda
    return matrix

function E(i, j):
    matrix = IdentityMatrix(m)
    matrix[i, i] = 0
    matrix[j, j] = 0
    matrix[i, j] = 1
    matrix[j, i] = 1
    return matrix

function S(i, j, lambda):
    matrix = IdentityMatrix(m)
    matrix[i, j] = lambda
    return matrix
