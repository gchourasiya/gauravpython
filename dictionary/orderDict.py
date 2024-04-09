from collections import OrderedDict

orderDict = OrderedDict()

orderDict['p']=123
orderDict['q']=456
orderDict['r']=789

for key,value in orderDict.items():
    print("{}:{}".format(key,value))



#Python OrderedDict is a dict subclass that maintains the items insertion order. When we iterate over an OrderedDict, items are returned in the order they were inserted. A regular dictionary doesn't track the insertion order.
# So when iterating over it, items are returned in an arbitrary order.
# Ordinary dictionary may or may not keep the order of insertion


ordered_dict1=OrderedDict()
ordered_dict1['p']=123
ordered_dict1['q']=456
ordered_dict1['r']=789

ordered_dict2=OrderedDict()
ordered_dict2['r']=789
ordered_dict2['q']=456
ordered_dict2['p']=123

ordered_dict3=OrderedDict()
ordered_dict3['p']=123
ordered_dict3['q']=456
ordered_dict3['r']=789

print(ordered_dict1==ordered_dict2)
print(ordered_dict1==ordered_dict3)