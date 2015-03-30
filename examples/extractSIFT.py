#!/usr/bin/python3
import os,platform,subprocess
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from tools.imtools import get_imlist

    
filename='25.jpg'
img=Image.open(filename)
img=img.convert('L')
im=np.array(img)
fea,locs=SIFTFeatures(filename,'tmp')
plot_features(im,locs,False)
