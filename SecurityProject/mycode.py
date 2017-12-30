import threading
import time
import thread


def fun1(count):
    print "fun1"
    condition.acquire()
    while True:
        if(count>10):
            condition.notify()
        count+=1
        print count
        time.sleep(1)
    condition.release()

def fun2(count):
    print "fun2"
    condition.acquire()
    while True:
        if count>10:
            print "cms"
        condition.wait()
        print "releasd"
    condition.release()

condition = threading.Condition()

count = 0

thread.start_new_thread(fun1,(count,))
thread.start_new_thread(fun2,(count,))

while True:
    pass
