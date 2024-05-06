def menu():
    print("MỜI BẠN LỰA CHỌN")
    print("bấm số 1: để tính điểm trung bình học sinh.")
    print("bấm số 2: để tính tổng số nguyên tố.")
    print("bấm số 3: để tìm số lớn nhất trong 3 số ngẫu nhiên")
    print("bấm số 4: để tính tổng từ 1 đến n")
    print("bấm số 5: để nhập số lượng  in ra dãy số Fibonacci" )
    print("bấm số 6: để kiểm tra phải sô nguyên tố không")
    print("bâm số 7: để tính giai thừa ")
    print("bấm số 8: để chuyển đổi số nguyên N sang hệ cơ số B (2 <= B <= 32) bất kỳ")
    print("bấm số 9: để giải phương trình bậc 2: ax2 + bx + c = 0.")
    print("bấm số 10:để tìm UCLN và BCNN của hai số nguyên dương a và b nhập từ bàn phím.")


def diemtrungbinh():
    diem = (Toan + Ly + Hoa + Van + Anh) / 5
    if diem < 5 :
        print(f"học lực yếu")
    elif diem <= 6.9 :
        print("học lực trung bình")
    elif diem <= 8.9 :
        print("học lực khá")
    elif diem <= 10 :
        print("học lực giỏi")
    else:
        print("điểm ko hợp lệ")
       
def so_nguyen_to(n):
    if n > 1000 or n < 0:
        print("số không hợp lệ ")
        exit() #kết thúc ko thực hiện vòng lặp nữa
    if n <= 1:
        return False # nếu n nhỏ hơn hoặc = 1 là false ko phải số nguyên tố sssssssssssssssssss
    if n <= 3:
        return True # 2 và 3 là số nguyên tố 
    if n % 2 == 0 or n % 3 == 0:
        return False # nếu chia hết cho 2 hoặc chia hết cho 3 là ko phải số nguyên tố
    i = 5
    while i * i <= n: #5 * 5 <= n
        if n % i == 0 or n % (i + 2) == 0:
            return False # nếu n chia hết 5 hoặc chia hết cho 7 là ko phải số nguyên tố
        i += 6 # i = i + 6 là i = 11 là số nguyên tố
    return True
def tong_so_nguyen_to():  
    sum = 0
    for i in range(2, n+1): # tính từ 2 đến n +1
        if so_nguyen_to(i):
            sum += i # sum = sum + i ( cộng vào tổng)
    print("tổng các số nguyên tố là: ",sum)


def giatrilon():
    print("Nhập 3 số ngẫu nhiên bất kì")
    num = [int(input("số thứ  " + str(i+1) + ": ")) for i in range(3)] # hoặc num = [int(input("Nhập số thứ {}: ".format(i + 1))) for i in range(3)]
    so_lon_nhat = max(num)
    print("số lớn nhất trong 3 số trên là: ", so_lon_nhat)

def sum(n):
    if n == 0:# ví dụ n =3 
        return 0
    else:
        return n + sum(n-1)# hàm để qui


def fibonacci():
    if n <= 0:
        return []
    elif n <= 1:
        return[0]
    elif n <= 2:
        return [0,1]
    else:
        tong=[0,1]
        while len(tong) < n:
            tong.append(tong[-1]+tong[-2])
        print(tong)


def kiem_tra_so_nguyen_to():
    i=2
    if n > 1:
        while i * i <= n:
            if n % i == 0:
                print(f"{n} không phải là số nguyên tố")
                break
            i += 1
        else:
            print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là sô nguyên tố")


def giai_thua_khong_qui():
    a=1
    for i in range(1,n+1):
        a *= i # a = a * i
    print(f"giai thừa của {n} là: ", a)

def giai_thua_dung_qui(n):
    if n == 0 :
        return 1
    else:
        return n * giai_thua_dung_qui(n-1)# hàm để qui

# def bài 8



def  giai_phuong_trinhbac2():
    a= float(input("nhập hệ số a"))
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

def ucln_bcnn():
    n=int(input("nhập số nguyên a: "))
    m=int(input("nhập số nguyên b: "))
    a = n
    b = m
    #tìm ucln 
    while a != b:
        if a > b :
            a -= b
        else:
            b -= a
    # tìm bcnn
    bcnn = (n * m) //  a
    print(f"ước chung lớn nhất của {n} và {m} là: ", a)
    print(f"Bội chung nhỏ nhất của {n} và {m} là: ", bcnn)     

menu()
chucnang = input("mời bạn nhập: ")
if chucnang == "1": 
    Toan=float(input("mời bạn nhập điểm môn toán: "))
    Ly=float(input("mời bạn nhập điểm môn Lý: "))
    Hoa=float(input("mời bạn nhập điểm môn Hoa: "))
    Van=float(input("mời bạn nhập điểm môn Văn: "))
    Anh=float(input("mời bạn nhập điểm môn Anh: "))
    diemtrungbinh()
elif chucnang == "2":
    n=int(input("nhập số nguyên dương trong phạm vi từ 0 - 1000:\nMời nhập: "))
    tong_so_nguyen_to()
elif chucnang == "3":
    giatrilon()
elif chucnang == "4":
    n=int(input("nhập số bạn muốn cộng từ 1 tới "))
    print(f"tổng từ 1 đến {n} là:", sum(n))
elif chucnang == "5":
    n = int(input("nhập số lượng số bạn muốn in ra: "))
    fibonacci()
elif chucnang =="6":
    n=int(input("nhập số nguyên dương"))
    kiem_tra_so_nguyen_to()
elif  chucnang == "7":
    while True :
        print("nhập 1: để tính giai thừa (hàm không để qui)")
        print("nhập 2: để tính giai thừa (hàm để qui)")
        print("nhập 3: để kết thúc")
        lua_chon = input("Nhap lua chon cua ban: ")
        if lua_chon == "1":
            n=int(input("nhập số nguyên: "))
            giai_thua_khong_qui() 
        elif lua_chon == "2":
            n=int(input("nhập số nguyên: "))
            print(giai_thua_dung_qui(n))
        else:
            exit()
# elif chucnang == "8"
            
elif chucnang == "9":
    giai_phuong_trinhbac2()
elif chucnang == "10":
    ucln_bcnn()

else:
    print("exit")

 