import time

from pyb import LED, Pin, ADC  # type: ignore

print("Starting...")

pin_azul = Pin("Y1", Pin.OUT)
pin_rojo = Pin("Y2", Pin.OUT)
pin_verde = Pin("Y3", Pin.OUT)
pin_blanco = Pin("Y4", Pin.OUT)
pin_luz = ADC(Pin("X1"))


while True:
    cantidad_luz = pin_luz.read()
    print("Luz:", cantidad_luz)
    if cantidad_luz < 1200:
        luces = (0, 0, 0, 0)
    elif 1200 < cantidad_luz <= 2000:
        luces = (1, 0, 0, 0)
    elif 2000 < cantidad_luz <= 3000:
        luces = (1, 1, 0, 0)
    elif 3000 < cantidad_luz <= 4000:
        luces = (1, 1, 1, 0)
    else:
        luces = (1, 1, 1, 1)

    pin_azul.value(luces[0])
    pin_rojo.value(luces[1])
    pin_verde.value(luces[2])
    pin_blanco.value(luces[3])
    time.sleep(0.1)
