import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 30
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)


#
def _display(value):
    pixels.fill((0, 0, 0))
    color = COLOR_RED if value > 0 else COLOR_GREEN
    for i in range(0, abs(value)):
        pixels[i] = color
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
