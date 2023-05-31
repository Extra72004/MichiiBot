from machine import Pin, PWM
import time

def firme():
    
    #td=trasea derecha
    #dd=delantera derecha
    #ti=trasera izquierda
    #di=delantera izquierda
    
    #p=pata
    servo_pdd = PWM(Pin(27)) #verde
    servo_ptd= PWM(Pin(33)) #blanco
    servo_pdi=PWM(Pin(25)) #amarillo
    servo_pti=PWM(Pin(26)) #gris
    
    #r=rodilla
    servo_rdd=PWM(Pin(12)) #rojo
    servo_rtd=PWM(Pin(13)) #azul
    servo_rdi=PWM(Pin(14)) #vino cafe
    servo_rti=PWM(Pin(32)) #naranja
    
    servo_pdd.freq(50)
    servo_ptd.freq(50)
    servo_pdi.freq(50)
    servo_pti.freq(50)
    
    servo_rdd.freq(50)
    servo_rtd.freq(50)
    servo_rdi.freq(50)
    servo_rti.freq(50)
    
    servo_ptd.duty_ns(int((12.346*90**2 + 7777.8*90 + 700000)))
    servo_rtd.duty_ns(int((12.346*0**2 + 7777.8*0 + 700000)))
    
    servo_pti.duty_ns(int((12.346*110**2 + 7777.8*110 + 700000)))
    servo_rti.duty_ns(int((12.346*180**2 + 7777.8*180 + 700000)))
    
    time.sleep(0.001)
    
    servo_pdd.duty_ns(int((12.346*90**2 + 7777.8*90 + 700000)))
    servo_rdd.duty_ns(int((12.346*180**2 + 7777.8*180 + 700000)))
    
    servo_pdi.duty_ns(int((12.346*110**2 + 7777.8*110 + 700000)))
    servo_rdi.duty_ns(int((12.346*0**2 + 7777.8*0 + 700000)))

    time.sleep(0.01)
    
while True:
    firme()
