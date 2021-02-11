import time
from machine import Pin, PWM
from urandom import randint

# piny odpowiadające segmentom wyświetlacza
a = 14
b = 13
c = 18
d = 17
e = 16
f = 15
g = 19

sgs = [
    [PWM(Pin(d))],              # dół
    [PWM(Pin(c)),PWM(Pin(e))],  # dolne boki
    [PWM(Pin(b)),PWM(Pin(f))],  # górne boki
    [PWM(Pin(a)),PWM(Pin(g))]   # srodek i góra
]

while True:
    a = 17          # aktualny płomień na dole :-)
    for p in range(0, len(sgs)):  # dla każdego piętra...
        a = a - randint(2,3)      # zmniejsz ogień
        for s in range(0, len(sgs[p])): # dla każdego elementu na piętrze
            mod = randint(-1,1)         # modyfikator lewo-prawo
            sgs[p][s].duty_u16(2**(a+mod) -2) # zaświeć
            time.sleep_ms(50)
    time.sleep_ms(50)
