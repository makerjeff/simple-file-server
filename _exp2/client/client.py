import socket
import sys
import os

def Main():

    host = sys.argv[1]
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    filename = raw_input('Filename? -> ')

    if filename != 'q':

        s.send(filename)    # -> request to server

        data = s.recv(1024) # <- response from server

        if data [:6] == 'EXISTS':

            filesize = long(data[6:])

            message = raw_input('File exists, ' + str(filesize) + ' bytes, download? (Y/N) -> ')

            # check input
            if message == 'Y':
                s.send('OK')

                f = open(filename, 'wb')

                data = s.recv(1024)

                total_received = len(data)
                f.write(data)

                while total_received < filesize:
                    data = s.recv(1024)
                    total_received += len(data)
                    f.write(data)
                    print '{0: .3f}'.format((total_received/float(filesize)) * 100) + '% done.'

                print 'Download complete.'
        else:
            print 'Default error.'

    s.close()

if __name__ == '__main__':
    Main()

