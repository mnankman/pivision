# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

def init():
	global camera, cascade
	# initialize the video streams and allow them to warmup
	print("[INFO] starting camera...")
	camera = VideoStream(src=0).start()
	time.sleep(2.0)
	cascade = cv2.CascadeClassifier('cascade.xml')

def detect():
	frame = camera.read()
	frame = imutils.resize(frame, width=200)

	# convert the frame to grayscale, blur it slightly
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect objects using the cascade
	return cascade.detectMultiScale(gray, 1.3, 5)
	
def paint_detected_objects(frame, objects):
	j=0
	for (x,y,w,h) in objects:
		cv2.putText(frame, '#'+str(j), (x,y+h-2), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		j=j+1
		
	# read and grab the current timestamp
	timestamp = datetime.datetime.now()
	ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")

	# draw the timestamp on the frame
	cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	return frame
