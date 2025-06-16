import numpy as np

vec1_str = input("Enter the element of first vector seperate by space: ")
vec1 = np.array([float(x) for x in vec1_str.split()])


vec2_str = input("Enter the element of second vector seperate by space: ")
vec2 = np.array([float(x) for x in vec2_str.split()])

# التحقق من أن المتجهين لهما نفس الطول
if vec1.shape != vec2.shape:
    print("❌  the tow vectors must be the same length !")
    exit()

# جمع المتجهين
sum_vec = vec1 + vec2

# طرح المتجهين
diff_vec = vec1 - vec2

# حساب الطول (magnitude)
magnitude_vec1 = np.linalg.norm(vec1)
magnitude_vec2 = np.linalg.norm(vec2)

# ضرب المتجه الأول في عدد ثابت
scalar = float(input("Enter the Scalar multiplication of fist vector : "))
scaled_vec = scalar * vec1


print("\n✅ Rwsults:")
print("AdditionVector=", sum_vec)
print("SubtractionVector=", diff_vec)
print("length of first vector=", magnitude_vec1)
print("length of second vector=", magnitude_vec2)
print(f"first vector × {scalar} =", scaled_vec)