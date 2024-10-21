
def checkParola(pswrd):
    turkish_characters = "şçğöüıİ"
    for i in pswrd:
        if i in turkish_characters:
            raise TypeError("Password has Turkish character!")
        
        else:
            pass
    print("Valid parola.")


password = input("Password: ")
try:
    checkParola(password)
except TypeError as err:
    print(err)


#
def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negative value!")

    result = 1
    # for i in range(1, x+1):
    #     result *= i

    for i in range(x, 1, -1):
        result *= i
    
    return result

for x in [5, 10, 15, -3, "10a"]:
    try:
        y = factorial(x)
    except Exception as err:
        print(err)
        continue

    print(y)

