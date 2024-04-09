weeks=['fri','mon','wed','tue','thu','sat']
# How to sort them based on week order

week_dict = {'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7}

#How to sort the dict based on key  #Below output means alphabetical order of days
out = [key for key,value in (sorted(week_dict.items(),key=lambda x:x[0]))]
print(out)


#How to sort the dict based on value
out = [key for key,value in (sorted(week_dict.items(),key= lambda x:x[1]))]
print(out)

