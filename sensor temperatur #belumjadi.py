import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
SENSOR = Adafruit_DHT.DHT11
PIN = 21

while True:
    kelembapan, temperatur = Adafruit_DHT.read_retry(SENSOR, PIN)
    if kelembapan is not None and temperatur is not None:
        print("Temp ={0:0.1f}*C kelembapan= {1:0.1f}%", format(temperatur, kelembapan))
        
    else:
        print("sensor failed")
        time.sleep(2)