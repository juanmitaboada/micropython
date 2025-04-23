from machine import SoftI2C, Pin
from time import sleep
import mpu6050

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
accelerometer = mpu6050.accel(i2c)

# https://github.com/miketeachman/micropython-rotary
#
while True:
    print(accelerometer.get_values())
    sleep(0.5)
