import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

tempSensor = DHT.DHT11
tempPin = 17
def readF(tempPin):
	humidity, temperature = DHT.read_retry(tempSensor,tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Error Reading Sensor')
	return tempFahr

while True:
	data = readF(tempPin)
	print(data)
