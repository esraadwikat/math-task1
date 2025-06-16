  
x = 5  
y_true = 10  # ناتج صحيح (نريد أن تتعلم الشبكة أن 5 → 10)

# وزن ابتدائي عشوائي
w = 0.1

# معدل التعلم (learning rate)
lr = 0.01

# عدد التكرارات
for epoch in range(100):
    # --- Forward pass ---
    y_pred = w * x

    # --- حساب الخطأ (loss) ---
    error = y_pred - y_true
    loss = error ** 2

    # --- Backpropagation (التفاضل) ---
    # المشتقة بالنسبة للوزن = 2 * (y_pred - y_true) * x
    dloss_dw = 2 * error * x

    # --- تحديث الوزن ---
    w -= lr * dloss_dw

    # --- طباعة التقدم ---
    if epoch % 10 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.4f}, Weight = {w:.4f}")

# النتيجة النهائية
print("\n✅ Learning Finsh")
print(f" Final Weight {w:.4f}")
print(f"Model prediction at x = 5 : {w * x:.2f}")