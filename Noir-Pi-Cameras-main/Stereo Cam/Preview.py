# Rafael Almazar
# CSUN DMSP
# Fall 2021

# Purpose: Previews the stereo camera feed.

from picamera import PiCamera
from time import sleep

camera = PiCamera()
# camera.rotation(180) # flip upside down

time = 5; # seconds

camera.start_preview()
sleep(time)
camera.stop_preview()