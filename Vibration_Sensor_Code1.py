import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

CS = 36
SCLK = 38
DOUT = 40
#Set up function
def Vib_Start():
    GPIO.setup(DOUT, GPIO.IN)
    GPIO.setup(CS, GPIO.OUT)
    GPIO.setup(SCLK, GPIO.OUT)

    GPIO.output(CS, GPIO.HIGH)
    GPIO.output(SCLK, GPIO.HIGH)

def read_value():
    regval = 0#Is blank value used to simulate register to store read in bits
    GPIO.output(CS, GPIO.LOW)#Toggles CS to start read
    time.sleep(.000005)
    
    for x in range(16):
        GPIO.output(SCLK, GPIO.LOW)#Simulates Clock Pulse
        GPIO.output(SCLK, GPIO.HIGH)
        new = GPIO.input(DOUT)#Reads in bit value to DOUT
        regval = regval << 1#Shifts left 1
        regval = regval | new#OR new bit with old shifted data
    GPIO.output(CS, GPIO.HIGH)
    #Converts to voltage
    regval = regval*2.5
    regval = regval/4095
    regval = regval*1000
    
    return regval

