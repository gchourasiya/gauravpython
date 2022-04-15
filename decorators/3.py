def is_called():
    def is_returned():
        print("Hello")
    return is_returned

out = is_called()
out()