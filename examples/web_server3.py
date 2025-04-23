# https://programandoconro.wordpress.com/servidor-web-en-el-esp32-chip-con-micropython/
import network
from machine import Pin
from time import sleep
import random
import socket


html = """

<div>
    <center>
        <head>
            <title> Hello Hackers !!</title>
        </head>
        <body>
            <h1>Welcome to my site</h1>
            <input onChange="myName(this.value)"> </input>
            <button onclick="myIndex()"> Push me </button>
        </body>
    </center>
    <script>const myIndex = () => {alert('Hello Hackers')</script>
    <script>const myName = (e) => {alert(e)}</script>
</div>

"""

print(html)
"""
# punto de acceso
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ScaryBug')
"""

# conectar al Wifi
print("1 conectando wifi...")
sta = network.WLAN(network.STA_IF)
print("2 conectando wifi...")
sta.active(True)
print("3 conectando wifi...")
sta.connect("REPLACE_WITH_YOUR_SSID", "REPLACE_WITH_YOUR_PASSWORD")
print("4 conectando wifi...")
print("Conectado ?", sta.isconnected())
while sta.isconnected() == False:
    pass


print("Abriendo socket...")
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
print("socket abierto")
"""
if sta.isconnected():
    led = Pin(2, Pin.OUT)
    for i in range(1, 10**100):
        r = random.randint(0, 1)
        s.listen(1)
        cl, addr = s.accept()
        cl.send(html)
        sleep(0.1)
        led.value(r)
        cl.close()

"""