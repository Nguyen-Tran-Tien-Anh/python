n = int(input("nhập sô n mà bạn muốn nhân tới "))
s = 1
for i in range(2 , n + 1, 2):
  s *= i 
print(f"tích của các số chẵn = {s}")