n = int(input("Nhập số N: "))
if isinstance(n, int):
    print(f"{n} là số nguyên")
else:
    print(f"{n} không phải số nguyên")
if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")
if n % 2 == 0 and n > 0:
    print(f"{n} là số chẵn dương")
else:
    print(f"{n} không phải số chẵn dương")
if n % 2 != 0 and n < 0:
    print(f"{n} là số lẻ âm")
else:
    print(f"{n} không phải số lẻ âm")
can_bac_hai = int(n ** 0.5)
if can_bac_hai ** 2 == n:
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải số chính phương")