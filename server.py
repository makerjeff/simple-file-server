# started basic code with jeff-work

import socket
import threading
import os
import sys

from custom_colors import bcolors

# threaded file retrieval function

def retr_file(name, sock):

    # listen for a filename request
    filename = sock.recv(1024)

    # if the file exists
    if os.path.isfile(filename):

        # respond with 'EXISTS header and file size
        sock.send('EXISTS ' + str(os.path.getsize(filename)))

        # wait for client response
        user_response = sock.recv(1024)

        # if the first two characters of client response is 'OK'
        if user_response[:2] == 'OK':

            # open file with auto-close
            with open(filename, 'rb') as f:
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)

                while bytes_to_send != '':
                    print 'sending...'
                    bytes_to_send = f.read(1024)
                    sock.send(bytes_to_send)
                print 'completed!'

        else:
            # error, therefore send-o el error-o
            sock.send('ERR')

        # close de socket.
        sock.close()

    else:
        sock.send('NOPE')

def Main():
    host = sys.argv[1]
    port =5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)
    print bcolors.OKBLUE + 'Server started and listening on ' + host  + bcolors.ENDC

    # infiniti loop!
    while True:
        connection, addr = s.accept()

        print 'client connected ip: <' + str(addr) + '>'

        t = threading.Thread(target=retr_file, args=('retr_thread', connection))
        t.start()

    # if popping out of while loop, close socket.
    s.close()

if __name__ == '__main__':
    Main()
