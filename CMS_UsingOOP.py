#BLL Start from here
class Customer:
    listCus=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""
    def addCustomer(self):
        Customer.listCus.append(self)
    def searchCustomer(self,id):
        for i in range(len(Customer.listCus)):
            if(id==Customer.listCus[i].id):
                self.id=Customer.listCus[i].id
                self.name=Customer.listCus[i].name
                self.address=Customer.listCus[i].address
                self.mob=Customer.listCus[i].mob
                return
        print("Id not found")
    def deleteCustomer(self,id):
        for i in range(len(Customer.listCus)):
            if(id==Customer.listCus[i].id):
                Customer.listCus.pop(i)
                print("Customer Deleted Sucessfully")
                return
        print("Id not found")
    def updateCustomer(self):
        for i in range(len(Customer.listCus)):
            if(self.id==Customer.listCus[i].id):
                Customer.listCus[i]=self
                print("Customer Modified Sucessfully")
                return
        print("Id not found")
    def showAllCustomer(self):
        for cus in Customer.listCus:
            print("Id", cus.id, "Name", cus.name, "Address", cus.address, "Mobile no", cus.mob)
    def sortingKey(self,cus):
        return cus.name
    def sortCustomer(self):
        Customer.listCus.sort(key=self.sortingKey)

#PLL Code Start from here
while(True):
    print("1.AddCustomer\n2.Search\n3.Delete\n4.Modify\n5.Show All Customer\n6.Sort Customer\n0.Exit")
    ch=input("Enter your choice")
    if(ch=="1"):
        cus=Customer()
        cus.id=int(input("Enter id"))
        cus.name = input("Enter Name")
        cus.address = input("Enter Address")
        cus.mob = input("Enter Mobile No")
        cus.addCustomer()
        print("Customer Added Sucessfully")
        #write code for addCustomer
    elif (ch == "2"):
        cus=Customer()
        id=int(input("Enter ID"))
        cus.searchCustomer(id)
        print("Id",cus.id,"Name",cus.name,"Address",cus.address,"Mobile no",cus.mob)


        # write code for SearchCustomer
    elif (ch == "3"):
        cus=Customer()
        id = int(input("Enter ID"))
        cus.deleteCustomer(id)

        # write code for DeleteCustomer
    elif (ch == "4"):
        cus=Customer()
        cus.id = int(input("Enter ID"))
        cus.name = input("Enter Name")
        cus.address = input("Enter Address")
        cus.mob = input("Enter Mobile No")

        cus.modifyCustomer()

        # write code for ModifyCustomer
    elif (ch == "5"):
       cus=Customer()
       cus.showAllCustomer()
    elif (ch == "6"):
       cus=Customer()
       cus.sortCustomer()
    elif (ch == "0"):
       break

#PL Code End here