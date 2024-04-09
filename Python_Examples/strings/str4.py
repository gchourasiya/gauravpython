import io
fruits = 'apples$banana$mango$fig$pear'
# print(fruits.split('$ba'))


# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print(fruits, file=dummy_file)

# get the value from dummy file
out = dummy_file.getvalue()
print(out)