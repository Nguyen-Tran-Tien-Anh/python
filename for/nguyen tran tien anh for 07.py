n = int(input(" nhập số n"))
lasonguyento = True 

if n <= 1:
    lasonguyento = False
else:
    for i in range(2, n ):
        if n % i == 0:
            lasonguyento = False
            break 
if lasonguyento:
    print(n,("là số nguyên tố"))
else:
    print(n,"không phải là số nguyên tố")

