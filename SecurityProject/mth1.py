import threading
import time
import thread


def producer():
    global count
    print "producer"
    condition.acquire()
    while True:
        if(count >5):
            condition.notify()
        count+=1
        print count
        time.sleep(1)
def consumer():
    global count
    print "consumer"
    condition.acquire()
    while True:
        
        print "released"
        print count,"count"
        time.sleep(1)
        
        count+=1
    condition.release()


'''def producer(count1,count2):
    print "producer"
    condition1.acquire()
    condition2.acquire()
    while True:
        print "producer",count1
        if(count1>10):
            condition1.notify()
            count2=0
            condition2.wait()
                
        count1+=1
        time.sleep(1)
    condition1.release()
    condition2.release()
def consumer(count1,count2):
    print "consumer"
    condition1.acquire()
    condition2.acquire()
    while True:
        if(count1<10):
            condition1.wait()
            print "consumer",count2
        if(count2>10):
            condition2.notify()
            count1=0
            condition1.wait()
            
        count2+=1
        time.sleep(1)
    condition1.release()
    condition2.release()
            

condition1 = threading.Condition()
condition2 = threading.Condition()
count1 = 0
count2=0'''
count = 0

condition = threading.Condition()

thread.start_new_thread(consumer,())
thread.start_new_thread(producer,())

while(1):
    pass


