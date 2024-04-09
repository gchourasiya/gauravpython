import json

def readJSONData (isonFile):

    data={}

    with open(jsonFile, encoding="utf8") as data_file:

        data= json.Load(data_file)

    return data


def editJsonDataFile(path, dict):


    fullpath = path

    with open(fullpath, 'r') as file:

        json_data = json.load(file)
        for k, v in dict.items():

            json_data[k] = v


    with open(fullpath, 'w') as file:

        json.dump(json_data, file)

    return fullpath

cloudConfig= 0

data= readJSONData('configv2.json')

newJson = editJsonDataFile('sample.json',data)
print(newJson)
