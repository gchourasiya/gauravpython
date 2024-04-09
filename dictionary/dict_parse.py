numNames={1:"One", 2: "Two", 3:"Three"}

for key,value in numNames.items():
    if key==1:
        if 'O' in value:
            print("{}:{}".format(key,'\''+str(value)+'\''))
