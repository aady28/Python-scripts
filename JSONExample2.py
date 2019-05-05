import json
class Customer:
    def __init__(self,dictCus=None):
        if(dictCus==None):
            self.id=0
            self.name=""
            self.address=""
            self.mob=""
        else:
            for e in dictCus.items():
                self.__setattr__(e[0], e[1])


def cusIntoDict(cus):
    return cus.__dict__
def dictIntoCus(dictCus):
    cus=Customer()
    cus.id=dictCus["id"]
    cus.name=dictCus["name"]
    cus.address=dictCus["address"]
    cus.mob=dictCus["mob"]
    return cus

def dictIntoCusAuto(dictCus):
    cus=Customer()
    for e in dictCus.items():
        # cus.e[0]=e[1]
        # print(e)
        cus.__setattr__(e[0],e[1])

    return cus
cus=Customer()
cus.id=10
cus.name="abc10"
cus.address="noida 10"
cus.mob="100"
cusinDict=cusIntoDict(cus)
print(type(cusinDict),cusinDict)
cusinJson=json.dumps(cusinDict)
print(type(cusinJson),cusinJson)
cusinDictfromJson=json.loads(cusinJson)
cus=Customer(cusinDictfromJson)
print(cus.id,cus.name,cus.address,cus.mob)

# print(cusinDictfromJson.id)

#
