#Write a Python program to find all keys in the provided dictionary that have the given value.

students = {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}

out = list(key for key,value in students.items() if value==20)
print(out)