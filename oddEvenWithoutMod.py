# def isEven(n):
#     isEven = True
#     for i in range(1,n+1):
#         if isEven ==True:
#             isEven = False
#         else:
#             isEven = True
#     return isEven
#
# n = 100
# print(isEven(n))



n =1010

def checkifEven(n):
    if n//2*2 ==n:
        return True
    else:
        return False

print(checkifEven(n))