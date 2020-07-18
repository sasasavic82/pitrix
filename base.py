import argparse
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))

from rgbmatrix import RGBMatrix, RGBMatrixOptions

class PitrixBase(object):
    def __init__(self, *args, **kwargs):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument("-s", "--sequence", action="store", help="Sequence. RGB", default="RGB", type=str)
        self.parser.add_argument("-r", "--rows", action="store", help="Display rows. 16 for 16x32, 32 for 32x32. Default: 32", default=32, type=int)
        self.parser.add_argument("--cols", action="store", help="Panel columns. Typically 32 or 64. (Default: 32)", default=32, type=int)
        self.parser.add_argument("-c", "--chain", action="store", help="Daisy-chained boards. Default: 1.", default=1, type=int)
        self.parser.add_argument("-P", "--parallel", action="store", help="For Plus-models or RPi2: parallel chains. 1..3. Default: 1", default=1, type=int)
        self.parser.add_argument("-b", "--brightness", action="store", help="LED Brightness. Default: 100. Range: 1..100", default=100, type=int)
        self.parser.add_argument("-m", "--gpio-mapping", help="GPIO Mapping: regular, adafruit-hat, adafruit-hat-pwm" , choices=['regular', 'adafruit-hat', 'adafruit-hat-pwm'], default="adafruit-hat", type=str)
        self.parser.add_argument("--slow-write", action="store", help="Slow down writing to GPIO. Range: 0..4. Default: 1", default=1, type=int)

    def run(self):
        print("Running Pitrix")

    def bootstrap(self):
        self.args = self.parser.parse_args()

        options = RGBMatrixOptions()

        if self.args.gpio_mapping != None:
          options.hardware_mapping = self.args.gpio_mapping
        options.rows = self.args.rows
        options.cols = self.args.cols
        options.chain_length = self.args.chain
        options.parallel = self.args.parallel
        options.brightness = self.args.brightness
        options.led_rgb_sequence = self.args.sequence

        if self.args.slow_write != None:
            options.gpio_slowdown = self.args.slow_write

        self.matrix = RGBMatrix(options = options)

        try:
            # run loop
            print("CTRL-C to stop")
            self.run()
        except KeyboardInterrupt:
            print("Exiting...\n")
            sys.exit(0)

        return True