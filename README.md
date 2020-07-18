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

### Software Prerequisites

1. Latest Raspbery OS (Raspberian) from `https://www.raspberrypi.org/downloads/raspberry-pi-os/`
2. RGB LED Matrix python bindings from: `https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python`

### Running

```
$ ./pitrix.py
```

### Credits

Henner Zeller for the rpi-rgb-led-matrix lib @ https://github.com/hzeller/rpi-rgb-led-matrix