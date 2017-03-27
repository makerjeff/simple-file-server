import cv2
import time

folder_path = 'images/'

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)
current_frame = 1

# while True:
#     current_frame += 1
#     check, frame = video.read()
#
#     print check
#     print frame
#
#     cv2.imshow('videoh', frame)
#
#     key = cv2.waitKey(1000/15)
#
#     if key == ord('q'):
#         break

def capture_some_frames(frames=30, framerate=15):

    while current_frame <= frames:

        check, frame = video.read()

        global current_frame

        print check
        print frame

        cv2.imshow('veedeeoh', frame)
        cv2.imwrite(folder_path + 'frame_%04d.jpg' % current_frame, frame, [cv2.IMWRITE_JPEG_QUALITY, 50])

        key = cv2.waitKey(1000/framerate)

        current_frame += 1

        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    video.release()
    print str(frames) + ' successfully captured to ' + folder_path + '. '


def Main():
    capture_some_frames(90, 15)


if __name__ == '__main__':
    Main()



