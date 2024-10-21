class Person:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        print("Person Created.")

    def who_am_i(self):
        print("I am a Person.")

    def __str__(self):
        return f"My name is {self.firstName} {self.lastName}. "
    
    def __len__(self):
        return len(self.firstName) + len(self.lastName)


class Student(Person): #Inheritance
    def __init__(self, fName, lName, number):
        #super().__init__(fName, lName)
        Person.__init__(self, fName, lName)

        self.StudentNumber = number

        print("Student Created.")
    
    #Override
    def who_am_i(self):
        print("I am a Student.")

    def __str__(self):
        return super().__str__() + f"I am a Student."
    
    
    def __del__(self):
        print("Student object has been deleted.")


class Teacher(Person): #Inheritance
    def __init__(self, fName, lName, branch):
        #super().__init__(fName, lName)
        Person.__init__(self, fName, lName)

        self.branch = branch

        print("Teacher Created.")
    
    #Override
    def who_am_i(self):
        print(f"I am a {self.branch} Teacher.")

    
    def __str__(self):
        return super().__str__() + f"I am a Teacher."
    
    def __del__(self):
        print("Teacher object has been deleted.")


t1 = Teacher("Ali", "Yilmaz", "Math")

t1.who_am_i()
print(len(t1))
print(t1)
