import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Write number from 0 to 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, decimal2binary(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"Output voltage is {voltage:.4} volt")
            else:
                if num < 0:
                    print("Number must be >=0\n")
                elif num > 255:
                    print("Number is out of range\n")  
        except Exception:
            if num == "q": break
            print("Input string\n")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("The end\n")