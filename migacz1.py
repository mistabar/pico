import time
from machine import Pin, PWM


# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(25))

# Set the PWM frequency.
pwm.freq(1000)

# Fade the LED in and out a few times.
duty = 0
direction = 1
for _ in range(64 * 256):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -5
    elif duty < 0:
        duty = 0
        direction = 2
    pwm.duty_u16(duty * duty)
    time.sleep_ms(9)
    