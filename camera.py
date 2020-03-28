from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime

button = Button(17)
camera = PiCamera()

camera.rotation = 180
camera.start_preview(fullscreen = False, window = (100,200,300,400), alpha = 200)

try:
    button.wait_for_press()
    dt = str(datetime.datetime.now())
    nombre = 'pic_' + dt + '.jpg'
    camera.capture('/home/pi/Desktop/%s' % nombre)
finally:
    camera.stop_preview()
    camera.close()