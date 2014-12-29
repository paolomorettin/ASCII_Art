import os
from PIL import Image,ImageDraw,ImageFont

class ASCII_Image :
    greyscale_ascii = [' ','.',"'",'"','-',':','~','=','+','x','%','$','H','Z','X','#','@']
    default_font_path = os.path.dirname(os.path.abspath(__file__)) + "/data/DroidSansMono.ttf"

    @staticmethod
    def openImage(path) :
        '''
        This just wraps "Image.open"

        '''
        return Image.open(path)

    @staticmethod
    def saveImage(image,path) :
        '''
        Another wrapper for saving images.

        '''
        image.save(path)

    @staticmethod
    def textToImage(frame,width,fontsize = None,fg_color=(255,255,255),bg_color=(0,0,0)) :
        '''
        Converts an ASCII-art frame into a PIL Image. If no fontsize is passed, it determines the best-fitting
        size with a binary search. Returns the image and the fontsize for future uses.
        
        Params:
        frame - an ASCII-art frame
        width - the desired image width (in pixels). (Note: height is automatically determined)
        (OPTIONAL)
        fontsize - this parameter can be used to compute the best-fitting size just once.
        fg_color - text color in BGR.
        bg_color - background color in BGR.

        '''
        

        if fontsize == None :
            # initial font size
            bounds = [1, width * 2]
            fontsize = bounds[0] + int((bounds[1]-bounds[0])/2.)
            font = ImageFont.truetype(ASCII_Image.default_font_path, fontsize)
            # calculate the right font size to fit the image width, using a binary search
            first_row = ''.join(frame[0])
            while bounds[1] - bounds[0] > 2 :
                if font.getsize(first_row)[0] > width :
                    bounds[1] = fontsize
                else :
                    bounds[0] = fontsize
                fontsize = bounds[0] + int((bounds[1]-bounds[0])/2.)
                font = ImageFont.truetype(ASCII_Image.default_font_path, fontsize)
        else :
            font = ImageFont.truetype(ASCII_Image.default_font_path, fontsize)

        height = len(frame) * fontsize
        image = Image.new("RGB", (width,height), bg_color)
        draw = ImageDraw.Draw(image)
        
        for i in range(len(frame)) :
            draw.text((0, i*fontsize), ''.join(frame[i]), fg_color, font=font)        

        return image,fontsize

    @classmethod
    def greyscaleProcess(cls,image,hDef,vDef,inverse=False,normalize=False) :
        '''
        This converts a PIL image into a matrix (list of lists) of ASCII characters, selected according to the
        average greyscale value of each corresponing region.
        
        Params:
        image - the image to be processed (PIL Image type)
        hDef - how many characters for each line
        vDef - how many lines
        (OPTIONAL)
        inverse - boolean, reverse greyscale value
        normalize - boolean, normalize the averaged grayscale values

        '''
        # Converts the image to greyscale
        image = image.convert('L')

        # Resizes the image
        pixels = list(image.resize((hDef,vDef),Image.ANTIALIAS).getdata())
        matrix = [ pixels [i * hDef : (i + 1) * hDef - 1] for i in xrange(vDef)]
   
        gs_list = list(cls.greyscale_ascii)

        if inverse :
            gs_list.reverse()

        if normalize :
            gs_min = min([min(r) for r in matrix])
            gs_max = max([max(r) for r in matrix])
            if gs_max > 0 :
                matrix = [map(lambda x : int((float(x - gs_min)/gs_max)*255) , r) for r in matrix]
        alen = len(gs_list)
        return map(lambda row : map(lambda elem : gs_list[int((elem/256.)*alen)] , row), matrix)







