t = int(input("nhập số tuổi"))
if t > 0 and t <= 2:
    print("là trẻ sơ sinh")
elif t > 2 and t <= 10:
    print("là nhi đồng")
elif t > 10 and t <= 17:
    print("là vị thành niên")
elif t > 17 and t <= 39:
    print("là thanh niên")
elif t > 39 and t <= 50:
    print("là trung niên")
elif t > 50 :
    print("là cao niên")
else:
    print("tuổi không hợp lệ")
