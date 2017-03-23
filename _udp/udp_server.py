import socket

def Main():
    host = '192.168.1.130'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print 'Server started. '

    while True:
        data, addr = s.recvfrom(1024)
        print 'Message from: ' + str(addr)
        print 'From connected user: ' + str(data)

        # response
        data = str(data).upper()

        print 'Sending ' + str(data)
        s.sendto(data, addr)
    s.close()

if __name__ == '__main__':
    Main()