def divide(x,y):
    try:
        result = x//y
        print(("TRY BLOCK"))
    except ZeroDivisionError:
        print("\nEXCEPT BLOCK")
        print("Zero division error")
    else:
        print("\nELSE BLOCK")
        print("Result is :",result)


divide(3,2)
divide(3,0)
