from machine import Pin
from time import sleep

# Configración de GPIO
ledpin_door = 13
ledpin_motor_up = 15
ledpin_motor_down = 2
ledpin_motor_left = 0
ledpin_motor_right = 4

pin_door = Pin(ledpin_door, Pin.OUT)
pin_motor_up = Pin(ledpin_motor_up, Pin.OUT)
pin_motor_down = Pin(ledpin_motor_down, Pin.OUT)
pin_motor_left = Pin(ledpin_motor_left, Pin.OUT)
pin_motor_right = Pin(ledpin_motor_right, Pin.OUT)
"""
"""


class Door(object):
    def __init__(self, pin):
        self.pin = pin

    def open(self):
        self.pin.value(0)

    def close(self):
        self.pin.value(1)


class Motor(object):
    def __init__(self, pin_up, pin_left, pin_right, pin_down):
        self.pin_up = pin_up
        self.pin_left = pin_left
        self.pin_right = pin_right
        self.pin_down = pin_down

    def stop(self):
        self.pin_up.value(0)
        self.pin_left.value(0)
        self.pin_right.value(0)
        self.pin_down.value(0)

    def start(self):
        self.pin_up.value(1)
        self.pin_left.value(1)
        self.pin_right.value(1)
        self.pin_down.value(1)

    def up(self):
        self.stop()
        self.pin_up.value(1)

    def left(self):
        self.stop()
        self.pin_left.value(1)

    def right(self):
        self.stop()
        self.pin_right.value(1)

    def down(self):
        self.stop()
        self.pin_down.value(1)


door = Door(pin_door)
motor = Motor(pin_motor_up, pin_motor_left, pin_motor_right, pin_motor_down)

door.close()
motor.stop()

while True:
    door.close()

    motor.up()
    sleep(0.5)
    motor.down()
    sleep(0.5)
    motor.left()
    sleep(0.5)
    motor.right()

    sleep(0.5)
    door.open()
    # motor.start()
    sleep(0.5)
