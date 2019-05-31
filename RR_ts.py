
# coding: utf-8

import numpy as np
from PIL import Image
from PIL import ImageFilter 
import glob
import os

def main():
    path = input ("Please enter path:\n")
    #path = "D:/RR_Test/dev_dataset"
    ImgList = []
    for file in glob.glob(path + "/*.jpg"):
        img = Image.open(file)
        ImgList.append(img)
        
    for img1 in ImgList:
        for img2 in ImgList:
            img1int = (np.array(img1.convert('L').resize((32,32), resample=Image.BICUBIC) 
                        .filter(ImageFilter.GaussianBlur(radius=3))) 
                        ).astype(np.int)  
            
            img2int = (np.array(img2.convert('L').resize((32,32), resample=Image.BICUBIC) 
                        .filter(ImageFilter.GaussianBlur(radius=3))) 
                        ).astype(np.int)   
            
            diff = np.abs(img1int - img2int).sum()
            if diff < 8000 and img1.filename != img2.filename:
                print (os.path.basename(img1.filename), os.path.basename(img2.filename))
        ImgList.remove(img1)

main()
input ('Press ENTER to exit')

