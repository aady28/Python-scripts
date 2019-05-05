import threading
class MyThreadClass(threading.Thread):
    def run(self):
        for i in range (1000):
            print("Class",i)
            print(threading.active_count())
class MyThreadClass1(threading.Thread):
    def run(self):
        for i in range (1000):
            print("Class1",i)
            print(threading.active_count())


th1=MyThreadClass()
th2=MyThreadClass1()
th2.run()
th1.run()
for i in range(10):
    print("Main", i)
