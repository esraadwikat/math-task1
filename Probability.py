# المستخدم يدخل عدد الحالات الممكنة
favorable = int(input("Enter the number of possible outcomes (that satisfy the event): "))

# المستخدم يدخل عدد الحالات الكلية
total = int(input("Enter the All possible outcomes: "))

# التأكد من أن العدد الكلي أكبر من 0
if total == 0:
    print("❌ Division by zero is not allowed! Please enter a whole number greater than zero.")
elif favorable > total:
    print("❌ The number of favorable outcomes cannot be greater than the total number of outcomes.")
else:
    # حساب الاحتمال
    probability = favorable / total
    print(f"✅ Probability= {probability:.4f} or {probability * 100:.2f}%")