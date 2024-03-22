a = int(input("Nhập vào số nguyên dương a: "))
count = sum(1 for i in range(1, a + 1) if a % i == 0)
print("Số ước của", a, "là : ", count)

