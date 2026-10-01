import board
import neopixel

# The matrix has 8 rows and 32 columns, so 8 x 32 = 256 LEDs.
# Python does not see a grid. It sees ONE long line of LEDs,
# numbered from 0 up to 255.
num_pixels = 8 * 32

# Connect to the LEDs on pin D5 of the Feather RP2040.
# brightness is kept very low on purpose. The panel is powered through the
# Feather's USB, which can only supply about 500 mA. 256 LEDs at full power
# would need around 15 A. Do NOT raise this value.
# auto_write=False means nothing changes until we call pixels.show()
pixels = neopixel.NeoPixel(board.D5, num_pixels, brightness=0.02, auto_write=False)

# Colours are written as (red, green, blue). Each value goes from 0 to 255.
red = (255, 0, 0)
blue = (0, 0, 255)

# Turn on the FIRST LED in the line
pixels[0] = red

# Turn on the LAST LED in the line
pixels[num_pixels - 1] = blue

# Send the colours to the matrix
pixels.show()
