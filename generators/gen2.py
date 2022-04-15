def seq(x):
    for i in range(x):
        yield i

seq= seq(5)
# for _ in seq:
#     print(next(seq))

for val in seq:
    print(val)
