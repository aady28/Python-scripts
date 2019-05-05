class Customer:
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""

import json
intData=5
floatData=5.5
tupData=(1,3,[5,8,9],"abc2",3.5)
dictData={"key1":"Value1","Id":10,"Name":"Abc"}
print(type(dictData),dictData)
strJsonData=json.dumps(dictData)
print(type(strJsonData),strJsonData)
dictfromJson=json.loads(strJsonData)
print(type(dictfromJson),dictfromJson)
# print(strJsonData)