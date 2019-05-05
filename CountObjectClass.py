# class CountObject:
#     def __init__(self):
#         self.count=0
#         self.count+=1
#         print(self.count)

class CountObject:
    count=0
    def __init__(self):
        CountObject.count+=1
        print(CountObject.count)

ob1=CountObject()
ob2=CountObject()
ob3=CountObject()
ob1=CountObject()
