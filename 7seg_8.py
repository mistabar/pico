import time
from machine import Pin, PWM

# wyświetla latającą 8 na 7 segmentach

# piny odpowiadające segmentom wyświetlacza
a = 14
b = 13
c = 18
d = 17
e = 16
f = 15
g = 19

segs = [PWM(Pin(a)),
        PWM(Pin(b)),
        PWM(Pin(c)),
        PWM(Pin(d)),
        PWM(Pin(e)),
        PWM(Pin(f)),
        PWM(Pin(g))]

sgs = [PWM(Pin(a)),
        PWM(Pin(b)),
        PWM(Pin(g)),
        PWM(Pin(e)),
        PWM(Pin(d)),
        PWM(Pin(c)),
        PWM(Pin(g)),
        PWM(Pin(f))
        ]
a = 0           # aktualny
m = len(sgs)    # długość tabeli, do liczenia modulo
while True:
    a = (a + 1) % m     # przechodzimy do kolejnego segmentu
    p1 = (a + m -1) % m # poprzedni segment
    p2 = (a + m -2) % m # 2 do tyłu 
    
    for q in range(0, m):
        if q not in [a,p1,p2]:
            sgs[q].duty_u16(2**8) # wygaszanie pozostałych
            
    sgs[a].duty_u16((2**16) -2)
    sgs[p1].duty_u16(2**14)
    sgs[p2].duty_u16(2**12)
            
    time.sleep(.4)
    

