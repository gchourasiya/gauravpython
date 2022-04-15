def make_pretty(func):
    def inner():
        print("I got declared")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

# out = make_pretty(ordinary)           #Line 7 OR Line 11. Both are same.
ordinary()
