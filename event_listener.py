import threading
import time


class eventListener:

    works = dict()

    def __init__(self, refresh_rate=0.01):
        self.refresh_rate = refresh_rate
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()
        pass

    def run(self):

        while True:
            for _, work in self.works.items():
                hasEvent, param_dict = work[0](**work[2])

                if hasEvent:
                    return_dict = dict(work[3])
                    if(len(param_dict)>0):
                        return_dict.update(param_dict)
                    work[1](**return_dict)
            time.sleep(self.refresh_rate)

    def addListener(self, check, callback,
                    args_check=dict(), args_call=dict()):
        content = (check, callback, args_check, args_call)
        key = (id(check), id(callback), id(args_check),
               id(args_call))
        self.works[key] = content

        return key

    def removeListener(self, key):
        try:
            self.works.pop(key)
        except KeyError as e:
            print(key, "is not present")
            pass

        pass

class eventScheduler:
    def __init__(self):
        pass


e = eventListener(1)
i=0
loop=True
def check(a, b):
    global i
    i += 1
    print(a ,b)
    if(i==4):
        return True, {"a":1, "b":2}
    else :
        return False, {"a":1, "b":2}

def callback(a, b):
    print("event fired")
    print(a ,b)
    global loop
    loop=False
e.addListener(check, callback, {"a":1, "b":2})
while loop:
    time.sleep(1)