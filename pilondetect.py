import numpy as np
import cv2

cascade_lpb = cv2.CascadeClassifier('cascade_LBP/cascade.xml')
cascade_haar = cv2.CascadeClassifier('cascade_HAAR/cascade.xml')

for i in range(1,17):
	img = cv2.imread('test/test' + str(i) + '.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	objects = cascade_lpb.detectMultiScale(gray, 1.3, 5)
	j=0
	for (x,y,w,h) in objects:
		img = cv2.putText(img, '#'+str(j), (x,y+h-2), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		j=j+1
		

	cv2.imshow('img',img)
	cv2.waitKey(0)
cv2.destroyAllWindows()
