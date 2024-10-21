#If we open the file with this way, we dont need to use close() funct.
# with open("newFile.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

#     file.seek(0)
#     print(file.tell())

#     content2 = file.read(10)
#     print(content2)



#For Updating..
#Only read
# with open("newFile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())


# with open("newFile.txt", "r+", encoding="utf-8") as file:
#     file.write("aaa ")
# 
#     #for reading..
#     file.seek(0)
#     print(file.read())



#Updating on end of the page.
# with open("newFile.txt", "a", encoding="utf-8") as file:
#     file.write("Veli Samet\n")



#Updating on beginning of the page.
# with open("newFile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Cenk Samet\n" + content

#     file.seek(0)
#     file.write(content)



#Updating middle of the page.
with open("newFile.txt", "r+", encoding="utf-8") as file:
    myList = file.readlines()
    myList.insert(1, "Hakan Samet\n")

    file.seek(0)
    # for i in myList:
    #     file.write(i)
    file.writelines(myList) #Makes same job with the for loop above


