'''
Small example of ASCII_Image usage.
Reads an image and prints it to console.

'''

if __name__ == '__main__' :

    import sys,os
    sys.path.insert(1, os.path.join(sys.path[0], '..'))

    from ASCII_Image import * 

    
    input_path = sys.argv[1] if len(sys.argv) == 2 else 'example_image.jpg'
    image = ASCII_Image.openImage(input_path)
    # parameters to play with
    rows = 40
    columns = 80
    inverse = False
    normalize = False
    for line in ASCII_Image.greyscaleProcess(image,columns,rows,inverse=inverse,normalize=normalize) :
        print ''.join(line)
