import time
from machine import Pin, PWM

# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(15))
pwmx = PWM(Pin(25))
pwm2 = PWM(Pin(16))

# Set the PWM frequency.
pwm.freq(1000)
pwmx.freq(1000)
pwm2.freq(1000)

# Fade the LED in and out a few times.
duty = 0
duty2 = 255
direction = 3
dir2 = -3
while True:
    duty += direction
    duty2 += dir2
    if duty > 255:
        duty = 255
        duty2 = 0
        direction = -3
        dir2 = 3
    elif duty < 0:
        duty = 0
        duty2 = 255
        direction = 3
        dir2 = -3
    pwm.duty_u16(duty**2)
    pwmx.duty_u16(duty2**2)
    pwm2.duty_u16(duty2**2)
    time.sleep_ms(15)