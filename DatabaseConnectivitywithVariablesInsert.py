import pymysql
con=pymysql.connect(host="localhost",user="root",password="cetpa@123",database="cms19thjan")
print("Sucess")
print(type(con))
myCursor=con.cursor()
id=input("Enter Id")
name=input("Enter Name")
address=input("Enter Address")
mob=input("Enter Mobile no")

strQuery="insert into customer values(%s,%s,%s,%s)"
# strQuery="select * from Customer where id=%s and name=%s"
# strQuery="select * from Customer where id="+id+" and name='"+name+"'"
# strQuery="select * from customer where name like '%%%s%%'"
# print(myCursor.mogrify(strQuery))
# print(myCursor.mogrify(strQuery,(name,)))
rowAffected=myCursor.execute(strQuery,(id,name,address,mob))
con.commit()
strQuery="select * from Customer"
# print("Total Record=",rowAffected)
# print(myCursor.fetchall())
# data=myCursor.fetchall()
# print(type(data))
# print(myCursor.description)
myCursor.execute(strQuery)
for row in myCursor.description:
    print(row[0],end="\t")
print()
for row in myCursor.fetchall():
    for cell in row:
        print(cell,end="\t")
    print()
    # print(row)
