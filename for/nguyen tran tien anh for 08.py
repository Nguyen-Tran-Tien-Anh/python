n = int(input("Nhập số nguyên dương n: "))  # Người dùng nhập số nguyên dương n
tong = 0

for i in str(n):
    tong += int(i)
    
print("Tổng các chữ số của n là", tong)
