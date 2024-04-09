class Stack:
    def __init__(self):
        self.item = []

    def push(self,element):
        self.item.append(element)

    def pop(self):
        self.item.pop()

    def isEmpty(self):
        return self.item == []

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.item[-1]

    def getStack(self):
        return self.item


s = Stack()
string_ = "{[{()}][]}([])"
print(list(string_))
def isValid(String):
    for char in string_:
        # print(char)

        print("/******************************************************/")
        print("Peak -> " +s.peek())
        print("char -> " + char)
        print("/******************************************************/")
        print('\n')
        if char == "(" or char == "[" or char == "{":
            s.push(char)
        elif char ==")" and not s.isEmpty() and s.peek() == "(":
            s.pop()
        elif char =="]" and not s.isEmpty() and s.peek() == "[":
            s.pop()
        elif char =="}" and not s.isEmpty() and s.peek() == "{":
            s.pop()
        else:
            return False
    return s.isEmpty()


print(isValid(string_))