#!/usr/bin/python3
#encoding=utf-8
'''
This example shows how to extract SIFT features from a directory containing images.
'''

import os
import numpy as np
from PIL import Image

from tools.imtools import getImlist
from descriptors import sift

def extractSIFT(imgsPath,featsOutPath):
    imgslist = getImlist(imgsPath)
    for idx, imgPath in enumerate(imgslist)
        fea,locs=SIFTFeatures(imgPath,featsOutPath)
        plot_features(im,locs,False)

if __name__=='__main__':
    imgsPath = 'testImages'
    featsOutPath = 'imgFeats'
    if not os.path.exists(featsOutPath):
        os.makedirs(featsOutPath)