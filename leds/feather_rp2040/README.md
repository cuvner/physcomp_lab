# Lighting Every LED with a For Loop

Year 12 Computer Science

## Starting point

Your starter program lights the first LED red and the last LED blue. Everything in between stays off. Your job is to light every LED using a for loop.

The matrix looks like a grid of 8 rows and 32 columns. Python does not see a grid. It sees one long line of 256 LEDs.

```python
import board
import neopixel

num_pixels = 8 * 32
pixels = neopixel.NeoPixel(board.D5, num_pixels, brightness=0.02, auto_write=False)

red = (255, 0, 0)
blue = (0, 0, 255)

pixels[0] = red
pixels[num_pixels - 1] = blue

pixels.show()
```

Starter program: [`first_and_last_led.py`](first_and_last_led.py)

**The rules**

- You must use a for loop.
- You must not use `pixels.fill()`. It does the job for you and hides the thinking.
- Keep `brightness` at 0.02. The panel is powered through the Feather's USB, which supplies about 500 mA. 256 LEDs at full power would need around 15 A, enough to reset the board or damage the USB port.

## Part 1: Read and predict

Answer these before you run anything.

1. How many LEDs are on the matrix? Show the calculation.
2. The first LED is `pixels[0]`. Why does counting start at 0 and not 1?
3. Why is the last LED `pixels[num_pixels - 1]` and not `pixels[num_pixels]`? What would happen if you used `pixels[num_pixels]`?
4. Write the actual number that `num_pixels - 1` works out to.
5. A colour is written as three numbers, for example `(255, 0, 0)`. What does each number control?
6. What would `(0, 255, 0)` look like? What about `(255, 255, 0)`?
7. Delete the line `pixels.show()` and predict what happens. Then test it. Why does this line matter when `auto_write=False`?

Now run the program and check that what you see matches your answers.

## Part 2: Spot the pattern

Imagine lighting every LED without a loop. It would start like this:

```python
pixels[0] = red
pixels[1] = red
pixels[2] = red
pixels[3] = red
```

1. How many lines like this would you need to light every LED?
2. Look at the four lines above. What stays the same on every line? What changes?
3. The part that changes goes up by how much each time?
4. Fill in the table.

| Line number | Index used | Colour |
| --- | --- | --- |
| 1st | 0 | red |
| 2nd | | red |
| 10th | | red |
| 100th | | red |
| Last | | red |

5. Write a rule in plain English: "On every line, the index is..."

When only one thing changes and it changes by the same amount each time, a loop can do the repeating for you. The thing that changes becomes the loop variable.

## Part 3: Build the loop

Warm up on paper first. What does each of these print?

| Code | Output |
| --- | --- |
| `for i in range(5): print(i)` | |
| `for i in range(2, 6): print(i)` | |
| `for i in range(0, 10, 2): print(i)` | |

1. `range(5)` stops before which number?
2. You need the loop to visit every index from the first LED to the last. Which `range()` gives you exactly that? Use `num_pixels` rather than typing the number.
3. Complete the skeleton below. Replace the two gaps.

```python
for i in range(________):
    pixels[____] = red

pixels.show()
```

4. Should `pixels.show()` sit inside the loop or after it? Try both. Describe the difference you see.
5. Run it. Did every LED light? If not, which ones were missed and why?
6. Keep your starter lines for the first and last LED but put them after the loop. What happens to those two LEDs now? Why does the order of the code matter?

## Part 4: Extend

Pick at least two. Each one changes one small thing about your loop.

1. **Every other LED.** Light only the even-numbered LEDs. There are two ways: change the `range()` or add an `if` with `%`. Try both.
2. **Two colours.** Alternate red and blue down the whole line.
3. **First half, second half.** Light the first 128 LEDs red and the last 128 blue. Use `num_pixels // 2` rather than typing 128.
4. **Backwards.** Light the LEDs one at a time from the last to the first. You will need `import time`, `time.sleep(0.02)` and `pixels.show()` inside the loop. Which `range()` counts down?
5. **Fade.** Make the red value grow along the line so the first LED is dim and the last is bright. Hint: the index runs from 0 to 255 and so does a colour value.
6. **Challenge.** The sample program reaches an LED with `x * 8 + y`. Use two nested loops to light only the top row of the matrix. What does this tell you about how the LEDs are wired?
