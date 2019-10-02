import cv2
import imutils
import numpy as np
import os
import argparse

class PreProces:
    def illumination_correctionimg(self,img):
        ILLUMINATION = np.mean(img)
        
        if ILLUMINATION > 245:
            ALPHA = 1.8
            BETA = -140
        elif ILLUMINATION > 240 and ILLUMINATION < 245:
            ALPHA = 2.1
            BETA = -160
        elif ILLUMINATION > 200 and ILLUMINATION < 240:
            ALPHA = 2.6
            BETA = -110
        elif ILLUMINATION < 200:
            ALPHA = 2.3
            BETA = -130
        else:
            ALPHA = 2.0
            BETA = -160
        
        img = ALPHA * img + BETA   
        img = np.clip(img, 0, 255).astype(np.uint8)
        img = cv2.equalizeHist(img)

        return img


    def remove_heavy_specles(self,img):
        kernel = np.ones((2,2),np.uint8)
        invert_image_og = cv2.bitwise_not(img)
        #print("Here")
        
        opening_remove_specles = cv2.morphologyEx(invert_image_og, cv2.MORPH_OPEN, kernel, iterations = 1)
        invert_to_threshold = cv2.bitwise_not(opening_remove_specles)
        
        # blur_to_threshold = cv2.GaussianBlur(img , (11, 11), 0)
        # adaptive_threshold = cv2.adaptiveThreshold(blur_to_threshold,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        #                                         cv2.THRESH_BINARY,21,2)
        
        adaptive_threshold = self.adaptive_equalization(invert_to_threshold)

        cv2_subt = cv2.subtract(adaptive_threshold,img)
        invert_noise_mask = cv2.bitwise_not(img)
        denoised_image = cv2.subtract(invert_noise_mask,cv2_subt)
        invert_denoised_image = cv2.bitwise_not(denoised_image)
        
        image = invert_denoised_image
        
        return image

    def remove_saltpepper_noise(self,image):
        image= cv2.medianBlur(image,3)
        ret3,image = cv2.threshold(image,0,255,cv2.THRESH_TOZERO)
        return image

    def adaptive_equalization(self,img):
        blur_to_threshold = cv2.GaussianBlur(img , (11, 11), 0)
        adaptive_threshold = cv2.adaptiveThreshold(blur_to_threshold,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                cv2.THRESH_BINARY,21,2)
        return adaptive_threshold
    

parser = argparse.ArgumentParser()
image_pre_process = PreProces()
parser.add_argument("--image", "-i", required = True, help = "Path to input image")
args = parser.parse_args()

print("Input Image Path is: " + args.image)

image_path = args.image

directory = 'IMG_PREPROCESS_OUTPUT'
if not os.path.exists(directory):
    os.makedirs(directory)

imread = cv2.imread(args.image,0)

cv2.imwrite("IMG_PREPROCESS_OUTPUT/00_Original_Image.png",imread)


illumination_correction = image_pre_process.illumination_correctionimg(imread)
cv2.imwrite("IMG_PREPROCESS_OUTPUT/01_Illumination_Correction.png",illumination_correction)


heavy_specles_removal = image_pre_process.remove_heavy_specles(illumination_correction)
cv2.imwrite("IMG_PREPROCESS_OUTPUT/02_Heavy_Specle_Removal.png",heavy_specles_removal)



salt_pepper_noise_removal = image_pre_process.remove_saltpepper_noise(heavy_specles_removal)
cv2.imwrite("IMG_PREPROCESS_OUTPUT/03_Salt_Pepper_Noise.png",salt_pepper_noise_removal)

print("====================================================================================")
print("Output Images Stored in IMG_PREPROCESS_OUTPUT folder under current working directory")





    