#Import libraries
import RPi.GPIO as GPIO
import time
import signal
import os
import sys

#Initialize the GPIO

tch = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(tch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def clearLog():
	os.system('rm log/sensorLog.db')

#Call the blinkOnce function above in a loop
try:
	#initializes state of alarm pin or it will sound in the beginning
	arm = 0
	trigger = 0
	while True:
		#checks to see if arming switch has been hit and arms system
		if GPIO.input(tch) == GPIO.HIGH:
			print('System Armed')
			os.system('python3 sensor.py')
			print('--System Disarmed--')
			sys.exit()

#Cleanup the GPIO when done
except KeyboardInterrupt:
	clearLog()
	os.system('clear')
	print('--System Disarmed--')
	GPIO.cleanup()
