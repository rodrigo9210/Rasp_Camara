from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime

button = Button(17)
camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.rotation = 180
camera.start_preview(fullscreen = False, window = (200,50,600,800))

try:
    button.wait_for_press()
    dt = str(datetime.datetime.now())
    nombre = 'pic_' + dt + '.jpg'
    camera.capture('/home/pi/Desktop/%s' % nombre)
finally:
    camera.stop_preview()
    camera.close()