import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from meta_data import *

def main():
    
    #sorting_images()                 # "please un-comment before running and delete day, night folders"              
    org_day4 = cv.imread('./day/IMG_20210705_162255056.jpg')
    org_day5 = cv.imread('./day/IMG_20210705_162259482.jpg')
    org_night4 = cv.imread('./night/IMG_20210705_194445280.jpg')
    org_night5 = cv.imread('./night/IMG_20210705_194445467.jpg')
    original_image_difference(org_day4, org_day5)
    original_image_difference(org_night4, org_night5)
    smooth_day4, smooth_day5 = bilateralFilter(org_day4, org_day5)
    smooth_night4, smooth_night5 = bilateralFilter(org_night4, org_night5)
    after_smoothing_difference(smooth_day4, smooth_day5)
    after_smoothing_difference(smooth_night4, smooth_night5)


if __name__ == "__main__":
    main()