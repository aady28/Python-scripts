#BLL Start from here
import pymysql
class Customer:
    con = pymysql.connect(host="localhost", user="root", password="cetpa@123", database="cms19thjan")
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""
    def addCustomer(self):
        myCursor=Customer.con.cursor()
        strQuery="insert into customer values(%s,%s,%s,%s)"
        myCursor.execute(strQuery,(self.id,self.name,self.address,self.mob))
        Customer.con.commit()
    def searchCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer where id=%s"
        rowAffected=myCursor.execute(strQuery, (self.id,))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mob = row[3]
        else:
            raise Exception("Id not found")



    def deleteCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "delete from customer where id=%s"
        rowAffected=myCursor.execute(strQuery, (self.id,))
        if(rowAffected!=0):
            Customer.con.commit()
        else:
            raise Exception("Id not found")
    def updateCustomer(self):
        myCursor = Customer.con.cursor()
        strQuery = "update customer set name=%s,address=%s,mob=%s where id=%s"
        rowAffected=myCursor.execute(strQuery, ( self.name, self.address, self.mob,self.id))
        if (rowAffected != 0):
            Customer.con.commit()
        else:
            raise ("Id not found")


    def showAllCustomer(self):
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer"
        myCursor.execute(strQuery)

        for row in myCursor.fetchall():
            print("Id", row[0], "Name", row[1], "Address", row[2], "Mobile no", row[3])

#PLL Code Start from here
while(True):
    print("1.AddCustomer\n2.Search\n3.Delete\n4.Modify\n5.Show All Customer\n0.Exit")
    ch=input("Enter your choice")
    if(ch=="1"):
        try:
            cus=Customer()
            cus.id=int(input("Enter id"))
            cus.name = input("Enter Name")
            cus.address = input("Enter Address")
            cus.mob = input("Enter Mobile No")
            cus.addCustomer()
            print("Customer Added Sucessfully")
        except Exception as ex:
            print(ex)
        #write code for addCustomer
    elif (ch == "2"):
        try:
            cus=Customer()
            id=int(input("Enter ID"))
            cus.searchCustomer(id)
            print("Id",cus.id,"Name",cus.name,"Address",cus.address,"Mobile no",cus.mob)
        except Exception as ex:
            print(ex)


        # write code for SearchCustomer
    elif (ch == "3"):
        try:
            cus=Customer()
            id = int(input("Enter ID"))
            cus.deleteCustomer(id)
        except Exception as ex:
            print(ex)


        # write code for DeleteCustomer
    elif (ch == "4"):
        cus=Customer()
        cus.id = int(input("Enter ID"))
        cus.name = input("Enter Name")
        cus.address = input("Enter Address")
        cus.mob = input("Enter Mobile No")

        cus.updateCustomer()

        # write code for ModifyCustomer
    elif (ch == "5"):
       cus=Customer()
       cus.showAllCustomer()

    elif (ch == "0"):
       break

#PL Code End here