import threading
import time
import queue


class eventListener:

    listenerWorks = dict()
    threads = 0

    def __init__(self, refresh_rate=0.01, maxQueueSize=30):
        eventListener.threads = eventListener.threads+1
        self.refresh_rate = refresh_rate
        self.loop = True
        self.workQueue = queue.Queue(maxsize=maxQueueSize)
        self.dict_lock = threading.Lock()
        self.queue_lock = threading.Lock()
        self.workEvent = threading.Event()
        self.thread_listen = threading.Thread(
            target=self.runListener, daemon=True)
        self.thread_listen.start()
        self.thread_callback = threading.Thread(
            target=self.runCallback, daemon=True)
        self.thread_callback.start()

        pass

    def runCallback(self):
        while self.loop:
            self.workEvent.wait()
            # self.queue_lock.acquire()
            try:
                call, kwargs = self.workQueue.get()                
                call(**kwargs)
                self.workQueue.task_done()

            except Exception as e:
                print(e)
            finally:
                self.queue_lock.acquire()
                if self.workQueue.qsize() == 0:
                    self.workEvent.clear()
                self.queue_lock.release()
                # if self.queue_lock.locked():
                #     self.queue_lock.release()

            pass

    def addCallback(self, callback, kwargs):
        self.queue_lock.acquire()
        try:
            self.workQueue.put((callback, kwargs), False)
        except queue.Full:
            print("Max queue size reached, the callback takes too long to run. \
            Another thread may be needed.")            
            pass
        finally:
            self.workEvent.set()
            if self.queue_lock.locked():
                self.queue_lock.release()

    def runListener(self):
        # print(time.perf_counter())

        while self.loop:

            start = time.perf_counter()            
            self.dict_lock.acquire()
            try:
                for _, work in self.listenerWorks.items():

                    eventTup = work[0](**work[2])
                    if type(eventTup) == tuple:
                        hasEvent, param_dict = eventTup
                    else:
                        hasEvent = eventTup
                        param_dict = dict()

                    if hasEvent:
                        return_dict = dict(work[3])
                        if(len(param_dict) > 0):
                            return_dict.update(param_dict)
                  
                        self.addCallback(work[1], return_dict)
                        print("add callback")                      

            except:
                pass
            finally:
                if self.dict_lock.locked():
                    self.dict_lock.release()
            # print(time.perf_counter()-start)
            time.sleep(self.refresh_rate)

    def addListener(self, check, callback,
                    args_check=dict(), args_call=dict()):
        content = (check, callback, args_check, args_call)
        key = (id(check), id(callback), id(args_check),
               id(args_call))
        self.dict_lock.acquire()
        self.listenerWorks[key] = content
        if self.dict_lock.locked():
            self.dict_lock.release()

        return key

    def removeListener(self, key):
        self.dict_lock.acquire()
        try:
            if self.listenerWorks.get(key, None) != None:
                # self.loop = False
                # print("dict size", len(self.listenerWorks.items()))
                self.listenerWorks.pop(key)
                # print("dict size", len(self.listenerWorks.items()))
                # self.loop = True
                # self.thread = threading.Thread(target=self.run, daemon=True)
                # print("new thread")
                # self.thread.start()
            else:
                print(key, "is not present")
                pass
        finally:
            self.dict_lock.release()

    def __del__(self):
        self.loop = False

        pass

    def reset(self):
        pass


class eventScheduler:
    def __init__(self):
        pass


e = eventListener(0.5, 3)
i = 0

loop = True

L1 = None


def check():
    global i
    i += 1
    # print(a ,b)
    if(i == 4):
        i = 0
        return True, {"pressed": True}
    else:
        return False


def callback(pressed):
    global loop, L1, i
    
    print("event fired")      

    for a in range(10):
        time.sleep(1)
    # print(a ,b)    

L1 = e.addListener(check, callback)
while loop:
    time.sleep(1)
