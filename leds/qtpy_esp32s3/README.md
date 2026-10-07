# Touch to Light a NeoPixel Strip

Adafruit QT Py ESP32-S3

## Warm-up: Simple button

Before the touch sensor, start with one button and the NeoPixel built into the QT Py. Hold the button and the NeoPixel glows green. Let go and it turns off.

```python
import time
import board
import digitalio
import neopixel

power = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
power.switch_to_output(True)
led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if button.value == False:      # pressed
        led.fill((0, 255, 0))      # green
    else:
        led.fill((0, 0, 0))        # off
    time.sleep(0.02)
```

Program: [`simple_button.py`](simple_button.py)

**Wiring:** connect one leg of a push button to **A1** and the other leg to **GND**. You do not need a resistor, because `Pull.UP` turns on one inside the board.

**Libraries:** `neopixel.mpy` and `adafruit_pixelbuf.mpy`.

1. `Pull.UP` makes `button.value` read `True` when nothing is pressed. Why does pressing the button make it `False`?
2. Why does the program have to switch on `NEOPIXEL_POWER` first?
3. Change the program so the NeoPixel stays on after you let go, and turns off on the next press. Hint: look at how the touch program below uses `was_touched`.

## Starting point

Touch any pad on the MPR121 touch sensor and the NeoPixel strip turns red. Touch again and it turns off.

```python
import time
import board
import neopixel
import adafruit_mpr121

pixel_pin = board.A0
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.02, auto_write=False)

i2c = board.STEMMA_I2C()
touch = adafruit_mpr121.MPR121(i2c)

leds_on = False
was_touched = False

while True:
    touched = any(touch[i].value for i in range(12))

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
```

Starter program: [`touch_neopixel.py`](touch_neopixel.py)

## What you need

- Adafruit QT Py ESP32-S3
- A strip of 60 NeoPixels
- Adafruit MPR121 12-key capacitive touch sensor with a STEMMA QT socket
- A STEMMA QT cable

## Wiring

**Unplug the QT Py before you wire anything.**

| NeoPixel strip | QT Py |
| --- | --- |
| 5V (red) | 5V |
| GND (white or black) | GND |
| DIN (data in) | A0 |

Plug the MPR121 into the STEMMA QT socket on the QT Py with the cable. That one cable carries power and data, so it needs no other wires.

## Libraries

Copy these from the CircuitPython library bundle into the `lib` folder on CIRCUITPY:

- `neopixel.mpy`
- `adafruit_pixelbuf.mpy`
- `adafruit_mpr121.mpy`
- `adafruit_bus_device` (the whole folder)

## Installing CircuitPython on the QT Py

The QT Py has no BOOTSEL button. Instead:

1. Plug it in by USB.
2. Press the **reset** button, then press it again about half a second later. A drive called **QTPYS3BOOT** appears.
3. Drag the CircuitPython `.uf2` file onto that drive. Use the download for the **QT Py ESP32-S3 no PSRAM**.

## Part 1: Read and predict

Answer these before you run anything.

1. The MPR121 has 12 pads. What does `range(12)` give you, and why does that cover every pad?
2. What does `any(...)` return if just one pad is touched? What if none are?
3. Why does the program remember `was_touched`? What would happen if you held your finger on a pad without it?
4. Keep `brightness` at 0.02. Why does it matter with 60 LEDs powered from USB?

Now run the program and check that what you see matches your answers.

## Part 2: Change it

1. Change the colour from red to green.
2. Make each pad light the strip a different colour. Hint: check `touch[0].value`, `touch[1].value` and so on, one at a time.
3. Make pad 0 light only the first LED, pad 1 the second LED, and so on.

## Extension

Use a for loop so that touching a pad lights the strip one LED at a time, like a bar filling up.
