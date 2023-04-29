import json
import sys, time
sys.path.append('path/to/src/')
from Database import Database as d
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO


def main():
    GPIO.cleanup()
    db = d()
    reader = SimpleMFRC522()
    while True:
        idd, text = reader.read()
        if idd != None:
            if idd in db.get_keys():
                db.remove_key(idd)
                reader.write("")
                GPIO.setup(16, GPIO.OUT)
                GPIO.output(16, 1)
                time.sleep(0.25)
                GPIO.output(16, 0)
            break
    GPIO.cleanup()

if __name__ == '__main__':
    main()
