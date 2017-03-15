import socket
import threading
import os

from custom_colors import bcolors

# Threaded file-retrieval function
def retr_file(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))

        user_response = sock.recv(1024)

        if user_response [:2] == 'OK':

            with open(filename, 'rb') as f:
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)

                while bytes_to_send != '':
                    bytes_to_send = f.read(1024)
                    sock.send(bytes_to_send)

        else:
            sock.send('ERR')

        sock.close()

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)
    print bcolors.OKBLUE + 'Server started and listening...' + bcolors.ENDC

    while True:
        connection, addr = s.accept()
        print 'client connected ip: <' + str(addr) + '>'
        t = threading.Thread(target=retr_file, args=('retr_thread', connection))
        t.start()

    s.close()

if __name__ == '__main__':
    Main()
