n = int(input("nhập các số nguyên dương n:"))
tong = 0
while ( n != 0):
    du = n % 10 
    tong = tong + du
    n //= 10
print(f"tổng của các số nguyên dương là {tong}")

