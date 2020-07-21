#!/usr/bin/env python3

import time
import picamera
import picamera.array
import random

from vector_2d import Vector
from base import PitrixBase

class Bouncy(PitrixBase):
    def __init__(self, *args, **kwargs):
        super(Bouncy, self).__init__(*args, **kwargs)

    def run(self):

        position = Vector(random.randint(1,32), random.randint(1,32))
        velocity = Vector(random.randint(1,2), random.randint(1,2))

        while True:
            self.matrix.Clear()
            position = position + velocity

            if position.x > self.matrix.width or position.x < 0:
                velocity = Vector(velocity.x * -1, velocity.y)
            if position.y > self.matrix.height or position.y < 0:
                velocity = Vector(velocity.x, velocity.y * -1)

            self.matrix.SetPixel(position.x,  position.y, random.randint(0,255), random.randint(0,255), random.randint(0,255))
            time.sleep(0.05)

# entrypoint ...
if __name__ == "__main__":
    bouncy = Bouncy()
    if (not bouncy.bootstrap()):
        bouncy.print_help()