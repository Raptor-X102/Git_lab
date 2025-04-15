import RPi.GPIO as GPIO

pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

n = 10
p = GPIO.PWM(pin, 1000)
p.start(0)

try:
    while True:
        f = int(input())
        p.ChangeDutyCycle(f)
        print(3.3*f/100)

finally:
    p.stop()
    GPIO.output(pin,0)
    GPIO.cleanup()