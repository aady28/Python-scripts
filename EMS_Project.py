class EMP:
    listEmp=[]
    @staticmethod
    def getTypebyId(id):
        for e in EMP.listEmp:
            if(e.id==id):
                return e.type

    @staticmethod
    def getObjectbyId(id):#for Runtime Polymorphism
        for e in EMP.listEmp:
            if (e.id == id):
                if(e.type=="Dir"):
                    return Dir()
                elif(e.type=="Mgr"):
                    return Mgr()
                elif(e.type=="TT"):
                    return TT()


    def __init__(self):
        self.id=0
        self.name=""
        self.type=""
    def __str__(self):
        return "Id: "+self.id+" Name: "+self.name
    def add(self):
        EMP.listEmp.append(self)
    def search(self,id):
        for e in EMP.listEmp:
            if(e.id==id):
                self.id=e.id
                self.type=e.type
                self.name=e.name
                return

class Dir(EMP):

    def __init__(self):
        self.share=0
        self.dirSpecial=""
        super().__init__()
    def __str__(self):
        return "Id: "+self.id+" Name: "+self.name+" Share: "+self.share+" dirSpecial: "+self.dirSpecial
    def add(self):
        super().add()
    def search(self,id):
        for e in EMP.listEmp:
            if(e.id==id):
                self.share=e.share
                self.dirSpecial=e.dirSpecial
                super().search(id)
                return
class Mgr(EMP):
    def __init__(self):
        self.incentive=0
        self.mgrSpecial=""
        super().__init__()
    def __str__(self):
        return "Id: "+self.id+" Name: "+self.name+" Incentive: "+self.incentive+" mgrSpecial: "+self.mgrSpecial
    def add(self):
        super().add()
    def search(self,id):
        for e in EMP.listEmp:
            if(e.id==id):
                self.incentive=e.incentive
                self.mgrSpecial=e.mgrSpecial
                super().search(id)
                return
class TT(EMP):
    pass
while(True):
    print("1.Add Emp\n2.Search Emp\n0.Exit")
    ch=int(input("Enter your choice"))
    if(ch==1):
        while(True):
            print("1.Add Dir\n2.Add Mgr\n3.Add TT\n0.Exit")
            ch1=input("Enter your choice")
            if(ch1=="1"):
                obDir=Dir()
                obDir.type="Dir"
                obDir.id=int(input("Enter ID"))
                obDir.Name = input("Enter Name")
                obDir.share = input("Enter Share")
                obDir.dirSpecial=input("Enter dirSpecial")
                obDir.add()
                print("Director Added Sucessfully")

            elif(ch1=="2"):
                obMgr = Mgr()
                obMgr.type = "Mgr"
                obMgr.id = int(input("Enter ID"))
                obMgr.Name = input("Enter Name")
                obMgr.incentive = input("Enter Incentive")
                obMgr.mgrSpecial = input("Enter mgrSpecial")
                obMgr.add()
                print("Manager Added Sucessfully")

            else:
                break


    elif(ch==2):
        id=int(input("Enter Id"))
        obj=EMP.getObjectbyId(id)
        obj.search(id)
        print(obj)
        # print("Id",obj.id,"Name:",obj.name)
        # if(obj.type=="Dir"):
        #     print("Share", obj.share, "dir Special:", obj.dirSpecial)
        # elif(obj.type=="Mgr"):
        #     print("Incentive", obj.incentive, "mgr Special:", obj.mgrSpecial)
    else:
        break

