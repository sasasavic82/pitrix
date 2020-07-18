# Pitrix
----

Pitrix is a super-simple app that converts your Raspberry Pi PiCamera stream to Adafruit RGB Matrix display. 

![Alt text](./docs/pitrix.gif)

----

## Hardware Requirements

1. Raspberry Pi 2, 3, 4 or Zero
2. Raspberry Pi PiCamera
3. Adafruit RGB Matrix HAT or Bonnet (I have Bonnet)
4. RGB 32x32 LED Matrix (There are also 16x32, 32x32, 64x32 and 64x64 matrices)
5. 5V/4A Power Supply

### Installation

Instructions on how to install the Adafruit RGB Matrix are located @ https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/overview

(Note: I purchased Adafruit RGB Matrix Bonnet, and it's pretty much plug-and-play into the GPIO pins of your Pi)

### Software Prerequisites

1. Latest Raspbery OS (Raspberian) from https://www.raspberrypi.org/downloads/raspberry-pi-os/
2. RGB LED Matrix python bindings from: https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python

### Running
Note: This assumes you have `python 3.x` and LED Matrix drivers installed (Step 2 from Software Prerequisites)  

```
$ ./pitrix.py
```

### Credits

Henner Zeller for the rpi-rgb-led-matrix lib @ https://github.com/hzeller/rpi-rgb-led-matrix