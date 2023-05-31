from machine import Pin, PWM
import time
from marcha import Marcha
    
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
def caminar1():
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
    
    servo_pdd.duty_ns(int((12.346*100**2 + 7777.8*100 + 700000)))
    servo_rdd.duty_ns(int((12.346*160**2 + 7777.8*160 + 700000)))
#     time.sleep(0.05)
#     servo_rdd.duty_ns(int((12.346*160**2 + 7777.8*160 + 700000)))

    servo_pti.duty_ns(int((12.346*70**2 + 7777.8*70 + 700000)))
    servo_rti.duty_ns(int((12.346*140**2 + 7777.8*140 + 700000)))
#     time.sleep(0.05)
#     servo_rti.duty_ns(int((12.346*130**2 + 7777.8*130 + 700000)))
    
    servo_ptd.duty_ns(int((12.346*95**2 + 7777.8*95 + 700000)))
    servo_rtd.duty_ns(int((12.346*40**2 + 7777.8*40 + 700000)))
     
    servo_pdi.duty_ns(int((12.346*160**2 + 7777.8*160 + 700000)))
    servo_rdi.duty_ns(int((12.346*60**2 + 7777.8*60 + 700000)))
    
    time.sleep(0.01)
def DePaso():
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
    servo_rdd.duty_ns(int((12.346*150**2 + 7777.8*150 + 700000)))

    servo_rti.duty_ns(int((12.346*130**2 + 7777.8*130 + 700000)))
    
# #     servo_ptd.duty_ns(int((12.346*95**2 + 7777.8*95 + 700000)))
# #     servo_rtd.duty_ns(int((12.346*40**2 + 7777.8*40 + 700000)))
# #      
# #     servo_pdi.duty_ns(int((12.346*160**2 + 7777.8*160 + 700000)))
# #     servo_rdi.duty_ns(int((12.346*60**2 + 7777.8*60 + 700000)))
    
    time.sleep(0.01)
    
def caminar2():
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
    servo_pdi.duty_ns(int((12.346*110**2 + 7777.8*110 + 700000)))
    servo_rdi.duty_ns(int((12.346*40**2 + 7777.8*40 + 700000)))
    
    servo_ptd.duty_ns(int((12.346*130**2 + 7777.8*130 + 700000)))
    servo_rtd.duty_ns(int((12.346*40**2 + 7777.8*40 + 700000)))
    
    servo_pdd.duty_ns(int((12.346*50**2 + 7777.8*50 + 700000)))
    servo_rdd.duty_ns(int((12.346*160**2 + 7777.8*160 + 700000)))

    servo_pti.duty_ns(int((12.346*110**2 + 7777.8*110 + 700000)))
    servo_rti.duty_ns(int((12.346*160**2 + 7777.8*160 + 700000)))
    
    time.sleep(0.01)
def Depaso():
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
    servo_rtd.duty_ns(int((12.346*60**2 + 7777.8*60 + 700000)))

    servo_rdi.duty_ns(int((12.346*60**2 + 7777.8*60 + 700000)))
    
    time.sleep(0.01)

for i in range(100):
    Marcha()
    print(i)
    
time.sleep(0.1)
while True:
    
    for i in range(10):
        caminar1()
        print(i)
        
    time.sleep(0.1)
    print("cambio pos")
    
    DePaso()
    time.sleep(0.9)
    
    for i in range(10):
        caminar2()
        
    time.sleep(0.1)
    print("cambio pos")
    
    Depaso()
    time.sleep(0.9)