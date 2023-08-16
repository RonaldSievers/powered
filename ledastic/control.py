import math
import time
import board
import neopixel

from ledastic.log_configuration import logger


pixel_pin = board.D18
num_pixels = 144
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


#
def _display(value, brightness=1.0):
    pixels.fill(COLOR_BLACK)
    color = (255, 0, 0) if value > 0 else (0, 255, 0)
    adjusted_color = (
        (int(255 * brightness), 0, 0) if value > 0 else (0, int(255 * brightness), 0)
    )
    for i in range(0, abs(value)):
        pixels[i] = adjusted_color if i == abs(value) - 1 else color
    pixels.show()


def blink(color, times):
    for _ in range(0, times):
        pixels.fill(color)
        pixels.show()
        time.sleep(0.1)
        pixels.fill(COLOR_BLACK)
        pixels.show()
        time.sleep(0.1)


def wave():
    z = 0.0
    while True:
        for i in range(0, num_pixels):
            s = math.cos(z + i / 10)
            v = int(abs(s) * 255)
            pixels[i] = (0, 0, v)
        pixels.show()
        time.sleep(0.1)
        z += 0.3
        if z > 5:
            break


def animate(color):
    left_side = 0
    right_side = num_pixels - 1
    direction = -1

    start = num_pixels - 1
    end = 0

    while True:
        # go from max to 0
        for i in range(start, end, direction):
            pixels.fill(COLOR_BLACK)
            # left side
            for l in range(0, left_side):
                pixels[l] = COLOR_BLUE
            # right side
            for r in range(right_side, num_pixels):
                pixels[r] = COLOR_GREEN
            pixels[i] = color
            pixels.show()

        # add to the left

        # change direction
        if direction == -1:
            left_side += 1
            direction = 1
            start = left_side
            end = right_side
        else:
            right_side -= 1
            direction = -1
            start = right_side
            end = left_side


def flash(color, times):
    for _ in range(0, times):
        pixels.fill(COLOR_BLACK)
        for i in range(0, num_pixels, 2):
            pixels[i] = color
        pixels.show()
        time.sleep(0.1)
        pixels.fill(COLOR_BLACK)
        for i in range(1, num_pixels - 1, 2):
            pixels[i] = color
        pixels.show()
        time.sleep(0.1)


class PowerBar:
    def __init__(self):
        self.previous_value = 0
        self.clear()

    def clear(self):
        pixels.fill(COLOR_BLACK)
        pixels.show()

    def change_to(self, newvalue, brigthness):
        step = 1 if newvalue > self.previous_value else -1
        for i in range(self.previous_value, newvalue, step):
            _display(i, brigthness)
            # make this async
            time.sleep(0.005)

        self.previous_value = newvalue

    def boot_up(self):
        blink(COLOR_RED, 2)
        blink(COLOR_GREEN, 2)
        blink(COLOR_BLUE, 2)

        flash(COLOR_RED, 2)
        flash(COLOR_GREEN, 2)
        flash(COLOR_BLUE, 2)

        # animate(COLOR_RED)
        wave()
