#For Writing..
file = open("newFile.txt", "w", encoding = "utf-8")    #utf-8  for using turkish characters.
file.write("Ali Samet\n")
file.close()


#For Appending..
file = open("newFile.txt", "a", encoding = "utf-8")
file.write("Osman Samet\n")
file.close()


#For only Create a file.. (if file is already exist, it gives error.)
# file = open("newFile2.txt", "x", encoding = "utf-8")
# file.close()



#For Reading..
try:
    file = open("newFile.txt", "r", encoding="utf-8")
    print(file)
except FileNotFoundError:
    print("File Open Error!")
finally:
    print("File is closing..")
    file.close()


file = open("newFile.txt", "r", encoding="utf-8")
#
#Read from file line by line.
# for i in file:
#     print(i, end="")

#Read funct..
# content = file.read()
# print(content)

# content = file.read(5)
# content = file.read(3)
# print(content)


#readline funct..
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")


#readlines funct..
myList = file.readlines()
print(myList)
print(myList[1])

file.close()
