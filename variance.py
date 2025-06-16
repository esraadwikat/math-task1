import numpy as np

input_str = input("Enter The Numbers: ")
numbers = [float(num) for num in input_str.split()]

# تحويل القائمة إلى مصفوفة numpy
arr = np.array(numbers)

# حساب التباين
variance = np.var(arr)

print(f"(variance): {variance}")
