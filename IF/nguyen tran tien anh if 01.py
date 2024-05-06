a = int(input("nhập số nguyên a:"))
b = int(input("nhập số nguyên b:"))
c = int(input("nhập số nguyên c:"))
if a > b and a > c:
    print("số lớn nhất là ", a)
elif b > a and b > c:
    print("số lớn nhất là:", b)
else :
    print("số lớn nhất là ", c)