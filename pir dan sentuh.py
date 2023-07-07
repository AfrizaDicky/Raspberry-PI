from gpiozero import LED
import RPi.GPIO as GPIO
import time



led1 = LED(21)
led2 = LED(20)
touch = 26
pir = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(touch, GPIO.IN)
GPIO.setup(pir, GPIO.IN)

while True:
    print(GPIO.input(pir))
    if GPIO.input(touch) == 1 or GPIO.input(pir) == 1:
        led1.on()
        led2.on()
        
        
    else:
        led1.off()
        led2.off()
        
GPIO.cleanup()