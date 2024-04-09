from unittest.mock import patch
import unittest

def cow():
    print("Cow")
    return {'cow':'moooo'}

def dog():
    print("Dog")
    return {'dog':'bhau bhau'}

def animals():
    data = cow()
    dogData = dog()
    data.update(dogData)
    data['pig']='khwen khwen'
    return data

def test_cow():
    assert cow() == {'cow':'moooo'}

def test_dog():
    assert dog() == {'dog':'bhau bhau'}

'''
@patch('__main__.cow')
@patch('__main__.dog')
def test_animals(patched_dog,patched_cow):
    data = animals()
    assert patched_dog.called is True
    assert patched_cow.called is True

'''


@patch('1.cow')
@patch('1.dog')

def test_animals(patched_dog, patched_cow):
    data = animals()
    assert patched_dog.called is True
    assert patched_cow.called is True

data= animals()
# print(data)
test_cow()
test_dog()
test_animals()

# if __name__ == '__main__':
#     unittest.main()