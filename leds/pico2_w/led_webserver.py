import time
import wifi
import socketpool
import board
import digitalio
from secrets import secrets
from adafruit_httpserver import Server, Request, Response, GET

# Connect to Wi-Fi
print("Connecting to Wi-Fi...")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to", secrets["ssid"])
print("IP address:", wifi.radio.ipv4_address)

# Setup onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Create a socket pool and server
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

# HTML page with a button
HTML = """
<html>
  <head><title>LED Control</title></head>
  <body>
    <h1>Blink the LED</h1>
    <form action="/blink" method="get">
      <button type="submit">Blink LED</button>
    </form>
  </body>
</html>
"""

@server.route("/", GET)
def base(request: Request):
    return Response(request, HTML, content_type="text/html")

@server.route("/blink", GET)
def blink(request: Request):
    led.value = True
    time.sleep(1)
    led.value = False
    return Response(request, body="LED blinked!<br><a href='/'>Go back</a>", content_type="text/html")

# Start the server
server.start(str(wifi.radio.ipv4_address))
print("Server started, connect to: http://{}".format(wifi.radio.ipv4_address))

# Main loop
while True:
    try:
        server.poll()
    except Exception as e:
        print("Error:", e)
