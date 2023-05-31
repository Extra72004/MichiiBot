from machine import Pin, PWM
import time

servo=PWM(Pin(14))
    
servo.freq(50)
n=110#angulo
duty = int((12.346*n**2 + 7777.8*n + 700000))

servo.duty_ns(duty)
