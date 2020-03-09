print("hello world")
print("I'm Jamie")


def plus_2_number(number1, number2):
    total = number2 + number1
    print(total)

plus_2_number(2, 4)

class Person:
    def __init__(self, name, age, gender, address, birth):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.birthday = birth

    def printAll(self):
        return self.name + " " + str(self.age) + " " + self.gender + " " + self.address + " "  + self.birthday


def print_person(person):
    print(person.printAll())


person = Person("Nguyen Thanh Hung", 36, "Male", "HCM", "03/12/2982")
print_person(person)

x = 1
y = "aaaa"


def noReturn():
    print("noReturn")


def haveReturn():
    return "result"


def print_log_on_console(error):
    print(error)


def check_login():
    return True


result = check_login()
if result == False:
    print_log_on_console("test login screen FAIL")
else:
    print_log_on_console("test login screen SUCCESS")


class MobileLog:
    def __init__(self, model, os, version):
        self.deviceModel = model
        self.systemOS = os
        self.osVersion = version

    def isAndroid(self):
        isAndroid = self.systemOS == "android"
        return isAndroid


log = MobileLog("SamSung Ạ50S", "IOS", "9.0")

if log.isAndroid():
    print("Your device is Android.")
else:
    print("Your device is IOS")

thislist = ["apple", "banana", "cherry"]
print(thislist)

rating_number = 3


def test_login_screen():
    print("tested")
