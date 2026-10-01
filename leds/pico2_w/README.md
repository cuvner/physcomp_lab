# Blinking the Built-in LED

Raspberry Pi Pico 2 W

## Starting point

The Pico 2 W has a small green LED on the board, next to the USB port. You do not need any wires. Your program turns it on, waits, turns it off, waits, and repeats forever.

```python
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   # LED on
    time.sleep(0.5)
    led.value = False  # LED off
    time.sleep(0.5)
```

Starter program: [`blink.py`](blink.py)

Copy `blink.py` onto CIRCUITPY and rename it `code.py`. The LED should start flashing straight away.

## Part 1: Read and predict

Answer these before you run anything.

1. `led.value` can be `True` or `False`. Which one turns the LED on?
2. How many times will the LED flash in one second? Show how you worked it out.
3. Why does the program need `while True:`? What would happen without it?
4. Delete the second `time.sleep(0.5)` and predict what happens. Then test it. Explain what you see.

Now run the program and check that what you see matches your answers.

## Part 2: Change the timing

1. Make the LED flash twice as fast.
2. Make it stay on for 1 second but off for only 0.1 seconds.
3. Use a variable called `delay` for the timing so you only have to change one number.

## Part 3: Count the flashes

1. Replace `while True:` with a for loop so the LED flashes exactly 10 times, then stops.
2. Add `print()` so the console shows the flash number each time.
3. Make the LED flash your age, then stop.

## Extension: Morse code

Flash SOS: three short flashes, three long flashes, three short flashes. Then pause and repeat. Write a function `flash(length)` so you do not repeat the same lines.

## Next step: Blink from a web page

The Pico 2 W has Wi-Fi. [`led_webserver.py`](led_webserver.py) joins your network and serves a web page with a button. Press the button and the LED blinks.

1. Copy [`secrets_example.py`](secrets_example.py) onto CIRCUITPY, rename it `secrets.py` and fill in your Wi-Fi name and password. See [Wi-Fi and the secrets file](../../README.md#wi-fi-and-the-secrets-file).
2. Make sure the `adafruit_httpserver` folder is in `lib` on CIRCUITPY. It comes in the CircuitPython library bundle.
3. Copy `led_webserver.py` onto CIRCUITPY as `code.py`.
4. Open the serial console. The board prints its IP address. Type that address into a browser on the same network.
