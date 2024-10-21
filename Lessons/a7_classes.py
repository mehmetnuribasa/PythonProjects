class Circle:
    #Class attributes
    pi = 3.14

    #Constructor
    def __init__(self, radius = 1):
        #Object attributes
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * self.pi * self.radius
    
    def __str__(self):
        return f"Radius: {self.radius} Perimeter: {self.calculate_perimeter()}"
    


c1 = Circle()
c2 = Circle(5)

print(c1)
print(c2)