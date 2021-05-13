#!/usr/bin/python3
from gpiozero import LED,Button
from threading import Event

led = LED(17)
pir = Button(18, pull_up = False)
btn = Button(23)
evt = Event()

active = False

led.blink(on_time=0.2, off_time=0.1, n=2, background=True)

def pirHandler():
	global pir
	print('pir handler')
	while pir.is_pressed:
		led.blink(on_time=0.1, off_time=0.2, n=2, background=False)

def btnHandler():
	global active
	global pir
	global pirHandler
	active = not active
	print('active = ', active)
	pir.when_pressed = None
	if active:
		pir.when_pressed = pirHandler

btn.when_pressed = btnHandler
pir.when_pressed = pirHandler

while not evt.wait(timeout=30):
	print('koniec evt')

print('koniec końców')

#while True:
#	pass

