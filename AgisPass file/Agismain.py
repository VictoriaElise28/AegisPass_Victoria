import random
import string

# Banner xịn xịn mang thương hiệu độc quyền Victoria
print("========================================")
print("  🛡️  AEGISPASS - PHIÊN BẢN VICTORIA 🛡️  ")
print("    Trình Tạo Mật Khẩu Siêu Cấp Độc Quyền ")
print("========================================")

# Nhận độ dài mật khẩu từ người dùng
do_dai = int(input("\n🙌 Nhập độ dài mật khẩu bạn muốn (tối thiểu 4): "))

# Kiểm tra điều kiện & xuất thông báo
if do_dai < 4:
    print("\n⚠️ LỖI RỒI: Ngắn quá má ơi! Trẻ con lớp 1 cũng đoán được! 🤡")
    print("Nhập lại độ dài >= 4 giúp mình nha.")
else:
    # Hiệu ứng "nấu" mật khẩu
    print("\n⏳ Đang 'nấu' mật khẩu siêu bảo mật cho bạn...")
    print("   + Thêm chút chữ thường...")
    print("   + Thêm vài CHỮ HOA...")
    print("   + Nêm thêm con số 123...")
    print("   + Cho tí gia vị ký tự đặc biệt @#$...")

    # Lấy kho ký tự
    chu_thuong = string.ascii_lowercase
    chu_hoa = string.ascii_uppercase
    chu_so = string.digits
    ky_tu_dac_biet = string.punctuation

    tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet

    # Bắt buộc mỗi nhóm ít nhất 1 ký tự
    mat_khau_list = [
        random.choice(chu_thuong),
        random.choice(chu_hoa),
        random.choice(chu_so),
        random.choice(ky_tu_dac_biet)
    ]

    # Bổ sung các ký tự còn lại
    for i in range(do_dai - 4):
        mat_khau_list.append(random.choice(tat_ca))

    # Xáo trộn vị trí ký tự
    random.shuffle(mat_khau_list)
    mat_khau = "".join(mat_khau_list)

    # Đánh giá độ mạnh hài hước
    if do_dai < 8:
        do_manh = "YẾU 😎 (Ai không biết công nghệ cũng hack được nha!)"
    elif do_dai <= 11:
        do_manh = "TRUNG BÌNH 🤣 (Đủ xài cho nick ảo Facebook, TikTok)"
    else:
        do_manh = "SIÊU MẠNH 😱 (Tới CIA cũng quỳ lạy bó tay!)"

    # In kết quả dạng bảng thông báo
    print("\n========================================")
    print("🎉 TẠO MẬT KHẨU THÀNH CÔNG:")
    print(f"🔑 Mật khẩu: {mat_khau}")
    print(f"💪 Độ mạnh:  {do_manh}")
    print("========================================")
    print("Cảm ơn bạn đã dùng phần mềm của Victoria! ✨\n")