import os
import PIL
from PIL import Image

class ImageRename():
    def __init__(self):
        self.path = os.getcwd()

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 0

        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'img' + format(str(i), '0>3s') + '.jpg')
                os.rename(src, dst)
                i = i + 1

    def resize(self):
        filelist = os.listdir(self.path)
        i=0
        for item in filelist:
            if item.endswith('.jpg'):
                img=Image.open(item)
                img_resized=img.resize((768,576),PIL.Image.ANTIALIAS)
                img_resized.save('img'+format(str(i),'0>3s')+'.jpg')
                i=i+1



if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
    newname.resize()
