from gpiozero import LED
import RPi.GPIO as GPIO
import time

led1 = LED(21)
led2 = LED(20)
touch = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(touch, GPIO.IN)

while True:
    if GPIO.input(touch) == 1:
        led1.on()
        time.sleep(1)
        led2.on()
        time.sleep(1)
    else:
        led1.off()
        led2.off()