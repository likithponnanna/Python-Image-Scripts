# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:59:58 2018

@author: likithponnanna

This code generates examplars, starting with a single image in the following way:
    
    1- will add gaussian blur - small amount   20%
    2- will add a small amount of S&P noise    20%
    3- will add both 1 and 2                   20%
    4- original data                           40%
                                         ________________
                                         1000 images in total
    
will scale the images down to 72 dpi, but are still readable

"""
import cv2
import numpy as np
import random
import imutils


def noise_generator (noise_type,image):

    row,col,ch= image.shape
    if noise_type == "gauss":       
        gauss_noise = [0.02, 0.03, 0.04, 0.05]
        mean = 0.0
        var = random.sample(gauss_noise, 1)
        sigma = var[0]**0.5
        gauss = np.array(image.shape)
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy.astype('uint8')
    
    elif noise_type == "s&p":
        s_vs_p = 0.5
        amount = 0.004
        out = image
        # Generate Salt '1' noise
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
        out[coords] = 255
        # Generate Pepper '0' noise
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
        out[coords] = 0
        return out
    
    elif noise_type == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    
    elif noise_type =="speckle":
        gauss = np.random.randn(row,col,1)
        gauss = gauss.reshape(row,col,1)        
        noisy = image + image * gauss
        print("NOISY dtype =", type(noisy), noisy.shape)
        return noisy
    
    else:
        return image



def inject_noise(img):
    
    WIDTH = 480 #768
    HEIGHT = 640 #128
    rnd = random.random()

    #rnd = 0.50
    
    if (rnd < 0.4):  # < 0.2
        #Gaussian noise generation
        img_GB = noise_generator("gauss", img)#   cv2.GaussianBlur(th2, (9,9),1)        
        gray = cv2.cvtColor(img_GB,cv2.COLOR_BGR2GRAY)
        thgauss2 = cv2.resize(gray, (WIDTH,HEIGHT), interpolation = cv2.INTER_AREA)  #imutils.resize(gray, width=WIDTH)       
        
        return thgauss2

    if (rnd >= 0.4 and rnd < 0.7): # >= 0.2 and  < 0.4  
    #Salt and pepper noise generator
        img_sp = noise_generator("s&p", img)#   cv2.GaussianBlur(th2, (9,9),1)        
        gray_sp = cv2.cvtColor(img_sp,cv2.COLOR_BGR2GRAY)
        thgauss2 = cv2.resize(gray_sp, (WIDTH,HEIGHT), interpolation = cv2.INTER_AREA)  #imutils.resize(gray, width=WIDTH)       

        return thgauss2

   
    if (rnd  >= 0.7 and rnd < 0.8): #>= 0.4 and < 0.8
     #original image resized down to 384x496 (AR = 0.77204...)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        thimage = cv2.resize(gray, (WIDTH,HEIGHT), interpolation = cv2.INTER_AREA)
        
        return thimage

  
    if (rnd >= 0.8):
        #Add small shear [-10..10] degrees max
        img_sh = imutils.rotate(img, -2)  #transform_image(image,ang_range,shear_range,trans_range,brightness=0)
        gray = cv2.cvtColor(img_sh,cv2.COLOR_BGR2GRAY)
        shimage = cv2.resize(gray, (WIDTH,HEIGHT), interpolation = cv2.INTER_AREA)
        return shimage

"""    
    #Poisson noise generator
    img_poisson = noise_generator("poisson", img)
    img_poisson = np.array(img_poisson, dtype=np.uint8)
    gray_poisson = cv2.cvtColor(img_poisson,cv2.COLOR_BGR2GRAY)
    ret2,thpoisson = cv2.threshold(gray_poisson,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thpoisson = imutils.resize(thpoisson, width=WIDTH)
    cv2.imwrite("E:\\DeepLearning\\Form_taxreturns\\IRS_FORMS\\IRS_1040_Schedule_A\\poisson_noise.jpg", thpoisson)
    
    #Speckle noise generator
    img_speckle = noise_generator("speckle", img)#   cv2.GaussianBlur(th2, (9,9),1)
    img_speckle = np.array(img_speckle, dtype=np.uint8)
    gray_speckle = cv2.cvtColor(img_speckle,cv2.COLOR_BGR2GRAY)
    ret2,thspeckle = cv2.threshold(gray_speckle,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thspeckle = imutils.resize(thspeckle, width=WIDTH)
    cv2.imwrite("E:\\DeepLearning\\Form_taxreturns\\IRS_FORMS\\IRS_1040_Schedule_A\\speckle_noise.jpg", thspeckle)
"""    
 
   

