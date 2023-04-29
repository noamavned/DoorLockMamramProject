import time
import sys, os
sys.path.append('path/to/src/')
from Database import Database as db
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
import sqlite3
import subprocess
time.sleep(15)
GPIO.output(16, 1)
time.sleep(0.5)
GPIO.output(16, 0)
os.system("python path/to/reset_pro.py")

while True:
    proc = subprocess.Popen(["python", "path/to/RFID_CHECKER.py"])
    proc.wait()