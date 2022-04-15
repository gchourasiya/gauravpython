def divide(x,y):
    try:
        result = x//y

    except ZeroDivisionError:
        print("ZeroDivisionError")

    else:
        print("result :",result)

    finally:
        print("In finally block")

divide(3,2)
divide(3,2)