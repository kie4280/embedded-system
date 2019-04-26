import threading
import time
import queue


class eventListener:

    listenerWorks = dict()
    threads = 0

    def __init__(self, refresh_rate=0.01):
        eventListener.threads = eventListener.threads+1
        self.refresh_rate = refresh_rate
        self.loop = True
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()
        self.workQueue = queue.LifoQueue()

        pass

    def run(self):
        # print(time.perf_counter())

        while self.loop:

            start = time.perf_counter()
            self.lock.acquire()
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
                        # work[1](**return_dict)
                        threading.Thread(target=work[1], kwargs=return_dict).start()
            except:
                pass
            finally:
                self.lock.release()
            # print(time.perf_counter()-start)
            time.sleep(self.refresh_rate)

    def addListener(self, check, callback,
                    args_check=dict(), args_call=dict()):
        content = (check, callback, args_check, args_call)
        key = (id(check), id(callback), id(args_check),
               id(args_call))
        self.listenerWorks[key] = content
        self.reset()

        return key

    def removeListener(self, key):
        self.lock.acquire()
        if self.listenerWorks.get(key, None) != None:
            self.loop = False
            
            try:
                print("dict size", len(self.listenerWorks.items()))
                self.listenerWorks.pop(key)
                print("dict size", len(self.listenerWorks.items()))
                self.loop = True

            finally:
                pass
            self.thread = threading.Thread(target=self.run, daemon=True)
            print("new thread")
            self.thread.start()
        else:
            print(key, "is not present")
            pass
        self.lock.release()

    def reset(self):
        pass


class eventScheduler:
    def __init__(self):
        pass


# e = eventListener(1)
# i = 0

# loop = True


# def check():
#     global i
#     i += 1
#     # print(a ,b)
#     if(i == 4):
#         return True, {"pressed": True}
#     else:
#         return False


# def callback(pressed):
#     print("event fired")
#     print(pressed)
#     # print(a ,b)
#     global loop, L1
#     e.removeListener(L1)
#     print("removed")


# L1 = e.addListener(check, callback)
# while loop:
#     time.sleep(1)
