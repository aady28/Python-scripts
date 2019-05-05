import threading
count=0
locObject=threading.Condition()
def fun1():
    global count
    for i in range(1000000):
        locObject.acquire()
        count+=1
        locObject.release()
    print("Fun1 Total",count)

def fun2():
    global count
    for i in range(1000000):
        locObject.acquire()
        count += 1
        locObject.release()
    print("Fun2 Total", count)
th1=threading.Thread(target=fun1)
th2=threading.Thread(target=fun2)
th1.start()
th2.start()
th1.join()
th2.join()
print("Main Total", count)
