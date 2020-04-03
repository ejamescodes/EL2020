#Import libraries
import RPi.GPIO as GPIO
import time
import signal
import os

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

#This function will make the light blink once
def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(.1)
	GPIO.output(pin,False)
	time.sleep(.1)

#Call the blinkOnce function above in a loop	
try:
	for i in range (10):
		blinkOnce(17)
		time.sleep(.2)


#Cleanup the GPIO when done
except KeyboardInterrupt:
	os.system('clear')
	print('--END--')
	GPIO.cleanup()
