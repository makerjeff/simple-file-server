import cv2
from PIL import Image
import numpy as np
import random

# 307200 (640x480),  76800 (320,240)
filesizes = [(480,640), (240,320), (16,16)]    # CV2 XY is reversed, written as ROW, COLUMN

def random_pattern(max):
    # create an image array
    iar = np.arange(max)

    # write the random data
    for item in iar:
        #iar[item] = random.randrange(0, 256)
        print item

    # reshape the array
    iar = iar.reshape(filesizes[1])

    # write the file
    cv2.imwrite('random.png', iar)

def write_random_pattern(max, iterations):

    iterator = 0
    iar = np.arange(max)

    while iterator < iterations:

        for item in iar:
            iar[item] = random.randrange(0, 256)

        iar = iar.reshape(filesizes[1][1], filesizes[1][0])

        print iar
        print iterator

        cv2.imwrite('img_seq/' + 'img_' + str(iterator) + '.jpg', iar)

        iterator += 1

def display_random_pattern():

    current_frame = 1

    iar = np.zeros(307200, dtype=np.uint8)  #np.uint8 = unsigned integer 8-bit (0-255)
    iar = iar.reshape(480, 640)

    while True:
        current_frame += 1

        # iterate X
        for item in iar:
            iar[item] = random.randrange(0,255)

        #iar = iar.reshape(480,640)
        print iar

        cv2.imshow('video', iar)
        key = cv2.waitKey(1000/15)

        if key == ord('q'):
            break

    print 'Number of iterations: ' + str(current_frame)
    cv2.destroyAllWindows()

def show_pixel_array():

    # this works properly.
    iar = np.zeros(307200, dtype=np.uint8)  #dtype=np.uint8 is required for cv2images.

    for item in range(1, 307200):
         iar[item] = random.randrange(0, 255)

    iar = iar.reshape(480,640)

    cv2.imshow('pic', iar)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#def pixel sequence


def Main():

    #show_pixel_array()
    display_random_pattern()
    # write_random_pattern(76800, 100)
    # random_pattern(filesizes[1][0] * filesizes[1][1])

if __name__ == '__main__':
    Main()