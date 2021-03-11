import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(7, GPIO.IN) # Set pin 7 to be an input pin

while True:
    if GPIO.input(7):
        GPIO.output(8, GPIO.HIGH) # If pin 7 is high, turn on pin 8
    else
        GPIO.output(8, GPIO>LOW) # If pin 7 is low, turn off pin 8
