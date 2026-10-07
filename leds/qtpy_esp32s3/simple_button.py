# Hold the button to light the onboard NeoPixel green
# Adafruit QT Py ESP32-S3
import time
import board
import digitalio
import neopixel

# Onboard LED
power = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
power.switch_to_output(True)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

# Button between A1 and GND
button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if button.value == False:      # pressed
        led.fill((0, 255, 0))      # green
    else:
        led.fill((0, 0, 0))        # off
    time.sleep(0.02)
