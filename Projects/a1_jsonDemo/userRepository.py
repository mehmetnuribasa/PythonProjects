import json
import os

class User:
  
    def __init__(self, name, password, mail):
        self.userName = name
        self.password = password
        self.email = mail


class UserRepository:

    def __init__(self):
        self.userKnowledge = [] #Holds the user objects as a list.
        self.isLoggedIn = False
        self.currentUser = {}   # {}  indicates that this is object.

        #Load the users from json file.
        self.loadFromFile()


    def loadFromFile(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding = "utf-8") as file:
                tempUserList = json.load(file)  #Actually temUserList is json dictionary list.

                for temp in tempUserList:
                    newUser = json.loads(temp) #Convert the json dict. information(temp) to a python dict. object(newUser)
                    newUserObject = User(name = newUser["userName"], password = newUser["password"], mail = newUser["email"])

                    self.userKnowledge.append(newUserObject)    #Appends the new user object to the user knowledge list.



    def register(self, user: User):
        self.userKnowledge.append(user)
        self.saveToFile()
        print("User is created.")


    def login(self, name, password):
        for temp in self.userKnowledge:
            if (temp.userName == name and temp.password == password):
                self.isLoggedIn = True
                self.currentUser = temp
                print("Login is successfull.")
                break
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Logged out.")
    
    def identity(self):
        if self.isLoggedIn:
            print(f"User name: {self.currentUser.userName}, Email: {self.currentUser.email}")
        else:
            print("Was not logged in.")

    


    def saveToFile(self):

        userList = []   #Holds the knowledge converted to json(disctionary object).

        for temp in self.userKnowledge:
            userList.append(json.dumps(temp.__dict__))

        #Writes the userList to the json file.
        with open("users.json", "w", encoding = "utf-8") as file:
            json.dump(userList, file)



repository = UserRepository()
#Menü
while True:
    print("Menü".center(50, '*'))
    choice = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\n")

    if choice == '5':
        break
    else:
        if choice == '1':
            userName = input("Name: ")
            userPassword = input("Password: ")
            userEmail = input("Email: ")

            newUser = User(name=userName, password=userPassword, mail=userEmail)
            repository.register(newUser)

        elif choice == '2':
            userName = input("Name: ")
            userPassword = input("Password: ")

            repository.login(name=userName, password= userPassword)

        elif choice == '3':
            repository.logout()

        elif choice == '4':
            repository.identity()

        else:
            print("Invalid Input!")
