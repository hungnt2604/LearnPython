import random
number = random.randint(1,20)
guess = int(input("Bạn hãy đoán một con số từ 1 đến 20. Con số bạn chọn là: "))
while guess != number:
    if guess < number:
        print("Bạn đã chọn con số nhỏ hơn đáp án rồi.")
    else:
        print("Bạn đã chọn con số lớn hơn đáp án rồi.")
    guess = int(input("Bạn hãy đoán lại nhé: "))
print("Chúc mừng bạn đã đoán trúng rồi.")
