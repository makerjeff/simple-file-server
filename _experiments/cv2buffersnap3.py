# ===================================
# SNAP AN IMAGE TO A STREAM BUFFER ==
# ===================================
# 2017.MAR.28 WORKING LOGIC, hit

import cv2
import numpy as np
import time
import io

#create buffer
buffer = io.BytesIO()

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)




def grab_frame():
    # read from camera buffer
    check, frame = capture.read()
    cv2.imshow('original', frame)


print 'initializing...'
time.sleep(2)

while True:

    grab_frame()

    key = cv2.waitKey(0)

    if key == ord('a'):
        print ' advancing. '
        grab_frame()
        continue

    else:
        print ' quitting. '
        cv2.destroyAllWindows()
        capture.release()
