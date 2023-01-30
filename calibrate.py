#Make this script output a file with servo position parameters for the main program to use
def setup_all():                        #Sets up the i2c bus and enables all 16 channels
    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c)
    pca.frequency = 50
    for i in range(16):
        servo[i] = servo.Servo(pca.channels[i], min_pulse=500, max_pulse=2600)

def instruct():
    print("\n \n------------------------------------------------------------------")
    print("Welcome to the the calibration program. Enter a command to begin:") 
    print("------------------------------------------------------------------")
    print("'zero'' to set all servos to calibrated zero") 
    print("'quit' to terminate") 
   
def set_zero():
    for i in range(16):
        servo[i].angle = 90
        time.sleep(0.05)
    print("All servos at central position... install all joints now")

def servo_cal():
    pass

def from_main():
    instruct()
    print("'back' to return to the main function") 

if __name__ == '__main__':
    setup_all()
    instruct()
    