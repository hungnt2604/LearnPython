# How to user input ()
# print("Hãy tạo nhân vật!")
# name = input("Tên nhân vật")
# age = input("Tuổi nhân vật")
# strengths = input("Sức mạnh của nhân vật")
# weakness = input("Điểm yếu của nhân vật")
#
# print("Nhân vật của tôi tên là: ", name)
# print("Tuổi của nhân vật: ", age, "tuổi")
# print("Thế mạnh của nhân vật: ", strengths)
# print("Điểm yếu của nhân vật: ", weakness)
# print(name, "nói 'Xin chào Jamie'")

# age = input("Bạn bao nhiêu tuổi ?")
# ageNextYear = int(age) + 1
# print("Bạn sẽ đuợc", ageNextYear , "tuổi vào sinh nhật tới.")

# How to use If, Else, Elif
# user_reply = input("Bạn có thích Python không ? (Hãy điền có,không,có thể hoặc không biết là gì)")
# if user_reply == "có" or user_reply == "Yes":
#     print("Yes Yes!")
# elif user_reply == "không" or user_reply == "No":
#     print("Game Over")
# elif user_reply == "có thể" or user_reply == "Maybe":
#     print("Oops ! Câu trả lời thông minh đấy !")
# else:
#     print("Bạn sẽ thích khi cùng học với tôi !")


print("-=TRÒ CHƠi=-")
print("Tìm số may mắn của bạn.")
exit_Choice = "AAA"


def start_game():
    user_Choice = input("Hãy chọn một số bất kỳ từ 1 đến 4: ")
    if user_Choice == "1":
        print("Chúc bạn may mắn lần sau !")
    elif user_Choice == "2":
        print("Oops ! Bạn đã chọn trúng con số gần may mắn rồi đấy. Hảy thử lại nào !")
    elif user_Choice == "3":
        print("Bạn đã chọn gần đúng rồi. Hãy chọn thêm 1 số phụ nhé !")
        number_Choice = input("Điền 1 hoậc 2: ")
        if number_Choice == "1":
            print("Bạn chọn nhầm rồi. Hãy bắt đầu lại từ đầu nào !")
        elif number_Choice == "2":
            print("Chúc mừng ! Bạn đã rất may mắn đấy.")
        else:
            print("Xin lỗi bạn đã không chọn 1 hoặc 2.")
    else:
        print("Chúc bạn may mắn lần sau !")


while exit_Choice != "Thoát":
    start_game()
    exit_Choice = input("Nhấn ENTER để tiếp tục hoặc gõ Thoát để thoát ra khỏi trò chơi. ")
