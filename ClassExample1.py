class Class1:
    def __init__(self):
        self.x=0
        self.y=0
    def setData(self,x1,y1):
        self.x=x1
        self.y=y1
    def showData(self):
        print(self.x,self.y)

ob1=Class1()
ob2=Class1()
ob1.x=10
ob1.y=20
ob2.x=100
ob2.y=200
ob1.setData(40,60)
ob2.showData()
print(ob1.x)
