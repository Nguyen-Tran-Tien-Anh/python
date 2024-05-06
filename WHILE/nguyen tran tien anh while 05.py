n = int(input("nhập số nguyên n:"))
m = int(input("nhập số nguyên m:"))
songuyen1 = n # 4
songuyen2 = m# 2
# tìm uscln
while songuyen1 != songuyen2:
    if songuyen1 > songuyen2:
       songuyen1 -= songuyen2 # n = 4 - 2 ( n = 2)
    else:
       songuyen2 -= songuyen1  # 2

# Tính BSCNN
bcnn = (n * m) // songuyen1 # // chia lấy nguyên
print(f"bội chung nhỏ nhất của {n} và {m} là {bcnn}")
print(songuyen1)