#GPIO 18 Payload ORANGE

import RPi.GPIO as GPIO

import time

from time import sleep

servoPIN = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN, GPIO.OUT)

pwm=GPIO.PWM(servoPIN, 50)

pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 3
	GPIO.output(18, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(18, False)
	pwm.ChangeDutyCycle(0)


SetAngle(90)
time.sleep(0.5)
SetAngle(0)

pwm.stop()

GPIO.cleanup()
