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

#arms the system
def arm():
	arm = 1

#Clears previous entries
def clearLog():
	os.system('rm ../log/sensorLog.db')

#Tries to connect to a database. If there isn't one, it makes one
con = mydb.connect('log/sensorLog.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS sensorLog(Date INTEGER, Arm INTEGER, Trigger INTEGER)""")



#Call the blinkOnce function above in a loop
try:
	#initializes state of alarm pin or it will sound in the beginning
	GPIO.output(alarm, True)
	arm = 0
	trigger = 0
	while True:
		#checks to see if arming switch has been hit
		if GPIO.input(tch) == GPIO.HIGH:
			arm = 1
		#checks to see if the system is armed
		if arm == 1:
			#checks if any of the sensors have been triggered
			if GPIO.input(snd) or GPIO.input(vib) or GPIO.input(ir):
				trigger = 1
			#if the system has been triggered then it logs it to the sensorLog database and rings until the system is disarmed
			if trigger == 1:
				cur.execute('INSERT INTO sensorLog (Date, Arm, Trigger) VALUES(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'), arm, trigger))
				con.commit()
				print(time.strftime('%Y‐%m‐%d %H:%M:%S')+" Arm: %d Trigger: %d\n" %(arm, trigger))
				ring()

		cur.execute('INSERT INTO sensorLog (Date, Arm, Trigger) VALUES(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'), arm, trigger))
		con.commit()
		print(time.strftime('%Y‐%m‐%d %H:%M:%S')+" Arm: %d Trigger: %d\n" %(arm, trigger))
		time.sleep(.5)

#Cleanup the GPIO when done
except KeyboardInterrupt:
	clearLog()
	os.system('clear')
	print('--END--')
	GPIO.cleanup()
