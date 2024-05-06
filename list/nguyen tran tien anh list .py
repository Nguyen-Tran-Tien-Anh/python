def tinh_tong():
    s= 0
    sochan = 2
    while s  < 50:
      s += sochan
      sochan += 2
    print(f"tổng các số chẵn là:{ s }")


def tam_giac():
 n  = 4
 for i in range(n):
    print(' ' *(n - i - 1) + '*' *(2 * i + 1))
 #' ' *(n - i - 1) là dòng dùng để tăng dấu  ' '
 #'*' *(2 * i + 1) là dòng dùng để tăng dấu '*'
    

def diem_hocsinh():
 # tạo danh sách hs và điểm
 hoten = ["Nguyễn Văn A", "Nguyễn Văn B", "Nguyễn văn C"]
 Toan = [7.4, 6.5, 7.0]
 Ly  = [6.5, 7.0, 7.4]
 Hoa  = [7.0, 7.4, 6.5]
 # nhập tên học sinh
 hovaten = input("nhập họ và tên học sinh: ")
 
 # tìm thông tin học sinh
 if hovaten in hoten:
    vitri = hoten.index(hovaten) # index là hàm tiềm kiếm vị trí đầu tiên của một phần tử trong danh sách
    print("họ và tên học sinh: ", hoten[vitri])
    print("Diem Toan: ", Toan[vitri])
    print("Diem Ly: ", Ly[vitri])
    print("Diem Hoa: ", Hoa[vitri])
 else:
    print ("không tìm thấy học sinh")
    
def trai_cay():
  # Tạo danh sách tên và giá tiền/kg của các loại trái cây
 traicay = ["apple", "banana", "jackfruit","cherry", "butter", "Orange", "mango","lemon","melon", "guava", "mango"]
 gia = [20.000,25.000,30.000,20.000,15.000,40.000,50.000,30.000,55.000,76.000,43.000,90.000]

 # tìm vị trí cherry và melon 
 batdau = traicay.index("cherry")
 ketthuc = traicay.index("melon")

 #in ra kết quả
 for i in range(batdau, ketthuc + 1):
    print("tên trái cây: ", traicay[i])
    print("giá tiền/kg: ", gia[i])

def check_hoc_sinh():
   # tạo danh sách hs và điểm
 hoten = ["Nguyễn Văn A", "Nguyễn Văn B", "Nguyễn văn C"]
 Toan = [7.4, 6.5, 7.0]
 Ly   = [6.5, 7.0, 7.4]
 Hoa  = [7.0, 7.4, 6.5]
 # kiểm tra tên học sinh có tồn tại ko
 check = input(" check tên học sinh cso tồn tại traong danh sách không: ")
 if check in hoten:
    print("học sinh", check , " có tồn tại")
 # nhập tên học sinh
 hovaten = input("nhập họ và tên học sinh: ")

 #  tìm thông tin học sinh
 if hovaten in hoten:
    vitri = hoten.index(hovaten) # index là hàm tiềm kiếm vị trí đầu tiên của một phần tử trong danh sách
    print("họ và tên học sinh: ", hoten[vitri])
    print("Diem Toan: ", Toan[vitri])
    print("Diem Ly: ", Ly[vitri])
    print("Diem Hoa: ", Hoa[vitri])
 else:
    print ("không tìm thấy học sinh")


def chen_va_bo_traicay():
   # Tạo danh sách tên và giá tiền/kg của các loại trái cây
 traicay = ["apple", "banana", "jackfruit","cherry", "butter", "Orange","kiwi", "mango","lemon","melon", "guava", "mango"]
 gia = [20.000,25.000,30.000,20.000,15.000,40.000,50.000,30.000,55.000,60.00,76.000,90.000,]
 # bỏ thành phần cuối của trái cay và giá
 traicay.pop()
 gia.pop()
 # chèn thêm 2 trái trước trái kiwi
 vitritraikiwi = traicay.index("kiwi")
 traicay.insert(vitritraikiwi, "papaya")
 gia.insert(vitritraikiwi, 14.000)
 traicay.insert(vitritraikiwi, "coconut")
 gia.insert(vitritraikiwi, 7.000)
 # tìm vị trí cherry và melon 
 batdau = traicay.index("cherry")
 ketthuc = traicay.index("melon")


def luu_du_lieu_hoc_sinh():
  # Tạo danh sách lưu trữ thông tin sinh viên
 sinh_vien = []

 while True:
    print("1. Nhap thong tin sinh vien")
    print("2. Tim kiem thong tin sinh vien")
    print("3. Thoat")
    lua_chon = int(input("Nhap lua chon cua ban: "))

    if lua_chon == 1:
        # Nhập thông tin sinh viên
        mssv = input("Nhap MSSV: ")
        ho_ten = input("Nhap ho va ten: ")
        ngay_sinh = input("Nhap ngay thang nam sinh: ")
        lop = input("Nhap ten lop: ")
        diem_tk = [float(input("Nhap diem thuong ky " + str(i+1) + ": ")) for i in range(3)]
        diem_gk = float(input("Nhap diem thi giua ky: "))
        diem_ck = float(input("Nhap diem thi cuoi ky: "))
        diem_tb = (sum(diem_tk)+ diem_gk + diem_ck ) / 3
        ket_qua = "Dau" if diem_tb >= 5 else "Rot"
        # Lưu thông tin sinh viên vào danh sách
        sinh_vien.append([mssv, ho_ten, ngay_sinh, lop, diem_tk, diem_gk, diem_ck, diem_tb, ket_qua])
    elif lua_chon == 2:
        # Tìm kiếm thông tin sinh viên
        tu_khoa = input("Nhap MSSV, ten hoac lop can tim: ")
        for sv in sinh_vien:
            if tu_khoa in sv:
                print("MSSV: ", sv[0])
                print("Ho va ten: ", sv[1])
                print("Ngay sinh: ", sv[2])
                print("Lop: ", sv[3])
                print("Diem thuong ky: ", sv[4])
                print("Diem giua ky: ", sv[5])
                print("Diem cuoi ky: ", sv[6])
                print("Diem trung binh: ", sv[7])
                print("Ket qua: ", sv[8])
    elif lua_chon == 3:
        break


