import time
import sys
sys.path.append('path/to/src/')
from Database import Database as db
import RPi.GPIO as GPIO
d = db()
print("reset")
d.update_open("false")
outPin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.output(outPin, 1)
GPIO.output(16, 0)
GPIO.cleanup