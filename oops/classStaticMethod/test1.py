class Student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.nickname = None
    def set_nickname(self,name):        #Instance Methods as the first parameter is self.
        self.name = name

    @classmethod
    def get_from_string(cls,name_string:str):
        fname,lname = name_string.split()
        return Student(fname,lname)

    @classmethod
    def get_from_json(cls, json_obj):
        pass
        # return student

    @classmethod
    def get_from_excle(cls, excle_file):
        pass
        # return student

    @classmethod
    def get_from_audio_record(cls, audio):
        pass
        # return student

s = Student.get_from_string('Gaurav Chourasiya')
print(s.fname)      #Gaurav
print(s.lname)      #Chourasiya

# can't call instance method directly by class name
s2 = Student.set_nickname("Nick")   ## TypeError: set_nickname() missing 1 required positional argument: 'name'




