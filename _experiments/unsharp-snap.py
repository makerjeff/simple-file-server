import cv2
from PIL import Image
import numpy as np
from io import BytesIO
import pickle

buffer = BytesIO()

snap = cv2.VideoCapture(0)
snap.set(3, 640)
snap.set(4, 360)

# take the pic
check, frame = snap.read()

cv2.imshow('original', frame)
print frame.shape

cv2.waitKey(0)
cv2.destroyAllWindows()
snap.release()

retval, cv2buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])

cv2.imwrite('unsharp-snap.jpg', cv2buffer )