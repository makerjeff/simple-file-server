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
- JPG save quality:
    - cv2.imwrite('img_CV2_90.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
- [List Directories in Python](http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory)
    - use 'os' module, os.listdir() will returns the RELATIVE path of all files listed, vs glob.glob() will return path based on input pattern.
- [Python get file size](http://stackoverflow.com/questions/6591931/getting-file-size-in-python): 
    - os.path.getsize(path)
- Numpy 'dtype = np.uint8' is required for CV2 image viewing.  This is what CV2 images are.
- [Python Serial Port Communication](https://tungweilin.wordpress.com/2015/01/04/python-serial-port-communication/)
- [Scaling Images in Python CV2](http://docs.opencv.org/trunk/da/d6e/tutorial_py_geometric_transformations.html)
    - height, width = img.shape[:2]
    - res = cv2.resize(img, (2*width, 2*height). interpolation=cv2.INTER_NEAREST) (or cv2.INTER_CUBIC))
- [String Formatting](https://pyformat.info/) Using '{}'.format()
- Successful JWX Image sending protocol:
    - CLIENT connects to SERVER.
    - CLIENT sends 'OK' to SERVER.
    - SERVER sends 'FD, str(filesize), filename.ext'.
    - CLIENT parses FD (file data) response and sends 'GO' to SERVER when ready.
    - SERVER begins sending binary data.
    - 'FS######' = File size response from Server.'
- [Python ArgParse module for command line flags parsing. ](https://docs.python.org/2/library/argparse.html#module-argparse)
- [NumPy Data Types](https://docs.scipy.org/doc/numpy/user/basics.types.html)
- [**Numpy Input and Output** (important!)](https://docs.scipy.org/doc/numpy/reference/routines.io.html): Save a numpy array to a file on disk.
- [THIS ONE WORKS: CV2 to Binary](http://stackoverflow.com/questions/17967320/python-opencv-convert-image-to-byte-string) Using np.imencode to create a jpg-encoded buffer, write to any open file.
    - to encode:
        - img_str = cv2.imencode('.jpg', img)[1].tostring()
            - img_str then can be saved to a file via open('filename.ext', 'wb')
    - To decode:
        - nparr = np.fromstring(file/buffer.read(), dtype=np.uint8)
        - img = cv2.imdecode(nparr)
- [OpenCV 3.0.0](http://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html): Reference for imdecode.
     