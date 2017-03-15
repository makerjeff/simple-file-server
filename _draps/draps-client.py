import socket
from custom_colors import bcolors

def Main():
    host = '127.0.0.1'  # server ip
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input('Filename? -> ')

    if filename != 'q':
        s.send(filename)

        data = s.recv(1024)

        if data[:6] == 'EXISTS':
            filesize = long(data[6:])

            message = raw_input('File Exists, ' + str(filesize) + ' bytes, download? (Y/N)-> ')

            if message == 'Y':
                s.send('OK')
                f = open('new_' + filename, 'wb')

                data = s.recv(1024)

                total_received = len(data)

                f.write(data)

                while total_received < filesize:
                    data = s.recv(1024)
                    total_received += len(data)
                    f.write(data)
                    print "{0: .3f}".format((total_received/float(filesize))*100) + '% Done'

                print "Download complete!"
        else:
            print 'File does not exist!'

    s.close()

if __name__ == '__main__':
    Main()
