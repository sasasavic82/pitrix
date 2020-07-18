#!/usr/bin/env python3

import time
import picamera
import picamera.array

from PIL import Image
from base import PitrixBase

class Pitrix(PitrixBase):
    def __init__(self, *args, **kwargs):
        super(Pitrix, self).__init__(*args, **kwargs)

    def run(self):

        # setup
        camera = picamera.PiCamera(0)
        stream = picamera.array.PiRGBArray(camera)
        camera.resolution = (100,100)

        time.sleep(2)

        # capture a continuous stream from PiCamera
        for frame in camera.capture_continuous(stream, "rgb"):
            
            # truncate the stream so it doesn't overflow the
            # image buffer
            stream.truncate()
            stream.seek(0)
            
            # get frame image and convert it as an array
            image = Image.fromarray(frame.array)

            # scale the image down to a thumbnail of size set by the
            # RGBMatrixOptions
            image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

            self.matrix.SetImage(image)

            # take a pause...
            time.sleep(0.01)

# entrypoint ...
if __name__ == "__main__":
    pitrix = Pitrix()
    if (not pitrix.bootstrap()):
        pitrix.print_help()