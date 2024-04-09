from  unittest.mock import patch

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

@patch('3.dog')
@patch('3.cow')
def test_animals(patched_dog,patched_cow):

    # patched_dog.return_value = {'c','m'}
    # patched_cow.return_value = {'d','b'}
    data = animals()
    assert patched_dog.called is True
    assert patched_cow.called is True
    print(data)

test_animals()