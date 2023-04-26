from machine import Pin, PWM
import time

def main():
    #Configura el Servo de 180
    #ptd=pata trasea derecha
    #pdd=pata delantera derecha
    #pti=pata trasera izquierda
    #pdi=pata delantera izquierda
    
    servo_pdd = PWM(Pin(25))
    servo_ptd= PWM(Pin(26))
    servo_pdi=PWM(Pin(27))
    servo_pti=PWM(Pin(14))
    
    servo_ptd.freq(50)
    servo_pdd.freq(50)
    servo_pti.freq(50)
    servo_pdi.freq(50)

    duty = int((12.346*30**2 + 7777.8*30 + 700000))
    antiduty = int((12.346*170**2 + 7777.8*170 + 700000))
    
    servo_pdd.duty_ns(duty)
    servo_ptd.duty_ns(antiduty)
    servo_pdi.duty_ns(duty)
    servo_pti.duty_ns(antiduty)
    
    time.sleep(0.65)
    
    servo_pdd.duty_ns(antiduty)
    servo_ptd.duty_ns(duty)
    servo_pdi.duty_ns(antiduty)
    servo_pti.duty_ns(duty)
    
    time.sleep(0.65)   
        
while True:
    main()