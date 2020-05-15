#Import libraries
import RPi.GPIO as GPIO
import time
import signal
import os
import sqlite3 as mydb

#Initialize the GPIO

tch = 12
snd = 16
vib = 20
ir = 21

alarm = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(alarm,GPIO.OUT)
GPIO.setup(tch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(snd,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(vib,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ir,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

arm = 0
trigger = 0

#This function will make the alarm ring in intervals of 3
def ring():
	while True:
		for i in range (3):
			GPIO.output(alarm,False)
			time.sleep(.1)
			GPIO.output(alarm,True)
			time.sleep(.1)

		time.sleep(.5)

#This function disarms the system
def disarm():
	arm = 0
	trigger = 0
	GPIO.output(alarm, True)

def sensorStatus():
	if GPIO.input(snd) or GPIO.input(vib) or GPIO.input(ir):
		return 1

def clearLog():
	os.system('rm ../log/sensorLog.db')

con = mydb.connect('../log/sensorLog.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS sensorLog(Date INTTEGER, Arm INTEGER, Trigger INTEGER)""")



#Call the blinkOnce function above in a loop
try:
	GPIO.output(alarm, True)
	while True:
		if GPIO.input(tch) == GPIO.HIGH:
			arm = 1
		if arm == 1:
			sensorStatus()
			if GPIO.input(snd) or GPIO.input(vib) or GPIO.input(ir):
				trigger = 1
			if trigger == 1:
				cur.execute('INSERT INTO sensorLog (Date, Arm, Trigger) VALUES(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'), arm, trigger))
				print(time.strftime('%Y‐%m‐%d %H:%M:%S')+" Arm: %d Trigger: %d\n" %(arm, trigger))
				ring()
		print(GPIO.input(ir))
		print(time.strftime('%Y‐%m‐%d %H:%M:%S')+" Arm: %d Trigger: %d\n" %(arm, trigger))
		time.sleep(.5)

#Cleanup the GPIO when done
except KeyboardInterrupt:
	clearLog()
	os.system('clear')
	print('--END--')
	GPIO.cleanup()
