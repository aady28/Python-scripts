import threading
locObject =threading.Condition()
def Tick():
    for i in range(10):
        locObject.acquire()
        print("Tick ",end="")
        locObject.notify()
        locObject.wait()
        locObject.release()
def Tock():
    for i in range(10):
        locObject.acquire()
        print("Tock ")
        locObject.notify()
        if(i!=9):
            locObject.wait()
        locObject.release()

th1=threading.Thread(target=Tick)
th2=threading.Thread(target=Tock)
th1.start()
th2.start()
