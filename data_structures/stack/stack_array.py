class mystack:
    def __init__(self):
        self.data = []

    def length(self):      #length of the list
        return len(self.data)

    def is_full(self):      #check if the list is full or not
        if len(self.data) ==5:
            return True
        else:
            return False

    def push(self,element):
        if len(self.data) < 5:      # insert a new element
            self.data.append(element)
        else:
            return "overflow"

    def pop(self): # # remove the last element from a list
        if len(self.data) ==0:
            return "underflow"
        else:
            return self.data.pop()


a = mystack()
a.push(10)
a.push(23)
a.push(25)
a.push(27)
a.push(11)
print(a.length())
print(a.is_full())
print(a.push(45))           # we try to insert one more element in the list - the output will be overflow
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop()) # try to delete an element in a list without elements - the output will be underflow

