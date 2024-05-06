n = int(input("nhập một số nguyên dương:"))

if n > 1:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(f"ko phải là sô nguyên tố")
            break
        i += 1
    else:
        print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không là số nguyên tố.")


    