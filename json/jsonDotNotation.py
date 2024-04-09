import json
import sys

json_file = r'products.json'
# match_dict={}
with open(json_file,'r') as jsonData:
    json_data = json.load(jsonData)
    # strObj = json.dumps(json_data)
    # print(strObj)
    # for i in strObj:
    #     print(i)

    '''
    for i in json_data:
        # print(type(i))
        # print(i)
        for key,value in i.items():
            # print("{}:{}".format(key,value))
            if isinstance(value,dict):
                print(value)
                for i in value:
                    if isinstance(i,dict):
                        print(True)
                    else:
                        print(False)
    '''
    for i in json_data:
        print(any(isinstance(j, dict) for j in i.values()))

# def getKeys(val, old=""):
#     if isinstance(val, dict):
#         if val:
#           for k in val.keys():
#             getKeys(val[k], old + "." + str(k))
#         else:
#           print("{} : {}".format(old,"{}"))
#     elif isinstance(val, list):
#         if val:
#           for i,k in enumerate(val):
#             getKeys(k, old + "." + str(i))
#         else:
#           print("{} : []".format(old,"{}"))
#     else:
#         print("{} : {}".format(old,str(val)))
# with open(json_file) as jsonFile:
#     data=json.load(jsonFile)
#     getKeys(data)