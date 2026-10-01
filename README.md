# physcom_lab

Physical computing examples for students. Each activity gets you writing code that controls real hardware, such as lights, sensors, motors and displays.

All code in this repo is written in **MicroPython** unless a folder says otherwise.

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
| Adafruit Feather RP2040 | Small microcontroller board with USB-C and a built-in NeoPixel | [The Pi Hut](https://thepihut.com/products/adafruit-feather-rp2040) | [Adafruit guide](https://learn.adafruit.com/adafruit-feather-rp2040-pico) · [MicroPython firmware](https://micropython.org/download/ADAFRUIT_FEATHER_RP2040/) |
| Raspberry Pi Pico 2 W | Low-cost microcontroller with Wi-Fi and Bluetooth | [The Pi Hut](https://thepihut.com/products/raspberry-pi-pico-2-w) | [Raspberry Pi MicroPython guide](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) · [MicroPython firmware](https://micropython.org/download/RPI_PICO2_W/) |
| BBC micro:bit V2 | Classroom board with an LED grid, buttons and sensors built in | [The Pi Hut](https://thepihut.com/products/micro-bit-v2) | [Getting started](https://microbit.org/get-started/getting-started/introduction/) · [micro:bit Python Editor](https://python.microbit.org/) |
| Raspberry Pi 5 | A full computer running Linux, with GPIO pins for hardware | [The Pi Hut](https://thepihut.com/products/raspberry-pi-5) | [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html) |

## Getting started

### Feather RP2040 and Pico 2 W

Both boards use the same steps.

1. Download the MicroPython `.uf2` file for your board from the firmware link in the table.
2. Hold the **BOOTSEL** button while you plug the board in by USB. It appears as a USB drive.
3. Drag the `.uf2` file onto that drive. The board restarts running MicroPython.
4. Open [Thonny](https://thonny.org/), go to **Run > Configure interpreter** and choose **MicroPython (Raspberry Pi Pico)**. This works for the Feather RP2040 too.
5. Open a program from this repo and press **Run**.

To make a program run every time the board powers on, save it to the board as `main.py`.

### micro:bit

The micro:bit uses its own version of MicroPython. You do not need to install firmware. Write code in the [micro:bit Python Editor](https://python.microbit.org/) in your browser, then send it to the board over USB. Programs start with `from microbit import *`.

### Raspberry Pi 5

The Raspberry Pi 5 is a full computer, so it runs normal **Python 3**, not MicroPython. Set it up with Raspberry Pi OS using the getting started guide, then use Thonny, which comes installed. Code for the Pi lives in folders marked `raspberry_pi` and uses different libraries from the microcontroller examples.

## Working safely

- **Check the power before you light lots of LEDs.** A board powered from USB can only supply about 500 mA. A full LED panel at high brightness needs far more. Keep brightness at the value the worksheet gives you.
- **Unplug before you rewire.** Never move jumper wires while the board is powered.
- **Check your pin numbers.** Every board labels its pins differently. Use the pin your device's worksheet gives you, not one from a different board.

## How to use this repo

1. Find the topic folder, then your device's subfolder.
2. Read the worksheet `README.md` from top to bottom.
3. Copy the starter program onto your board and run it before you change anything.
4. Work through the worksheet one part at a time.
