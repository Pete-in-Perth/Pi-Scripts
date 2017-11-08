#!/bin/python  
# Script for restarting or shutting down the raspberry Pi by pressing or holding a button.  
# by Peter Glorie

# Button should be connected between ground and GPIO pin
# Use of resistor on one of the button connections recommended to avoid accidental damage to pi.
  
import RPi.GPIO as GPIO  
import time  
import os  
  
# Use the Broadcom SOC Pin numbers  
PIN = 21

# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)  


# Our function on what to do when the button is pressed  
def Shutdown():  
	print("Shutdown initiated")
	time.sleep(0.5)
	os.system("sudo shutdown -h now")  

def Reboot():  
	print("Reboot initiated")
	time.sleep(0.5)
	os.system("sudo reboot")  
	
def BTime(channel):
	t = 0
	while GPIO.input(channel) == GPIO.LOW:
		time.sleep(0.1)
		t += 0.1
		if t > 2: # if button is held long enough
			Shutdown()
	if t > 0.2: 
		Reboot() # if button is released early
	
 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(PIN, GPIO.FALLING, callback = BTime)  
 
# Now wait!  
while 1:  
	time.sleep(1)  
