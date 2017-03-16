#Simple File Server
Taking what I learned about reading socket connections, Here's a basic command-line file server using TCP.

##Notes

##Relevant Links
- [Compression with PIL and StringIO](http://stackoverflow.com/questions/30771652/how-to-perform-jpeg-compression-in-python-without-writing-reading): Use the last comment's technique,
    - Using BytesIO object as a buffer, do JPG formatting using PIL, then save out to file (or write)
- [Using Numpy to encode images into byte string](http://stackoverflow.com/questions/17967320/python-opencv-convert-image-to-byte-string): potentially a solution for storing and streaming images over socket.