#Print Fabonocci series :

#Approach 1
# n = int(input("Enter the limit for fabo series :  "))
# n1 = 0
# n2 = 1
#
# print(n1)
# print(n2)
#
# next = n1+n2
#
# while(next <=n) :
#
#     next = n1 + n2
#     if(next <=n):
#         print(next)
#     n1 = n2
#     n2 = next

#_________________________________________________________________

# Approach 2
n = int(input("Enter the limit for fabo series :  "))
n1 = 0
n2 = 1

print(n1)
print(n2)

next = n1+n2

while(True) :

    next = n1 + n2
    if(next > n):
        break
    print(next)
    n1 = n2
    n2 = next



# FOR Loop : Using Range function

#for i in range(10):
#    print(i)


#for i in range(-10,11):
#    print(i)

# Step defined as 2
#for i in range(-10,11,2):
#    print(i)

for i in range(11,-10,-1):
    print(i)
