import numpy as np

def read_matrix(name):
    rows = int(input(f"Enter the number rows of the matrix {name}: "))
    cols = int(input(f" Enter the number cols of the matrix {name}: "))
    
    print(f"\n Enter the Item {name}  row by row(seperate by space):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"row {i+1}: ").split()))
        while len(row) != cols:
            print("❌  the number of rows don't equal number of cols")
            row = list(map(float, input(f" row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

# قراءة المصفوفات من المستخدم
A = read_matrix("A")
B = read_matrix("B")

# العمليات
print("\n🧮 results\n")

# الجمع والطرح (فقط إذا نفس الأبعاد)
if A.shape == B.shape:
    print("1. A + B:\n", A + B)
    print("\n2. A - B:\n", A - B)
else:
    print("⚠️ can't add or  Subtraction Matrices with different dimensions.")

# ضرب بعدد ثابت
scalar = float(input("\Enter the Scalar multiplication of a matrix A : "))
print(f"\n3. {scalar} * A:\n", scalar * A)

# ضرب المصفوفات (إذا كان ممكنًا)
if A.shape[1] == B.shape[0]:
    print("\n4. A x B:\n", np.dot(A, B))
else:
    print("⚠️ can't A × B because the row of B ≠ th cols of A")

# Transpose
print("\n5. Transpose of A:\n", A.T)

# Determinant (إذا مربعة)
if A.shape[0] == A.shape[1]:
    det = np.linalg.det(A)
    print("\n6. Determinant of A:", det)
    
    # Inverse
    if det != 0:
        print("\n7. Inverse of A:\n", np.linalg.inv(A))
    else:
        print("\n7. can't calculate the Transpose because the Determinant |A|")
else:
    print("\n6. can't calculate Determination or transpos because A not squre")

# الرتبة
print("\n8. Matrix Rank A:", np.linalg.matrix_rank(A))