#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import time
import signal
import os
import sqlite3 as mydb
import sys

#Assign GPIO pins
soundPin  = 17 #placeholder
vibrationPin = 18 #placeholder
infraredPin = 19 #placeholder
alarmPin = 20 #placeholder

#Initialize Sensor Variables
sound = 0
vibration = 0
infrared = 0
armed = 0

#Arms System
def arm():
	armed  = 1

#Disarms System
def disarm():
	armed = 0

#Reads Sound Sensor
def readSound(SoundPin):
	humidity, temperature = DHT.read_retry(tempSensor,17)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Error Reading Sensor')
	return tempFahr

#Reads Vibration Sensor
def readVibration(vibrationPin):

#Reads Infrared Sensor
def readInfrared(infraredPin):

#Sounds Alarm
def alarm(alarmPin):
	

con = mydb.connect('../log/sensorLog.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS sensorLog(Sound INTTEGER, Vibration INTEGER, Infrared INTEGER, Armed Integer)""")
try:
	while True:
	
		cur.execute('INSERT INTO sensorLog (Sound, Vibration, Infrared, Armed) VALUES(?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'), data))
		con.commit()
		print ("Sound:"+sound+" Vibration:"+vibration+" Infrared:"+infrared+" Armed:"+armed)
		time.sleep(60)

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
	con.close()
