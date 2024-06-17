def intersectTwoLines (a1 , b1 , c1 , a2 , b2 , c2): 
    # ... 
    return x0 , y0
def LPMax2Var(alpha, beta, constraints):
    vertices = []
    n = len(constraints)
    
    # Tìm tất cả các giao điểm của các đường thẳng từ các ràng buộc
    for i in range(n):
        for j in range(i + 1, n):
            a1, b1, c1 = constraints[i]
            a2, b2, c2 = constraints[j]
            
            # Tìm giao điểm của hai đường thẳng
            intersection = intersectTwoLines(a1, b1, c1, a2, b2, c2)
            if intersection is None:
                continue
            
            x, y = intersection
            
            # Kiểm tra xem giao điểm có thỏa mãn tất cả các ràng buộc không
            is_feasible = True
            for k in range(n):
                a, b, c = constraints[k]
                if a * x + b * y > c:
                    is_feasible = False
                    break
            
            # Nếu giao điểm thỏa mãn tất cả các ràng buộc, thêm vào danh sách vertices
            if is_feasible:
                vertices.append((x, y))
    
    # Bước 2: Tính giá trị lớn nhất của hàm mục tiêu
    optimalVal = float('-inf')
    
    # Tính giá trị hàm mục tiêu tại mỗi đỉnh
    for (x, y) in vertices:
        T = alpha * x + beta * y
        if T > optimalVal:
            optimalVal = T
    
    # Trả về giá trị của hàm mục tiêu
    return optimalVal
