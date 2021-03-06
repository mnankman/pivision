#!/usr/bin/env python
import PCA9685 as servo
import time                  # Import necessary modules

MinPulse = 200
MaxPulse = 700

Current_x = 0
Current_y = 0

def setup():
	global Xmin, Ymin, Xmax, Ymax, homeX, homeY, pwm
	offset_x = 0
	offset_y = 0
	try:
		for line in open('config'):
			if line[0:8] == 'offset_x':
				offset_x = int(line[11:-1])
				#print 'offset_x =', offset_x
			if line[0:8] == 'offset_y':
				offset_y = int(line[11:-1])
				#print 'offset_y =', offset_y
	except:
		pass
	Xmin = MinPulse + offset_x
	Xmax = MaxPulse + offset_x
	Ymin = MinPulse + offset_y
	Ymax = MaxPulse + offset_y
	homeX = (Xmax + Xmin)/2
	homeY = Ymin + 80
	pwm = servo.PWM()           # Initialize the servo controller. 
	pwm.set_frequency(60)


def setx(x):
	global Current_x
	Current_x = x
	pwm.set_value(14, 0, Current_x) # CH14 <---> X axis
	
def sety(y):
	global Current_y
	Current_y = y
	pwm.set_value(15, 0, Current_y) # CH15 <---> Y axis
	
def maxleft():
	setx(Xmax)

def maxright():
	setx(Xmin)

def home_x():
	setx(homeX)

def pan(i):
	global Current_x
	Current_x += i
	r = (Current_x - Xmin) / (Xmax - Xmin)
	if Current_x > Xmax:
		Current_x = Xmax
		r = 1
	if Current_x <= Xmin:
		Current_x = Xmin
		r = 0
	setx(Current_x)
	return r
	
def pan_rel(r):
	global Current_x
	Current_x = int(Xmin + (Xmax - Xmin) * r)
	#print 'Current_x =', Current_x
	setx(Current_x)

def tilt(i):
	global Current_y
	Current_y += i
	r = (Current_y - Ymin) / (Ymax - Ymin)
	if Current_y > Ymax:
		Current_y = Ymax
		r = 1
	if Current_y <= Ymin:
		Current_y = Ymin
		r = 0
	sety(Current_y)
	return r
	
def tilt_rel(r):
	global Current_y
	Current_y = int(Ymin + (Ymax -Ymin) * r)
	sety(Current_y)
	

# ==========================================================================================
# Control the servo connected to channel 14 of the servo control board to make the camera 
# turning towards the positive direction of the x axis.
# ==========================================================================================
def move_decrease_x():
	global Current_x
	Current_x += 25
	if Current_x > Xmax:
		Current_x = Xmax
        pwm.set_value(14, 0, Current_x)   # CH14 <---> X axis
# ==========================================================================================
# Control the servo connected to channel 14 of the servo control board to make the camera 
# turning towards the negative direction of the x axis.
# ==========================================================================================
def move_increase_x():
	global Current_x
	Current_x -= 25
	if Current_x <= Xmin:
		Current_x = Xmin
        pwm.set_value(14, 0, Current_x)
# ==========================================================================================
# Control the servo connected to channel 15 of the servo control board to make the camera 
# turning towards the positive direction of the y axis. 
# ==========================================================================================
def move_increase_y():
	global Current_y
	Current_y += 25
	if Current_y > Ymax:
		Current_y = Ymax
        pwm.set_value(15, 0, Current_y)   # CH15 <---> Y axis
# ==========================================================================================
# Control the servo connected to channel 15 of the servo control board to make the camera 
# turning towards the negative direction of the y axis. 
# ==========================================================================================		
def move_decrease_y():
	global Current_y
	Current_y -= 25
	if Current_y <= Ymin:
		Current_y = Ymin
        pwm.set_value(15, 0, Current_y)
# ==========================================================================================		
# Control the servos connected with channel 14 and 15 at the same time to make the camera 
# move forward.
# ==========================================================================================
def home_x_y():
	setx(homeX)
	sety(homeY)

def calibrate(x,y):
	setx((MaxPulse+MinPulse)/2+x)
	sety((MaxPulse+MinPulse)/2+y)

def test():
	while True:
		home_x_y()
		time.sleep(0.5)
		for i in range(0, 9):
			move_increase_x()
			move_increase_y()
			time.sleep(0.5)
		for i in range(0, 9):
			move_decrease_x()
			move_decrease_y()
			time.sleep(0.5)

if __name__ == '__main__':
	setup()
	home_x_y()
