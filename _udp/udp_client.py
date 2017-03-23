import socket

def Main():
    host = '192.168.1.130'
    port = 5001

    server = ('192.168.1.130', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = raw_input('-> ')

    while message != 'q':
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)

        print 'Received from server: ' + str(data)

        message = raw_input('-> ')

    s.close()

if __name__ == '__main__':
    Main()