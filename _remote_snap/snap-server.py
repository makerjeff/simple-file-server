import socket
import threading
import os
import sys

## enable on Pi
#import picamera

import cv2
from PIL import Image
import numpy as np

from custom_colors import bcolors

# threaded file retrieval
def retr_file(name, sock):

    filename = sock.recv(1024)

    if os.path.isfile(filename):
        sock.send('EXISTS ' + str(os.path.getsize(filename)))
        user_response = sock.recv(1024)

        if user_response[:2] == 'OK':

            #TODO: swap this for camera-snap

            with open(filename, 'rb') as f:
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)

                while bytes_to_send != '':
                    print 'sending data...'
                    bytes_to_send = f.read(1024)
                    sock.send(bytes_to_send)

                print 'completed!'

        else:
            sock.send('KO')

        sock.close()

    else:
        sock.send('FU')


def Main():
    host = sys.argv[1]
    port = 5000

    s = socket.socket()
    s.bind((host, port))    #BIND for server, CONNECT for client.
    s.listen(5)

    print bcolors.OKBLUE + 'Server started and listening on ' + host + bcolors.ENDC

    while True:
        connection, addr = s.accept()
        print 'client connected ip: <' + str(addr) + '>'

        t = threading.Thread(target=retr_file, args=('retr_thread', connection), verbose=True)
        t.start()

    s.close()

if __name__ == '__main__':
    Main()
