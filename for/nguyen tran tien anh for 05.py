n = int(input("nhập số giai thừa của n"))
tong = 1
for i in range(1,n+1):
    tong *= i

print(f"giai thừa của {n} là = ", tong)