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

@patch('2.dog')
@patch('2.cow')
def test_animals(patched_dog,patched_cow):
    data = animals()
    assert patched_cow.called is True
    assert patched_dog.called is True

test_animals()