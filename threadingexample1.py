import threading
import time

def fun1():
    for i in range(6):
        x=input("Enter data for fun1")
        print("fun1",x)
    print("Fun1 Completed")
        # time.sleep(.001)
        # th2.join()
def fun2():
    for i in range(3):
        x = input("Enter data for fun2")
        print("fun2", x)
    print("Fun2 Completed")



th1=threading.Thread(target=fun1)
th2=threading.Thread(target=fun2)
th1.setDaemon(True)
th1.start()
th2.start()

print("Sucess")
for i in range(2):
    x=input("Enter for main")
    print("Main",x)
print("Main Completed")