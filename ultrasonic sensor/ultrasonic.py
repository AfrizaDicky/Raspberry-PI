from gpiozero import LED
import RPi.GPIO as GPIO
import time

led1 = LED(21)
led2 = LED(20)
ECHO = 16
TRIG = 26


GPIO.setmode(GPIO.BCM)
"GPIO.setwarnings(False)"


while True:
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, False)
    print("tunggu sebentar!")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.1)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        start=time.time()
    while GPIO.input(ECHO)==1:
        end=time.time()
    duration=end-start
    jarak= duration * 17150
    jarak= round(jarak,2)
    print("jaraknya adalah:", jarak, "cm")
    time.sleep(2)
    
#     pp= float(jarak)
#     if pp >= 5.00:
#         led1.on()
#         time.sleep(1)
#         led1.ff()
#     else:
#         led2.on()
#         time.sleep(1)
#         led2.off
    
