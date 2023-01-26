#!/usr/bin/python3

#INSTALL: #pip3 install adafruit-circuitpython-pca9685    

import sys
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

sys.path.append("..")
from calibrate import *

#Need an array here of saved calibration values
#Add a modifier to set the central position as zero

def start_cat():
        print("\n \n------------------------------------------------------------------")
        print("Welcome to the AshKitty. Enter a command to begin!") 
        print("------------------------------------------------------------------")
        print("'calib'' to set all servos to zero and begin the calibration process") 
        print("'quit' to terminate") 
        print("'test' to operate the function test() as required") 

def shutdown():
    #pca.deinit() #This perhaps disables the controller?
    pass

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

 if __name__ == '__main__':
    setup_all()
    start_cat
        while true:
        read_in()