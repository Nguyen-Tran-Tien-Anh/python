def menu():
    print("bấm số 1: để tìm điểm trung bình môn học của học sinh Nguyễn Văn A")
    print("bấm số 2: để in ra tên và giá tiền/ kg của các loại trái cây từ cherry tới melon")
    print("bấm số 3: để in ra 2 hàng Tuple nhập thành 1 hàng")
    print("bấm số 4: để tìm kiếm loại trái cây và giá tiền hoặc điều chỉnh")




def student():
    diem_trung_binh={"Nguyễn Văn A": {"Toán": 7.4,"Lý" : 6.5,"Hóa": 7.0}}
 #hàm tìm học sinh
    def tim_student(hoc_sinh):
        if hoc_sinh in diem_trung_binh :
            print(f"học sinh: {hoc_sinh}")
            for mon_hoc, diem_mon_hoc in diem_trung_binh[hoc_sinh].items():
                print(f"{mon_hoc}: {diem_mon_hoc}")
        else:
           print("không tìm thấy học sinh1")
#hàm cập nhật
    def cap_nhat(hoc_sinh, mon_hoc, diem_moi):
        if hoc_sinh in diem_trung_binh and mon_hoc in diem_trung_binh[hoc_sinh]:
            print(f"đã cập nhật điểm môn {mon_hoc} của học sinh {hoc_sinh} thành {diem_moi}")
        else:
            print("không tìm thấy học sinh2")

    # nhập dữ liệu
    hoc_sinh = input("nhập tên học sinh: ")
    tim_student(hoc_sinh)

    #cập nhật
    hoc_sinh = input("nhập Nguyễn Văn A để thay đổi điểm trung bình: ")
    mon_hoc = input("nhập môn Toán để thay đổi điểm: ")
    diem_moi = float(input("nhập 8 điểm để thay đổi: "))
    cap_nhat(hoc_sinh, mon_hoc, diem_moi)

def fruit():
    fruit_name=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    fruit_prices=(70,40,88,54,45,43,24)

    start_fruit=fruit_name.index("cherry")
    end_fruit=fruit_name.index("melon")

    for i in range(start_fruit,end_fruit+1):
        print(f"tên trái cây ", fruit_name[i], "\ngiá tiền/kg ", fruit_prices[i])

def Tuple():
    Tuple_1= ("apple", "banana", "cherry")
    Tuple_2= ("kiwi", "melon", "mango")
    print(Tuple_1 + Tuple_2)

def tim_trai_cay():
    fruit_name={"apple": 30000, "banana": 40000, "cherry": 500000, "orange": 10000, "kiwi":98000, "melon": 450000, "mango": 55000}

    def tim_trai_cay(trai_cay_can_tim):
        if trai_cay_can_tim in fruit_name:
            print(f"giá của{trai_cay_can_tim} là: {fruit_name[trai_cay_can_tim]} VND")
        else:
            print("không tìm  thấy trái cây ")

    def cap_nhat(trai_cay_can_cap_nhat, gia_moi):
        if trai_cay_can_cap_nhat in fruit_name:
            fruit_name[trai_cay_can_cap_nhat]=gia_moi
            print(f"đã cập nhật giá của {trai_cay_can_cap_nhat} là: {fruit_name[trai_cay_can_cap_nhat]}")
        else:
            print("không tìm thấy trái cây")

    def hien_thi_tat_ca():
        for trai_cay, gia in fruit_name.items():
            print(f"{trai_cay} giá {gia} VND")

    while True:
        print("nhập 1 để tìm giá tiên cảu loại trái cây")
        print("nhập 2 để cập nhật giá tiên cảu loại trái cây")
        print("nhập 3 để hiện tất cả trái cây")
        print("nhập 4 để kết thúc")
        choil=input("Mời nhập lựa chọn (1->4): ")
        if choil == "1":
            trai_cay_can_tim=input("nhập trái cây cần tìm: ")
            tim_trai_cay(trai_cay_can_tim)
        elif choil == "2":
            trai_cay_can_cap_nhat=input("nhập trái cây bạn muốn cập nhật")
            gia_moi = int(input("nhập giá mới: "))
            cap_nhat(trai_cay_can_cap_nhat, gia_moi)
        elif choil =="3":
            hien_thi_tat_ca()
        elif choil == "4":
            break 
        else:
            print("lựa chọn không hợp lệ ")

menu()
choil=input("mời nhập: ")
if choil == "1":
    student()
elif choil == "2":
    fruit()
elif choil == "3":
    Tuple()
elif choil == "4":
    tim_trai_cay()
else:
    exit()

