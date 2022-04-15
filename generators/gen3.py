def square(x):
    for i in range(x):
        yield i*i

sqr = square(5)
# while True:
#     try:
#         print("Received on next() : ",next(sqr))
#     except StopIteration:
#         break

for i in sqr:
    print("\nValue coming" )
    print(i)

