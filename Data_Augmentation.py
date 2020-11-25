# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:43:23 2018

@author: bipolarbrain

This code will generate N examplars for each file in the Input_Images folder - each file
will be labelled:  set1-{0000}.jpg
"""

import os
import string
import cv2
import numpy as np
import PIL
import math
import random
import pickle
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import scipy.misc
import time
from skimage.util import random_noise
from scipy.ndimage import filters
import imutils
import importlib
import time
import glob

import aim_prepare_exemplarsv1


start = time.time()
cv2.setUseOptimized(True)

input_dir = r'C:\Users\lbelliappa\Downloads\Logo detection\Wells_Fargo\Wells_Fargo_Processed'
data_dir = r'C:\Users\lbelliappa\Downloads\Logo detection\Wells_Fargo\Wells_Fargo_Processed\TestNoise'


#if not os.path.exists(data_dir):
#    os.makedirs(data_dir)
#############################################################
random.seed(-99)

#print("Current dir = ", current_dir + '/')
print("Input dir =",input_dir + '/' )
print("Data dir =",data_dir + '/' )


doctypes_label_dict = {}

label_value = 0

filenames = os.listdir(input_dir)

cd = os.getcwd()

sub_folder = []
for i in range(0,60):
    sub_folder.append('%03d' %i)

main_folder = input_dir+"/"

for t in sub_folder:
	f = main_folder+t+"/"
	os.chdir(f)
	images = glob.glob("*.png")
	os.mkdir(data_dir+"/"+str(t))
	os.chdir(cd)
	i = 0
	N = math.ceil(int(700/len(images)))
	for image in images:
		t_image = image
		image = main_folder+t+"/"+image
		for i in range(N):
			img = cv2.imread(image)
			img1  = aim_prepare_exemplarsv1.inject_noise(img)
			new_name = data_dir+"/"+str(t)+"/"+t_image.split(".png")[0]+"-"+str(i)+".png"
			cv2.imwrite(new_name,img1)
		i+=1
end = time.time()
print("Time taken: "+ str(end-start))

	
