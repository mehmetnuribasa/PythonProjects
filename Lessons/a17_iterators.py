myList = [1,2,3,4,5]

iterator = iter(myList) #Create an iterator object.

while True:
    try:
        element = next(iterator)    #gets the next element.
        print(element)
    except StopIteration:
        break




#
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
mylist = MyNumbers(3, 10)

#For loop uses/calls the iterator automatically.
# for x in mylist:
#     print(x)


myIter = iter(mylist)
while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break

