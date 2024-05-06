n = int(input("nhập sô n mà bạn muốn nhân tới "))
s = 1
for i in range(s,n + 1, 2):
    s *= i
print(f"tích của các số lẻ ={s}")