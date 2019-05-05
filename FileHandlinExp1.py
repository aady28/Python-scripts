import time
fs=open("pattern.py",'r')
print(fs.tell())
print("Sucess")
# data=fs.readlines(4)
# print(data)

while(True):
    data=fs.readline(5)
    if(data==""):
        break
    print(data,end="")
    time.sleep(.5)
    print(fs.tell())

print(fs.tell())
fs.see
# while(True):
#     data=fs.read(1)
#     if(data==""):
#         break
#     print(data,end="")
#     time.sleep(.1)
# print(type(fs))
# print(fs.readable())