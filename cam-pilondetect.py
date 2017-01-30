# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

# initialize the video streams and allow them to warmup
print("[INFO] starting camera...")
camera = VideoStream(src=0).start()
time.sleep(2.0)

cascade = cv2.CascadeClassifier('cascade.xml')

# initialize the two motion detectors, along with the total
# number of frames read
n = 0

# loop over frames from the video streams
while True:
	# initialize the list of frames that have been processed
	frames = []

	# read the next frame from the video stream and resize
	# it to have a maximum width of 400 pixels
	frame = camera.read()
	frame = imutils.resize(frame, width=200)

	# convert the frame to grayscale, blur it slightly, update
	# the motion detector
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	objects = cascade.detectMultiScale(gray, 1.3, 5)
	j=0
	for (x,y,w,h) in objects:
		cv2.putText(frame, '#'+str(j), (x,y+h-2), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		j=j+1

	n += 1
	
	if (n >= 10):
		# read and grab the current timestamp
		timestamp = datetime.datetime.now()
		ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")

		# draw the timestamp on the frame and display it
		cv2.putText(frame, ts, (10, frame.shape[0] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		cv2.imshow("webcam", frame)
		n = 0

	# check to see if a key was pressed
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
camera.stop()

