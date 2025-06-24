# طلب العنوان من المستخدم
listTitle = input("Enter The Title Of The List : ")

# إنشاء قائمة فارغة
list = []

print("Enter the item (enter End if you finish):")

# إدخال العناصر من المستخدم
while True:
    item = input("- ")
    if item.strip().lower() == "end":
        break
    list.append(item)

# طباعة العنوان والعناصر المرقمة
print(f"\n{listTitle}")
print("-" * len(list))

for i, item in enumerate( list , start=1):
    print(f"{i}. {item}")