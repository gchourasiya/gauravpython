students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}

def getMinMax(d):
  return max(d,key=d.get),min(d,key=d.get)

print(getMinMax(students))

