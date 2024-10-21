def my_decorator(funct):

    def wrapper(name):
        print("Operations before the function..")
        funct(name)
        print("Operations after the function..")

    return wrapper

# def sayHello(name):
#     print("Hello " + name)

# sayHello = my_decorator(sayHello)
# sayHello("Ali")

@my_decorator
def sayHello(name):
    print("Hello " + name)

sayHello("Ali")




