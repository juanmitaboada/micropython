import pyb
import time
import random

variable = "{} - Hello World".format(random.randint(1, 10))
main = 0
counter = 1
while True:
    pyb.LED(counter).on()
    print(main, variable, counter)
    time.sleep(0.5)
    pyb.LED(counter).off()
    time.sleep(0.25)
    if counter == 4:
        counter = 1
    else:
        counter += 1
    main += 1
    if main == 100:
        break
