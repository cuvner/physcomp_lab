# physcom_lab

Physical computing examples for students. Each activity gets you writing code that controls real hardware, such as lights, sensors, motors and displays.

All code in this repo is written in **[CircuitPython](https://circuitpython.org/)** unless a folder says otherwise. CircuitPython is a version of Python made by Adafruit for small boards. You save your program to the board like a file on a USB stick and it runs straight away.

## What is in here

```
physcom_lab/
└── leds/
    ├── feather_rp2040/   LED matrix activities for the Adafruit Feather RP2040
    └── pico2_w/          LED activities for the Raspberry Pi Pico 2 W
```

Each topic has its own folder, with one subfolder per device. Open a device folder and read its `README.md` first. That is your worksheet.

## The devices

| Device | What it is | Buy it | Set it up |
| --- | --- | --- | --- |
| Adafruit Feather RP2040 | Small microcontroller board with USB-C and a built-in NeoPixel | [The Pi Hut](https://thepihut.com/products/adafruit-feather-rp2040) | [Adafruit guide](https://learn.adafruit.com/adafruit-feather-rp2040-pico) · [CircuitPython download](https://circuitpython.org/board/adafruit_feather_rp2040/) |
| Raspberry Pi Pico 2 W | Low-cost microcontroller with Wi-Fi and Bluetooth | [The Pi Hut](https://thepihut.com/products/raspberry-pi-pico-2-w) | [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/) · [CircuitPython download](https://circuitpython.org/board/raspberry_pi_pico2_w/) |
| BBC micro:bit V2 | Classroom board with an LED grid, buttons and sensors built in | [The Pi Hut](https://thepihut.com/products/micro-bit-v2) | [Getting started](https://microbit.org/get-started/getting-started/introduction/) · [micro:bit Python Editor](https://python.microbit.org/) · [CircuitPython download](https://circuitpython.org/board/microbit_v2/) |
| Raspberry Pi 5 | A full computer running Linux, with GPIO pins for hardware | [The Pi Hut](https://thepihut.com/products/raspberry-pi-5) | [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html) · [CircuitPython libraries on Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux) |

New to CircuitPython? Start with Adafruit's [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython) guide.

## Getting started

### Feather RP2040 and Pico 2 W

Both boards use the same steps.

1. Download the CircuitPython `.uf2` file for your board from the download link in the table. Choose the latest stable release.
2. Hold the **BOOTSEL** button while you plug the board in by USB. It appears as a USB drive.
3. Drag the `.uf2` file onto that drive. The board restarts and appears as a new drive called **CIRCUITPY**.
4. Add the libraries your program needs. Download the bundle that matches your CircuitPython version from the [CircuitPython libraries page](https://circuitpython.org/libraries), then copy the library files you need into the `lib` folder on CIRCUITPY. The LED activities need `neopixel.mpy`.
5. Copy a program from this repo onto CIRCUITPY and rename it `code.py`. It runs as soon as you save it.

You can edit `code.py` in any editor, but [Thonny](https://thonny.org/) or [Mu](https://codewith.mu/) let you see error messages and `print()` output. In Thonny, choose **Run > Configure interpreter > CircuitPython (generic)**.

### micro:bit

The quickest route is the [micro:bit Python Editor](https://python.microbit.org/) in your browser. It uses the micro:bit's own version of MicroPython, so programs start with `from microbit import *` rather than `import board`. The micro:bit can also run CircuitPython using the download in the table, but the browser editor is simpler for most activities.

### Raspberry Pi 5

The Raspberry Pi 5 is a full computer, so it runs normal **Python 3**, not CircuitPython firmware. Set it up with Raspberry Pi OS using the getting started guide. Adafruit's Blinka library then lets you run CircuitPython-style code, such as `import board`, on the Pi. Code for the Pi lives in folders marked `raspberry_pi`.

## Working safely

- **Check the power before you light lots of LEDs.** A board powered from USB can only supply about 500 mA. A full LED panel at high brightness needs far more. Keep brightness at the value the worksheet gives you.
- **Unplug before you rewire.** Never move jumper wires while the board is powered.
- **Check your pin numbers.** Every board labels its pins differently. Use the pin your device's worksheet gives you, not one from a different board.

## How to use this repo

1. Find the topic folder, then your device's subfolder.
2. Read the worksheet `README.md` from top to bottom.
3. Copy the starter program onto your board as `code.py` and run it before you change anything.
4. Work through the worksheet one part at a time.
