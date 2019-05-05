import pickle
class Customer:
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""
fs=open(r"c:\abc\abc1.txt","rb")
# cusinBytes=fs.read()
cus=pickle.load(fs)
print(type(cus))
print(cus.id,cus.name,cus.address,cus.mob)


# cus=Customer()
# cus.id=10
# cus.name="abc10"
# cus.address="Noida10"
# cus.mob="10"
#
# cusinBytes=pickle.dumps(cus)
# print(cusinBytes)
#
# #
# fs=open(r"c:\abc\abc1.txt","wb")
# fs.write(cusinBytes)
# fs.close()
#
#
#

# x=bytes(5)
# print(x)
# fs.write(bytes(5))
# fs.close()
# # while(True):
#     data=input("Enter String 0 for Exit")
#     if(data=="0"):
#         break
#     fs.write(data)
#     fs.flush()
#

#
# fs.close()