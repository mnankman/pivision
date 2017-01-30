# pivision
Open CV based object recognition for Raspberry PI (specifically the Sunfounder Smartcar for Raspberry PI)

This project aims to make the Smartcar (equiped with a Raspberry PI 3 and a camera that can pan and tilt) follow a path indicated by pilons.
Therefor, the PI needs te be able to recognize pilons. For that purpose, OpenCV 3.1.0 is used. First, a cascade training is done for the 
recognition of pilons. The current version (pilondetect.py + cascade.xml) is fairly (but still not sufficiently) able to recognize pilons 
in test images. 

The next step is to make the car steer towards the nearest pilon it sees.
