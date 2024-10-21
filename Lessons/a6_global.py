name = 'Ali'

def ChangeName(newName):
    #name = 'Ali'     #local
    global name
    name = newName
    print(name)

ChangeName("Veli")
print(name)