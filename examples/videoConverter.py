'''
Small example of ASCII_Video usage.
Reads a video and converts every frame in ASCII art.

'''

if __name__ == '__main__' :

    import sys,os
    sys.path.insert(1, os.path.join(sys.path[0], '..'))

    from ASCII_Video import * 
    if len(sys.argv) != 3 :
        print "USAGE: python {} input_file output_file".format(os.path.basename(__file__))
        exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # parameters to play with
    step = 1
    cols = 160
    rows = 60
    inverse = False
    normalize = False
    ascii_frames = ASCII_Video.getVideoFrames(input_path,step=step,preprocess=(cols,rows,inverse,normalize))
    
    # more parameters to play with
    width = 1000
    fps = 32
    fg = (255,255,255)
    bg = (0,0,0)
    codec = 'XVID'
    ASCII_Video.asciiToVideo(ascii_frames,output_path,width,fps,fg_color=fg,bg_color=bg,codec=codec)
