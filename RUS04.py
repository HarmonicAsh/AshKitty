# Test code for the RUS04 built in ultrasonic sensor

#Copied code from SR04.py and modified
#Libraries (please install Python GPIO library first!!)
from math import dist
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM) #GPIO Mode (BOARD / BCM)
GPIO_IO = 18 #set GPIO Pin
 
def distance():
    GPIO.setup(GPIO_IO, GPIO.OUT)   #Sets the pin to act as an output
    GPIO.output(GPIO_IO, True)      #Set Trigger to HIGH
    time.sleep(0.00001)            
    GPIO.output(GPIO_TRIGGER, False)  #Set Trigger after 0.01ms to LOW
 
    StartTime = time.time()
    StopTime = time.time()
 
    GPIO.setup(GPIO_IO, GPIO.IN)    #Sets the pin to act as an input


    # save StartTime
    while GPIO.input(GPIO.IO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO.IO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

if __name__ == '__main__':
    try:
        print(distance())
        time.sleep(0.5)








 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

        
   