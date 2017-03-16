# started basic code with jeff-work
import socket
import sys
import os
from custom_colors import bcolors


def Main():
    # ping server and request file list
    # type in file name to download, otherwise hit 'q' to quit.
    # if file doesn't exist, alert user and display list again.

    host = sys.argv[1]
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input('Filename? -> ')

    if filename != 'q':

        # send request
        s.send(filename)    # this triggers the server to respond via code

        # server response with 1024 bytes
        data = s.recv(1024)

        # if data header = 'exists' (can put response code here instead)
        if data[:6] == 'EXISTS':

            # grab the filesize header
            filesize = long(data[6:])

            # ask if User wants to download
            message = raw_input('File Exists, ' + str(filesize) + ' bytes, download? (Y/N) -> ')

            # if user inputs Y, send to server 'OK' status
            if message == 'Y':
                s.send('OK')

                # open a new file for writing
                f = open('new_' + filename, 'wb')

                # load the first 1024 bytes of data
                data = s.recv(1024)

                # set total received value
                total_received = len(data)

                # write the first 1024 bytes
                f.write(data)

                # while not finished,
                while total_received < filesize:
                    data = s.recv(1024)
                    total_received += len(data)
                    f.write(data)
                    print '{0: .3f}'.format((total_received/float(filesize)) * 100) + '% done.'

                print 'Download complete.'
        else:
            print 'Default error.'

    # close the connection
    s.close()



# Boiler Plate
if __name__ == '__main__':
    Main()