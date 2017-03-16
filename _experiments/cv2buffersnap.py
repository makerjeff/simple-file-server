import cv2
import time
import numpy as np
from PIL import Image


# CREATE BUFFER
#buffer = StringIO()

# SETUP CAMERA
snap = cv2.VideoCapture(1)
snap.set(3, 640)
snap.set(4, 480)


# TAKE PIC
check, frame = snap.read()


# VIEW PIC
cv2.imshow('original', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
snap.release()


# SAVE TO FILE AS JPG (NEED TO WORK ON A STRING BUFFER. ENCODE / DECODE?)
cv2.imwrite('temp.jpg', frame)

# OPEN IMAGE FROM PIL AS JPG
img = Image.open('temp.jpg')
img.save('buffered_image_from_PIL.jpg')
img.close()

# FROM BUFFER SAVE IMAGE TO FILE