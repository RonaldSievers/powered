# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

from ledastic.log_configuration import logger

# Configure the count of pixels:
PIXEL_COUNT = 36

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(
    PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO
)

COLOR_RED = (1, 0, 0)
COLOR_GREEN = (0, 0, 1)


def _display(value):
    pixels.clear()
    color = COLOR_RED if value > 0 else COLOR_GREEN
    for i in range(0, abs(value)):
        pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2]))
    pixels.show()


class PowerBar:
    def __init__(self):
        self.previous_value = 0

    def change_to(self, newvalue):
        step = 1 if newvalue > self.previous_value else -1
        for i in range(self.previous_value, newvalue, step):
            _display(i)
            # make this async
            time.sleep(0.01)
        self.previous_value = newvalue
