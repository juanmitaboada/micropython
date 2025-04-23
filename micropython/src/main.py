import time

from pyb import LED, Pin  # type: ignore

# from pyb import Pin, ADC  # type: ignore

print("Starting...")

led_rojo = LED(1)
led_verde = LED(2)
led_azul = LED(3)
led_amarillo = LED(4)

pin_azul = Pin("Y1", Pin.OUT)
pin_rojo = Pin("Y2", Pin.OUT)
pin_verde = Pin("Y3", Pin.OUT)
pin_blanco = Pin("Y4", Pin.OUT)


def cambiar(pin, nombre):
    if pin.value() == 0:
        pin.value(1)
    else:
        pin.value(0)


pin_azul.value(0)
pin_rojo.value(0)
pin_verde.value(0)
pin_blanco.value(0)


def verde_blanco(verde, blanco):
    vueltas = 16
    espera = 0.5 / vueltas
    for i in range(vueltas):
        cambiar(pin_verde, "pin_verde")
        time.sleep(espera)
        cambiar(pin_verde, "pin_verde")

        cambiar(pin_blanco, "pin_blanco")
        time.sleep(espera)
        cambiar(pin_blanco, "pin_blanco")


while True:
    print(time.time(), "Time")
    cambiar(pin_azul, "pin_azul")
    verde_blanco(pin_verde, pin_blanco)
    cambiar(pin_azul, "pin_azul")

    cambiar(pin_rojo, "pin_rojo")
    verde_blanco(pin_verde, pin_blanco)
    cambiar(pin_rojo, "pin_rojo")


# # x1 = ADC(Pin("X1"))
# # x2 = ADC(Pin("X2"))
# pins = [Pin("Y{}".format(i), Pin.IN, Pin.PULL_UP) for i in range(1, 11)]
# # y1 = Pin("Y1", Pin.IN, Pin.PULL_UP)
# # y2 = Pin("Y2", Pin.IN, Pin.PULL_UP)

# main = 0
# counter = 1
# while True:
#     LED(counter).on()
#     values = [pin.value() for pin in pins]
#     # vx1 = x1.read()
#     # vx2 = x2.read()
#     # vy1 = y1.value()
#     # vy2 = y2.value()
#     print(
#         main,
#         "      ",
#         values[4],
#         values[3],
#         values[2],
#         values[1],
#         values[0],
#     )
#     print(
#         main,
#         "      ",
#         values[9],
#         values[8],
#         values[7],
#         values[6],
#         values[5],
#     )
#     print("----")
#     LED(counter).off()
#     time.sleep(0.1)
#     if counter == 4:
#         counter = 1
#     else:
#         counter += 1
#     main += 1
#     if main == 1000:
#         break
