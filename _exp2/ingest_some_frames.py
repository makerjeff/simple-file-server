# ===============================
# WORKING FRAME READER ==========
# ===============================

import cv2, socket, sys, os
import io

buffer = io.BytesIO()

def cv2_output(file):
    img = cv2.imread(file)

    while True:
        cv2.imshow('received file',img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

def Main():
    host = sys.argv[1]
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    input = raw_input('Connect? (y/n)? -> ')

    if input == 'y':

        s.connect((host, port))
        s.send('OK')

        datastring = s.recv(1024)
        print datastring

        data_object = datastring.split(',')
        print data_object

        if data_object[0] == 'FD':
            filesize = long(data_object[1])

            # send GO command.
            s.send('GO')

            with open('download/' + str(data_object[2]), 'wb') as f:
                data = s.recv(1024)

                total_received = len(data)
                f.write(data)

                while total_received < filesize:
                    data = s.recv(1024)
                    total_received += len(data)
                    f.write(data)
                    print '{0: .3f}'.format((total_received/float(filesize)) * 100) + '% done.'

                print 'download complete. '

            #TODO: Remove hardcoding
            print 'displaying to cv2'
            cv2_output('download/images/frame_0002.jpg')

        else:
            print 'default error'

    s.close()

if __name__ == '__main__':
    Main()



