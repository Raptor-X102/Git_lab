import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

GPIO.output(24, GPIO.input(21))