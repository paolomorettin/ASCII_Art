
import Image

class ASCII_Art :

    greyscale_ascii = [' ','.','-',':','+','x','H','#']

    @classmethod
    def greyscale_process(cls,path,hDef,vDef,inverse=False) :
        image = Image.open(path)
        matrix = []
        width,height = image.size
        h_gap = width/hDef
        v_gap = height/vDef

        for i in xrange(vDef) :
            matrix.append([])
            for j in xrange(hDef) :
                gs_value = 0
                for x in range(j*h_gap,(j+1)*h_gap) :
                    for y in range(i*v_gap,(i+1)*v_gap) :                        
                        gs_value += sum(image.getpixel( (x,y) )[:3])/3
                matrix[-1].append( gs_value / (v_gap * h_gap) )

        gs_list = list(cls.greyscale_ascii)
        if inverse :
            gs_list.reverse()
        alen = len(gs_list)
        return map(lambda row : map(lambda elem : gs_list[int((elem/256.)*alen)] , row), matrix)

if __name__ == '__main__' :
    from sys import argv
    if len(argv) - 1 == 3 :
        matrix = ASCII_Art.greyscale_process(argv[1],int(argv[2]),int(argv[3]))
        for row in matrix : print ''.join(row)
    else :
        print "usage: python ASCII_Art.py image_path horizonal_def vertical_def"
        exit()
