import socket
import threading    #don't use this for now
import sys
import os

def send_sequential_files(name, sock):
    filename = sock.recv(1024)

    if os.path.isfile(filename):
        sock.send('EXISTS ' + str(os.path.getsize(filename)))

        user_response = sock.recv(1024)

        if user_response[:2] == 'OK':

            with open(filename, 'rb') as f:
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)

                while bytes_to_send != '':
                    print 'sending... '
                    bytes_to_send = f.read(1024)
                    sock.send(bytes_to_send)
                print 'completed. '

        else:
            sock.send('ERR')

    else:
        sock.send('NOPE')

def Main():
    host = sys.argv[1]
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(5)
    os.system('clear')
    print 'Server started and listening on ' + str(host) + '...'

    while True:
        connection, addr = s.accept()

        print 'client connected ip: ' + str(addr) + '>'

        # changed threaded to single
        send_sequential_files('filesender', connection)

    s.close()   # close after connection is done.
    print str(addr) + ' socket closed. '

if __name__ == '__main__':
    Main()


