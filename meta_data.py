## Importing the reqiured libraries
import os
import shutil
from datetime import datetime
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL.ExifTags import TAGS

# Function for sorting the given images according to day time and night time 
def sorting_images():

    os.mkdir("./day")
    os.mkdir("./night")

    images = os.listdir("./Photos/")       

    for i in images:

        im = Image.open("./Photos/" + i)            #opening the image
        im_exif_data = im.getexif()                 #extracting meta-data
        im.close()                                  #closing the image

        for ids in im_exif_data:
            if TAGS.get(ids, ids) == 'DateTime':                                    #acessing the date and time
                im_time = im_exif_data.get(ids)
                datetime_obj = datetime.strptime(im_time, "%Y:%m:%d %H:%M:%S")      #matching the date-time format
                time = datetime_obj.time()

                if time.hour >= 19 and time.minute > 30:                            #condition for after 7.30pm
                    shutil.move("./Photos/" + i, "./night/" + i)                    #moving into night folder
                else:
                    shutil.move("./Photos/" + i, "./day/" + i)                      #moving into day folder


#Funcion for Absolute difference between original images 4 and 5 
def original_image_difference(image4, image5):                                  

    image_difference = cv.absdiff(image4, image5)

    plt.imshow(image_difference), plt.title('Original Image Difference')
    plt.xticks([]), plt.yticks([])
    plt.show()

#Function for smoothing the images using bilateral filter 
def bilateralFilter(image4, image5):

    smooth_image4 = cv.bilateralFilter(image4,20,150,150) 
    smooth_image5 = cv.bilateralFilter(image5,20,150,150) 
    
    plt.imshow(smooth_image4), plt.title('Smoothing output')
    plt.xticks([]), plt.yticks([])
    plt.show()
    
    plt.imshow(smooth_image5), plt.title('Smoothing output')
    plt.xticks([]), plt.yticks([])
    plt.show()
    
    return smooth_image4, smooth_image5

#Function for Absolute difference between the smoothened images  
def after_smoothing_difference(photo4, photo5):

    image_difference = cv.absdiff(photo4, photo5)

    plt.imshow(image_difference), plt.title('After Smoothing Difference')
    plt.xticks([]), plt.yticks([])
    plt.show()


