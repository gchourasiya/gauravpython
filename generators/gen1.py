def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

out = mygenerator()
for i in out:
    print("\nValue coming" )
    print(i)
