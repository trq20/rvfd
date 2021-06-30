# LED Toggle

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(1)


# ADC 

from machine import Pin, ADC
from time import sleep

v = Pin(25, Pin.OUT, value = 1)
adc = ADC(Pin(36))

while True:

    print("El valor del LDR es {}".format(adc.read()))
    sleep(1)

# PWM

from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(14), freq = 5000, duty = 100)
    
