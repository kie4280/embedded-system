import os 
import glob
import time
import re
import threading
#initialize the device

class Temp_sensor:
    def __init__(self):

        os.system('sudo modprobe w1-gpio')
        os.system('sudo modprobe w1-therm')
        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folder = glob.glob(self.base_dir + '28*')[0]
        self.device_file = self.device_folder + '/w1_slave'
    def _read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    def read_temp(self):
        t=time.perf_counter()
        lines = self._read_temp_raw()
        print(time.perf_counter()-t)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self._read_temp_raw()    
    
        # t = threading.Timer(0.2, readfile)

        # def readfile(lines):

        #     if lines[0].strip()[-3:] != 'YES':
        #         lines = self._read_temp_raw()               
        #         t.start()
        # readfile(lines)

    # above are some confusing code!!

        # equals_pos = lines[1].find('t=')
        match = re.search(r't=([0-9]*)\n*', lines[1])
        if match != None:
            temp_string = match.group(1)

            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
        else:
            return None, None

# while True:
#     print(read_temp())
#     time.sleep(1) 
