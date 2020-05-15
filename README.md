## ![New Paltz Logo](https://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg)
### **Spring 2020 Embedded Linux class**
##### This repository documents my class  work and projects done for CPS342
##### 1. **Personal information** 
#####    Name: Ernest Perez
#####    Major: Computer Engineering
#####    ID: [N03217280](https://github.com/ejamescodes)
#####    Year: Senior
##### 2. **Class Start Date** Jan 21, 2020
##### 3. **Class End Date** May 6, 2020
#####
##### The security.py program waits on the user to activate the touch sensor.
##### - If the touch sensor is activated the sensor.py program starts
##### Sensor.py waits for a reading from the sound, vibration, or infrared sensor
##### - If any of these sensors are activated then alarm sounds and it is logged to the database sensorLog.db
##### The only way to disarm the alarm is through the web interface
##### A flask server reads the content of the database and sends it to be dislayed client side via index.html
##### index.html has two buttons, one for arming and one for disarming
##### - When the arm button is pressed, it essentially does the same thing as the touch sensor and starts sensor.py
##### - When the disarm button is pressed, it stops sensor.py from running
##### **How to build**
##### Materials
##### - 1x Raspberry Pi (Here we used a Raspberry Pi 4)
##### ![Raspberry Pi 4](https://images-na.ssl-images-amazon.com/images/I/71IOISwSYZL._AC_SL1400_.jpg)
##### - 1x Sound Detection Sensor Module
##### ![Sound Detection Sensor Module](https://github.com/ejamescodes/EL2020/blob/final/Pictures/sound.PNG)
##### - 1x Vibration Sensor Module
##### ![Vibration Sensor Module](https://github.com/ejamescodes/EL2020/blob/final/Pictures/vibration.PNG)
##### - 1x HC-SR501 Infrared PIR motion Sensor Module
##### ![HC-SR501 Infrared PIR motion Sensor Module](https://github.com/ejamescodes/EL2020/blob/final/Pictures/IR.PNG)
##### - 1x Buzzer Alarm
##### ![Buzzer Alarm](https://github.com/ejamescodes/EL2020/blob/final/Pictures/alarm.PNG)
##### - 1x Digital Touch Sensor Module
##### ![Digital Touch Sensor Module](https://github.com/ejamescodes/EL2020/blob/final/Pictures/touch.PNG)
##### - Jumper Wires
