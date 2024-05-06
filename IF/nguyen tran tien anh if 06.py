n = int(input("nhập năm"))
if(n % 4 == 0 and n % 100 !=0) or n % 400 == 0:
    print("năm là năm nhuận")
else:
    print("không phải là năm nhuận")