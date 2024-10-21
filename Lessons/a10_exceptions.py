
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)

    except Exception as ex:
        print("Invalid input!", ex)

    # except (ZeroDivisionError, ValueError) as e:
    #     print("Invalid input!")
    #     print(e)

    else:
        break

    finally:
        print("Try except is finalled.")




#
def checkPasword(pswrd):
    import re

    if(len(pswrd) < 8):
        raise Exception("Pasword must be 7 character at least.")
    elif not re.search("[a-z]", pswrd):
        raise Exception("Pasword must have lower case.")
    elif not re.search("[A-Z]", pswrd):
        raise Exception("Pasword must have upper case.")
    elif not re.search("[0-9]", pswrd):
        raise Exception("Pasword must have number.")
    elif not re.search("[_@$]", pswrd):
        raise Exception("Pasword must have alpha numeric character.")
    elif re.search("\s", pswrd):
        raise Exception("Pasword have not space character.")

while True:
    try:
        pswrd = input("Pasword: ")
        checkPasword(pswrd)
    except Exception as e:
        print(e)
    else:
        print("Password is changed successfully.")
        break






#
class Person:
    def __init__(self, name , year):
        if(len(name) > 10):
            raise Exception("Too many caharacter in name area!")
        else:
            self.name = name
            self.year = year


try:
    p = Person("Aliiiiiiiiiiiiiii", 2005)
except Exception as e:
    print(e)
