txt = "hello, and welcome to my world."

print(txt.capitalize())         #Hello, and welcome to my world.
print(txt.casefold())           #hello, and welcome to my world.
print(txt.center(100))          #                                 hello, and welcome to my world.
print(txt.count('m'))           #2
print(txt.encode())             #b'hello, and welcome to my world.'
print(txt.endswith('world.'))   #True

txt = "H\te\tl\tl\to"
print(txt.expandtabs(2))        #H e l l o
print(txt.find('o'))            #8

txt = "  For \nonly {price:.2f} \ndollars!   "
print(txt.format(price=49))     #For
                                #only 49.00
                                #dollars!


print(txt.index('F'))           #2

print(txt.upper())              #FOR
                                #ONLY {PRICE:.2F}
                                #DOLLARS!

print(txt.lower())              #for
                                #only {price:.2f}
                                #dollars!


print(txt.swapcase())           #fOR
                                #ONLY {PRICE:.2F}
                                #DOLLARS!

print(txt.strip())              #For
                                #only {price:.2f}
                                #dollars!

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)                        #['Thank you for the music', 'Welcome to the jungle']



txt = "  For only {price:.2f} dollars!   "
print(txt.rstrip())             #  For only {price:.2f} dollars!
print(txt.lstrip())             #For only {price:.2f} dollars!

print(txt.replace('only','yes'))#  For yes {price:.2f} dollars!

print(txt.isalnum())            #False
print(txt.isalpha())            #
print(txt.isascii())            #

num = '10.0'
print(num.isdecimal())

txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

x = 'रतलाम'
y = x.isdecimal()
print(y)


