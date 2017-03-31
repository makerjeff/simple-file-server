import numpy as np
import cv2
import sys

# draw a black frame
img = np.zeros((512, 512, 3), np.uint8)

# draw a line
img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# draw a rectangle
img = cv2.rectangle(img, (384,0), (510, 128), (0,255,0), 3)

# draw a circle
img = cv2.circle(img, (447, 64), 63, (0,0,255), -1)

# draw ellipse
img = cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, (255,255,255), -1)

cv2.imshow('window', img)

key = cv2.waitKey(0)

if key == ord('q'):
    cv2.destroyAllWindows()
    sys.exit(0)
