#BL Code Start from here
listId=[]
listName=[]
listAddress=[]
listMob=[]

def addCustomer(id,name,address,mob):
    listId.append(id)
    listName.append(name)
    listAddress.append(address)
    listMob.append(mob)

def searchCustomer(id):
    for i in range(len(listId)):
        if(id==listId[i]):
            print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])
            return
    print("Id Not found")

def deleteCustomer(id):
    for i in range(len(listId)):
        if(id==listId[i]):
            listId.pop(i)
            listName.pop(i)
            listAddress.pop(i)
            listMob.pop(i)
            print("Customer deleted sucessfully")
            return
    print("Id Not found")

def modifyCustomer(id,name,address,mob):
    for i in range(len(listId)):
        if(id==listId[i]):

            listName[i]=name
            listAddress[i]=address
            listMob[i]=mob
            print("Customer modified sucessfully")
            return
    print("Id Not found")

#BL Code End here

#PLL Code Start from here
while(True):
    print("1.AddCustomer\n2.Search\n3.Delete\n4.Modify\n0.Exit")
    ch=input("Enter your choice")
    if(ch=="1"):
        id=int(input("Enter id"))
        name = input("Enter Name")
        address = input("Enter Address")
        mob = input("Enter Mobile No")
        addCustomer(id,name,address,mob)
        print("Customer Added Sucessfully")
        #write code for addCustomer
    elif (ch == "2"):
        id=int(input("Enter ID"))
        searchCustomer(id)

        # write code for SearchCustomer
    elif (ch == "3"):
        id = int(input("Enter ID"))
        deleteCustomer(id)

        # write code for DeleteCustomer
    elif (ch == "4"):
        id = int(input("Enter ID"))
        name = input("Enter Name")
        address = input("Enter Address")
        mob = input("Enter Mobile No")

        modifyCustomer(id,name,address,mob)

        # write code for ModifyCustomer
    elif (ch == "0"):
       break

#PL Code End here