import copy
'''
##Approach#1
student = {'Jim': 12, 'Anna': 14, 'Preet': 10}

def test(student):
    student = {'Sam':20, 'Steve':21}
    print("Inside the function", student)
    return

test(student)
print(student)
'''

##Approach#2

student = [1,2,3,4]
student2 = student[:]
def test(student2):
    print("Inside the function")
    student2.append(5)
    print(student2)
    return

test(student2)
print(student)
