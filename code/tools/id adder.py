import json
import sys
sys.path.append('path/to//src/')
from Database import Database as d
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import random, string, time


def main():
    GPIO.cleanup()
    db = d()
    reader = SimpleMFRC522()
    while True:
        id, text = reader.read()
        if id != None:
            if id not in db.get_keys():
                reader.write(db.get_tagText())
                db.insert_key(id)
                GPIO.setup(16, GPIO.OUT)
                GPIO.output(16, 1)
                time.sleep(0.25)
                GPIO.output(16, 0)
            break
    GPIO.cleanup()

if __name__ == '__main__':
    main()