import cv2
import numpy as np
from HSV_similarity_detection import *

text_RGB_sample1=[[90,89,95],[87,86,92],[90,88,99],[84,85,88],[95,94,99],[86,87,89],[100,100,112],[91,90,96],[96,93,99],[81,80,88]]
text_RGB_sample2=[[204,202,221],[204,214,220],[190,203,213],[172,179,180],[190,196,208],[186,201,208],[192,195,210]]
text_HSV= np.vstack((avr_HSV(text_RGB_sample1),avr_HSV(text_RGB_sample2)))

image_name  = "0.jpg"
image_folder= "images/"
image_path = image_folder+image_name
loaded_image = cv2.imread(image_path)
is_background_black:bool=False
is_background_white:bool=False
Sensivity="center"
final_img,text_pixels=color_similarity_HSV(loaded_image,specific_colors=text_HSV,ideal_color=[0,0,255],distance=50,sensivity=Sensivity,limit_other_colors=True)

cv2.imshow("final",final_img)
cv2.waitKey(0)
cv2.imwrite(image_path[0:-4]+"_textcolor_extracted_replacingothers_"+Sensivity+image_path[-4:], final_img)
print(text_pixels)