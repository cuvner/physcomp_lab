# Touch any pad on the MPR121 to turn the NeoPixel strip on or off
# Adafruit QT Py ESP32-S3
import time
import board
import neopixel
import adafruit_mpr121

# Setup NeoPixels (60 LEDs on A0)
pixel_pin = board.A0
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.02, auto_write=False)

# MPR121 touch sensor (12 pads) on the STEMMA QT socket
i2c = board.STEMMA_I2C()
touch = adafruit_mpr121.MPR121(i2c)

leds_on = False
was_touched = False

while True:
    # True if any of the 12 pads is being touched
    touched = any(touch[i].value for i in range(12))

    # Toggle only when a finger first lands, not while it's held
    if touched and not was_touched:
        leds_on = not leds_on
        if leds_on:
            pixels.fill((255, 0, 0))
        else:
            pixels.fill((0, 0, 0))
        pixels.show()
        print("LEDs ON" if leds_on else "LEDs OFF")

    was_touched = touched
    time.sleep(0.02)
