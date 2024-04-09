def is_called():
    def is_returned():
        return ("Hello")
    return is_returned

out = is_called()
out1 = out()
print(out1)