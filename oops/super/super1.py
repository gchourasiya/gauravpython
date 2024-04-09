class MyParentClass(object):
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        super().__init__()

obj = SubClass()
