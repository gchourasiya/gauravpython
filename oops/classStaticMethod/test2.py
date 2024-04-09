class Student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.nickname = None
    def set_nickname(self,name):        #Instance Methods as the first parameter is self.
        self.name = name
        print("In Student class : ",self.name)

    @classmethod
    def get_from_string(cls,name_string:str):
        fname,lname = name_string.split()
        return Student(fname,lname)

    @staticmethod
    def suitable_age(age):
        return 6 <= age <= 30


class Junior(Student):
    def __init__(self,fname,lname):
        super(Junior,self).__init__(fname,lname)
        # self.nickname = None

    def set_nickname(self,name:str):
        self.nickname = name
        self.nickname = self.nickname.upper()
        print("In Junior class : ",self.nickname)
        super(Junior,self).set_nickname(name)



obj = Junior("Junior","Student")
print(obj.suitable_age(10))         #Call from child class instance/object.
obj.set_nickname("tinku")

print(Junior.suitable_age(30))  #Call from child class

