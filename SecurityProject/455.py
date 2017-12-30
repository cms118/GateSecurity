import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s')



def consumer(cv):
    while(1):
        logging.debug('Consumer thread started ...')
        with cv:
            logging.debug('Consumer waiting ...')
            cv.wait()
            logging.debug('Consumer consumed the resource')
        time.sleep(1)

def producer(cv):
    while(1):
        logging.debug('Producer thread started ...')
        with cv:
            count+=1
            logging.debug('Making resource available')
            logging.debug('Notifying to all consumers')
            if count>10:
                cv.notifyAll()
        time.sleep(1)

if __name__ == '__main__':
    count = 0
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()
