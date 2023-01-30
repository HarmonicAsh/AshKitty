#!/usr/bin/python3
#https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
#INSTALL: #pip3 install adafruit-circuitpython-pca9685
#pip3 install adafruit-circuitpython-motorkit

import sys
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

sys.path.append("..")
from calibrate import *
from SR04 import *
#from MPU6050 import *



#Need an array here of saved calibration values
#Need an array of maximum angles
#Add a modifier to set the central position as zero

def start_cat():
        print("\n \n------------------------------------------------------------------")
        print("Welcome to the AshKitty. Enter a command to begin!") 
        print("------------------------------------------------------------------")
        print("'calib'' to set all servos to zero and begin the calibration process")
        print("'dist' to check the ultrasonic sensor distance for 10 seconds")
        print("'quit' to terminate") 
        print("'test' to operate the function test() as required") 

def shutdown():
    #pca.deinit() #This perhaps disables the controller?
    os._exit(0)

def test_func():
    pass

def read_in():
    serial_in = input()            #Reads serial inputs
    if serial_in == 'calib':       #Runs zero function
         from_main()
    elif serial_in == 'test':      #Runs test_func() function
         test_func()
    elif serial_in == 'quit':      #Terminate the program
         shutdown()
    elif serial_in == 'dist':      #Terminate the program
         check_dist()

def check_dist():
    print("\nMeasured distance (centimetres)")
    for i in range(10):
        print(distance()) 
        time.sleep(1)
    start_cat()

if __name__ == '__main__':
    setup_all()
    start_cat
    while True:
        read_in()

sit = [   # Petoi sit command. Initial array: [1 frame, 0 x axis angle, -30 y axis angle, 1 ???]
1, 0, -30, 1,
    0,   0, -45,   0,  -5,  -5,  20,  20,  45,  45, 105, 105,  45,  45, -45, -45]