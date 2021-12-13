from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2560, 1440)
camera.rotation = 180

name = "white_rtut"
def take_photo(name):

    camera.start_preview()
    sleep(5)  
    camera.capture("/home/gr104/lab104/" + name + ".png")
    camera.stop_preview()

take_photo(name)