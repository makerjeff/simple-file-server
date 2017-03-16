import cv2
import time
from io import BytesIO
from io import StringIO

video = cv2.VideoCapture(1)
video.set(3, 640)
video.set(4, 480)
check, frame = video.read() # returns 2 objects: 'retval', and image.

print check
print frame

time.sleep(1)

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print 'file length ' + str(len(gray.flat))

cv2.imshow('video frame', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
video.release()

cv2.imwrite('dummyfile_color.jpg', frame)
cv2.imwrite('dummyfile_gray.jpg', gray)

cv2.imwrite('dummyfile_color_sm.jpg', frame, [(cv2.IMWRITE_JPEG_QUALITY), 10])
cv2.imwrite('dummyfile_gray_sm.jpg', gray, [(cv2.IMWRITE_JPEG_QUALITY), 10])

