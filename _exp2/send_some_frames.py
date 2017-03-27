# =================================
# WORKING FRAME SERVER ============
# =================================

import cv2, time, numpy as np, glob, os, sys, socket
from custom_colors import bcolors


folder_path = 'images/'

filelist = glob.glob(folder_path + '*.jpg')


# Process file and send over the socket
def process_and_send(file, name, sock):
    print 'processing and sending file: ' + bcolors.OKGREEN + file + bcolors.ENDC + ', ' + str(os.path.getsize(file) / 100) + 'k'

    # send file descriptor
    sock.send('FD,' + str(os.path.getsize(file)) + ',' + file)

    # wait for 'GO' command from client.
    command = sock.recv(1024)

    if command[:2] == 'GO':

        with open(file, 'rb') as f:
            bytes_to_send = f.read(1024)
            sock.send(bytes_to_send)

            while bytes_to_send != '':
                print 'sending bytes...'
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)
            print bcolors.OKGREEN + 'file completed. ' + bcolors.ENDC






    # with open(file, 'rb') as f:
    #     bytes_to_send = f.read(1024)
    #     sock.send(bytes_to_send)
    #
    #     while bytes_to_send != '':
    #         print 'sending bytes...'
    #     bytes_to_send = f.read(1024)
    #         sock.send(bytes_to_send)
    #     print 'file completed. '







def Main():

    host = sys.argv[1]
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))    # socket.bind for server, socket.connect(?) for client.

    s.listen(5)
    print 'Server started listening on ' + str(host) + '... waiting for client connection. '

    while True:
        connection, addr = s.accept()

        print 'client connected on <' + str(addr) + '>'

        # CHECK FOR CLIENT HANDSHAKE 'OK' signal
        response = connection.recv(1024)

        if response[:2] == 'OK':
            print 'client is good to receive. '

            process_and_send('images/frame_0002.jpg', 'filsender', connection)






if __name__ == '__main__':
    Main()



