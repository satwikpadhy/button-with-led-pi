import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Pin 8 for LED
GPIO.setup(7, GPIO.IN) # Pin 7 for the button

while True:
    if GPIO.input(7):
        print("Button Pressed!")
        GPIO.output(8, GPIO.HIGH) # If pin 7 is high, turn on pin 8
        sleep(0.2)
        os.system('clear')
    else:
        GPIO.output(8, GPIO.LOW) # If pin 7 is low, turn off pin 8
        sleep(0.2)
