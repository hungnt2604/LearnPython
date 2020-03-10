aliens = 2
password = "ALIENS"
print("Nhanh lên! Nguời ngoài hành tinh đang tới đấy.")
print("Bạn cần bật mật khẩu phòng vệ toàn cầu, vì tuơng lai trái đất.")
print()
print("-------------------------------------------------------------------")
print("CHÀO MỪNG TỚI HỆ THỐNG PHÒNG VỆ TOÀN CẦU")
print("-------------------------------------------------------------------")
guess = input("Mời bạn nhập mật khẩu hệ thống: ").upper()
while guess != password:
    print()
    print("Mật khẩi sai.")
    print()
    aliens = aliens ** 2
    print("Có", aliens, "nguời ngoài hành tinh xâm chiếm trái đất. Hãy thử lại !")
    if aliens >7400000000:
        break
    print()
    print("TIP: Thứ đang tấn công chúng ta.")
    print()
    guess = input("Nhanh nào ! Hãy nhập mật khẩu: ").upper()
if aliens > 7400000000:
    print("Chúng ta đã thua rồi. Chúng quá đông so với loài nguời.")
else:
    print("Hoan hô chúng ta đã chiến thắng rồi.")