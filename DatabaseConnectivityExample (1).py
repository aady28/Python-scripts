import pymysql
con=pymysql.connect(host="localhost",user="root",password="cetpa@123",database="cms19thjan")
print("Sucess")
print(type(con))
myCursor=con.cursor()
strQuery="select * from Customer"
rowAffected=myCursor.execute(strQuery)
print("Total Record=",rowAffected)
# print(myCursor.fetchall())
# data=myCursor.fetchall()
# print(type(data))
# print(myCursor.description)
for row in myCursor.description:
    print(row[0],end="\t")
print()
for row in myCursor.fetchall():
    for cell in row:
        print(cell,end="\t")
    print()
    # print(row)
