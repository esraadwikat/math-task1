input_str = input("Enter the numbers separated by space: ")

numbers = [float(num.strip()) for num in input_str.split()]

# حساب المتوسط
mean = sum(numbers) / len(numbers)


print("The Mean is :", mean)