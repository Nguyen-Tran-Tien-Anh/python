n = int(input("nhập sô nguyên n"))
m = int(input("nhập số nguyên m"))
a = n
b = m
# tìm ưcln
while a != b:
    if a > b:
       a -= b
    else:
        b -= a
print(f"ước chung lớn nhất của { n } và { m } là {a}")