#Simple File Server
Taking what I learned about reading socket connections, Here's a basic command-line file server using TCP.

##Notes

##Relevant Links
- [Compression with PIL and StringIO](http://stackoverflow.com/questions/30771652/how-to-perform-jpeg-compression-in-python-without-writing-reading): Use the last comment's technique,
    - Using BytesIO object as a buffer, do JPG formatting using PIL, then save out to file (or write)
- [Using Numpy to encode images into byte string](http://stackoverflow.com/questions/17967320/python-opencv-convert-image-to-byte-string): potentially a solution for storing and streaming images over socket.
- [Fastest way to check if a value exists in a list or string](http://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list)
- [Pillow: Filter an iImage](http://pillow.readthedocs.io/en/3.4.x/reference/ImageFilter.html#example-filter-an-image)
    - EXAMPLE: (after importing Image, ImageFilter, cv2, numpy as np)
        - img = Image.open('file.jpg')
        - filtered = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
        - iar = np.asarray(filtered)
        - iar = iar[:,:,::-1]
        - cv2.imwrite('outputfile.jpg', iar)
        
- [Proper way to convert from CV2 to PIL](http://stackoverflow.com/questions/13576161/convert-opencv-image-into-pil-image-in-python-for-use-with-zbar-library)
    - Steps:
        - cv2 capture
        - convert from BGR to RGB
        - create PIL image with Image.fromarray (as CV2 images are numpy arrays))
        - (do what you need in PIL format, like unsharpmask, etc)
        
- [Serialize image data to send over Sockets using Pickle](http://stackoverflow.com/questions/7107075/sending-and-receiving-arrays-via-sockets): 
    - EXAMPLE:
        - To encode from server: dump = pickle.dumps(iar), returns a binary stream.
        - To decode from client: load = pickle.loads(dump), returns the image array.
    - Notes:
        - [Using BytesIO]https://docs.python.org/2/library/io.html