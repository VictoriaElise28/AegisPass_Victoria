import random
import string

print("========================================")
print("  🛡️  AEGISPASS - PHIÊN BẢN VICTORIA 🛡️  ")
print("    Trình Tạo Mật Khẩu Siêu Cấp Độc Quyền ")
print("========================================")
print("1. Tạo mật khẩu mới")
print("2. Kiểm tra độ mạnh mật khẩu của bạn")
print("========================================")

lua_chon = input("\n👉 Nhập lựa chọn của bạn (1 hoặc 2): ")

if lua_chon == "1":
    
    do_dai = int(input("\n😍 Nhập độ dài mật khẩu bạn muốn (tối thiểu 4): "))

    if do_dai < 4:
        print("\n⚠️ LỖI RỒI: Ngắn quá 🤣! Trẻ con lớp 1 cũng đoán được! 🤡")
        print("Nhập lại độ dài >= 4 giúp mình nha😘.")
    else:
        print("\n⏳ Đang tạo mật khẩu siêu bảo mật cho bạn...")
        print("   + Thêm chút chữ thường...")
        print("   + Thêm vài CHỮ HOA...")
        print("   + Nêm thêm con số 123...")
        print("   + Cho tí gia vị ký tự đặc biệt @#$...")

        chu_thuong = string.ascii_lowercase
        chu_hoa = string.ascii_uppercase
        chu_so = string.digits
        ky_tu_dac_biet = string.punctuation

        tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet

        mat_khau_list = [
            random.choice(chu_thuong),
            random.choice(chu_hoa),
            random.choice(chu_so),
            random.choice(ky_tu_dac_biet)
        ]

        for i in range(do_dai - 4):
            mat_khau_list.append(random.choice(tat_ca))

        random.shuffle(mat_khau_list)
        mat_khau = "".join(mat_khau_list)

        if do_dai < 8:
            do_manh = "YẾU 😎 (Ai không biết công nghệ cũng hack được nha!)"
        elif do_dai <= 11:
            do_manh = "TRUNG BÌNH 🤣 (Đủ xài cho nick ảo Facebook, TikTok)"
        else:
            do_manh = "SIÊU MẠNH 😱 (Tới CIA cũng quỳ lạy bó tay!)"

        print("\n========================================")
        print("🎉 TẠO MẬT KHẨU THÀNH CÔNG:")
        print(f"🔑 Mật khẩu: {mat_khau}")
        print(f"💪 Độ mạnh:  {do_manh}")
        print("========================================")
        print("Cảm ơn bạn đã dùng phần mềm của Victoria! ✨\n")

elif lua_chon == "2":
    
    mk_khach = input("\n🔍 Nhập mật khẩu bạn muốn kiểm tra: ")

    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_db = False

    
    for ky_tu in mk_khach:
        if ky_tu in string.ascii_lowercase:
            co_chu_thuong = True
        elif ky_tu in string.ascii_uppercase:
            co_chu_hoa = True
        elif ky_tu in string.digits:
            co_so = True
        elif ky_tu in string.punctuation:
            co_ky_tu_db = True

    
    diem = 0
    if co_chu_thuong: diem += 1
    if co_chu_hoa: diem += 1
    if co_so: diem += 1
    if co_ky_tu_db: diem += 1

    print("\n⏳ Đang kiểm tra mật khẩu...")

    
    if len(mk_khach) < 8 or diem <= 2:
        do_manh = "YẾU 😎 (Ai không biết công nghệ cũng hack được nha!)"
    elif len(mk_khach) <= 11 or diem == 3:
        do_manh = "TRUNG BÌNH 🤣 (Đủ xài cho nick ảo Facebook, TikTok)"
    else:
        do_manh = "SIÊU MẠNH 😱 (Tới CIA cũng quỳ lạy bó tay!)"

    print("\n========================================")
    print("🎉 KẾT QUẢ KIỂM TRA MẬT KHẨU:")
    print(f"🔑 Mật khẩu: {mk_khach}")
    print(f"💪 Độ mạnh:  {do_manh}")
    print("========================================")
    print("Cảm ơn bạn đã dùng phần mềm của Victoria! ✨\n")

else:
    print("\n⚠️ Nhập sai rồi! Chỉ gõ 1 hoặc 2 thôi nha😘.")