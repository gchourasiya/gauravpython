dict1 = {3:'fizz',5:'buzz',7:'jazz',35:'fizzbuzz'}
out = ('fizzbuzz' if ((v%3==0 and v%5==0 and v%7!=0)) or 'fizz' if ((v%3 ==0 and v%5!=0 and v%7!=0)) or 'buzz' if ((v%3!=0 and v%5==0 and v%7!=0)) or ('jazz' if (v%7==0 and not v%3!=0 and not v%5!=0)) for k,v in dict1.items())
print(out)