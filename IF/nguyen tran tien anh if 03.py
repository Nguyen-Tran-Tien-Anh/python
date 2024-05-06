n = int(input("nhập số nguyên"))
print(n)
if n % 2 != 0:
    print("Số lẻ")
elif n >= 100:
    print("Số chẵn và lớn hơn hoặc bằng 100")
elif n < 100:
    print("Số chẵn và bé hơn 100")
else:
     print("Vui lòng nhập một số nguyên hợp lệ.")
