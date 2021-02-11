import time
from machine import Pin, PWM
# piny odpowiadające segmentom wyświetlacza
a = 14
b = 13
c = 18
d = 17
e = 16
f = 15

segs = [PWM(Pin(a)),
        PWM(Pin(b)),
        PWM(Pin(c)),
        PWM(Pin(d)),
        PWM(Pin(e)),
        PWM(Pin(f))]

i = 0
while True:
    p = (i + 5) % 6 # poprzedni segment
    n = (i + 1) % 6 # nastepny segment
    for q in range(0, len(segs)):
        if q not in [p,i,n]:
            segs[q].duty_u16(2**8) # wygaszanie pozostałych
            
    segs[n].duty_u16((2**16) -2)
    segs[i].duty_u16(2**14)
    segs[p].duty_u16(2**12)
    
    i = (i + 1) % 6 # przechodzimy do nastepnego segmentu
        
    time.sleep(.3)
    
