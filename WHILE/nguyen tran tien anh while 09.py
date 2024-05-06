
n = int(input("nhập một số nguyên n"))

i = 2
while i <= n:
    if n % i:
        i +=1      
    else:
        n //= i
        print(i," ", end="")
if n > 1 :
    print(n)