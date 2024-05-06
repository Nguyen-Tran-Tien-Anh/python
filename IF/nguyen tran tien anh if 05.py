a = float(input("nhập hệ số a"))
b = float(input("nhập hệ số b"))
c = float(input("nhập hệ số c"))
if a == 0 and b == 0: 
        print("đây ko phải là phương trình bậc 2")
if a !=0 and b != 0:
    delta = b**2 - 4*a*c 
    if delta < 0:
     print("phương trình vô nghiệm")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép: x1 = x2 = ", (-b / (2 * a)))
    else :
        x1 = (-b + (delta)) / (2 * a)
        x2 = (-b - (delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm là: x1 = {x1} và x2 = {x2}")

