import Image
import numpy
import cv2
from ASCII_Image import ASCII_Image
from time import sleep

class ASCII_Video :

    out_video_extension = '.avi'

    @staticmethod
    def asciiToVideo(frames,path,width,fps,fg_color=(255,255,255),bg_color=(0,0,0),codec='XVID') :
        '''
        Given a list of ASCII-art frames, produces a video.
        
        Params:
        frames - list of ASCII-art frames.
        path - of the output file
        width - desired video width (in pixels)
        fps - desired framerate
        (OPTIONAL)
        fg_color - BGR values for the text
        bg_color - BGR values for the background
        codec - string representing the codec to use (see http://fourcc.org/codecs.php)

        '''
        image,fontsize = ASCII_Image.textToImage(frames[0],width,fg_color=fg_color,bg_color=bg_color)

        fourcc = cv2.cv.CV_FOURCC(*codec)
        video = cv2.VideoWriter(path + ASCII_Video.out_video_extension, fourcc, fps, image.size)
        image = numpy.array(image)
        video.write(image)
        
        i = 1
        for f in frames[1:] :
            i += 1
            image,_ = ASCII_Image.textToImage(f,width,fontsize=fontsize,fg_color=fg_color,bg_color=bg_color)
            image = numpy.array(image)
            video.write(image)

        # is it useful?
        #video.release()

    @staticmethod
    def dump(path,frames) :
        '''
        Writes a list of ASCII-art frames as a textfile.

        Params:
        path - of the output file
        frames - the list

        '''
        with open(path,'w') as f :
            s_frames = []
            for frame in frames :
                s_frame = ''
                for row in frame :
                    s_frame += ''.join(row) + '\n'
                s_frames.append(s_frame)
            f.write('\n'.join(s_frames))

    @staticmethod
    def open(path) :
        '''
        Reads a textfile containing a list of ASCII-art frames, as written by the dump.

        Params:
        path - of the input file

        '''
        with open(path,'r') as frame_file :
            frames = []
            for f in frame_file.read().split('\n\n') :
                frames.append(map(list,f[:-1].split('\n')))
            return frames
                
    @staticmethod
    def getVideoFrames(path,step=1,preprocess=None) : 
        # NOTE: Online preprocessing of each frame is advised. This should be implemented in order to deal with big video files.
        '''
        Extracts a list of frames (PIL Images) from a video file.

        Params:
        path - of the input video file
        (OPTIONAL)
        step - takes one frame every 'step' frames
        preprocess - tuple of parameters (n.cols,n.rows,inverse,normalize) for the greyscaleProcess function. Online preprocessing of each frame.

        '''
        vc = cv2.VideoCapture(path)
        c=0
        frames = []

        if preprocess != None :
            cols,rows,inv,norm = preprocess

        if vc.isOpened():
            rval , frame = vc.read()
            frame = Image.fromarray(frame) if preprocess == None else ASCII_Image.greyscaleProcess(Image.fromarray(frame),cols,rows,inverse=inv,normalize=norm)
            frames.append(frame)
        else:
            rval = False
        while rval:
             rval, frame = vc.read()
             if c % step == 0 and rval :
                 frame = Image.fromarray(frame) if preprocess == None else ASCII_Image.greyscaleProcess(Image.fromarray(frame),cols,rows,inverse=inv,normalize=norm)
                 frames.append(frame)
             c = c + 1
        vc.release()
        return frames





