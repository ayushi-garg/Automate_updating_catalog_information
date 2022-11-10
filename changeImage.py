#!/usr/bin/python3

from PIL import Image
import glob
for img in glob.glob('/home/student-02-a90500197f9a/supplier-data/images/*.tiff'):
    im = Image.open(img)
    #print(str(img)[7:])
    im.resize((600,400)).convert('RGB').save(img[:-4]+"jpeg",'JPEG')
