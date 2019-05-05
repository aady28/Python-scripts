# sorting

list1 = [22,11,9,4,90]

for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if(list1[i]>list1[j]):
            temp = list1[i]
            list1[i]=list1[j]
            list1[j]= temp


print(list1)

list2 = ['22',11,'9',4.9,90]

for i in range(len(list2)-1):
    for j in range(i+1,len(list2)):
        if(int(list2[i])>int(list2[j])):
            temp = list2[i]
            list2[i]=list2[j]
            list2[j]= temp


print(list2)

list2.remove(4.9)
print(list2)

# to remove particular element from index
list2.pop(1)
print(list2)

x=list2.pop(1)
print(list2,x)

#to clear list elements
print(list1)
list1.clear()
print(list1)

x = "Name .123"
x.split(".")
print(x)


#_________________________________





