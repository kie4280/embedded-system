import requests
import time 
url = "http://172.18.108.76:8080/"

def toggleLED(status):    
    requests.get(url+("enable" if status else "disable")+"torch")


def takePhoto(file_loc="image.jpg"):
    response = requests.get(url+"photo.jpg")
    with open(file_loc, "wb") as img:
        img.write(response.content)
        img.close()    
def toggleCamera(loc=True):
    requests.get(url+"settings/ffc?set="+("on" if loc else "off"))

if __name__=="__main__":
    # takePhoto()
    # toggleLED(True)
    # time.sleep(1)
    # toggleLED(False)
    # toggleCamera(True)
    pass
