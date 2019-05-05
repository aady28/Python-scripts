import threading
import time

def fun1():
    for i in range(5):
        print("fun1",i)
        # time.sleep(.001)
        # th2.join()
def fun2():
    for i in range(5):
        print("fun2",i)

th1=threading.Thread(target=fun1)
th2=threading.Thread(target=fun2)
th1.start()
th2.start()

# fun1()
# fun2()
# while(th1.is_alive()):
#     pass
th1.join()
print(threading.active_count())
print("Sucess")
t=threading.current_thread()
print(t.is_alive(),t.getName())