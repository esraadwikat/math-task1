import numpy as np


vec1_str = input("Enter the element of first vector seperate by space: ")
vec1 = np.array([float(x) for x in vec1_str.split()])


vec2_str = input("Enter the element of second vector seperate by space: ")
vec2 = np.array([float(x) for x in vec2_str.split()])

# التحقق من أن المتجهين لهما نفس الطول
if vec1.shape != vec2.shape:
    print("❌ the tow vectors must be the same length !")
else:
    # حساب الضرب النقطي
    dot_product = np.dot(vec1, vec2)
    print(f" dot product = {dot_product}")
