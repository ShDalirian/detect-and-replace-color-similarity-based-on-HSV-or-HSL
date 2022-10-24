import numpy as np
import cv2

def color_similarity_HSV(img,specific_colors,ideal_color=[0,0,255],distance:int=15,sensivity:str="uniform",limit_other_colors:bool=False):
    center=np.array([img.shape[0]//2,img.shape[1]//2])
    converted_img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    text_pixel:int=0
    distance_effective:int=distance
    for y in range(converted_img.shape[0]):
        for  x in range(converted_img.shape[1]):
            dist=min(color_dist(converted_img[y,x],specific_colors)[0,:])
            delta=np.array([abs(y-center[0])/center[0],abs(x-center[1])/center[1]])
            match sensivity:
                case "around":
                    distance_effective=int(pow(max(delta[:]),3)*distance)
                case "center":
                    distance_effective=int(pow((1-(max(delta[:])/2)),3)*distance)
            if dist<=distance_effective:
                converted_img[y, x, 0:3]=ideal_color
                text_pixel +=1
            elif limit_other_colors:#if loaded_image[y, x, 0]<90 and  loaded_image[y, x, 1]<90 and loaded_image[y, x, 2]<90:
                # initalize empty list to stored difference between lists
                subtracted_list = []
                # iterating on iterator object return by zip() method
                for i,j in zip([180,255,255], ideal_color):
                    subtracted_list.append(i - j)
                converted_img[y, x, 0:3]=subtracted_list
    converted_img=cv2.cvtColor(converted_img, cv2.COLOR_HSV2BGR)
    return converted_img,text_pixel

def color_dist(picked_pixel,ideal_pixel):
    dist:float=np.zeros((1,ideal_pixel.shape[0]))
    for i in range(ideal_pixel.shape[0]):
        dist[0,i]:float=pow(pow(picked_pixel[0]-ideal_pixel[i][0],2)+pow(picked_pixel[1]-ideal_pixel[i][1],2)+pow(picked_pixel[2]-ideal_pixel[i][2],2),0.5)
    return dist

def avr_HSV(RGB_sample):
    RGB_sample_array1= np.uint8([RGB_sample])
    HSV_convert = np.zeros((RGB_sample_array1.shape[0],RGB_sample_array1.shape[1],3))
    HSV_convert = cv2.cvtColor(RGB_sample_array1,cv2.COLOR_RGB2HSV)
    text_color= np.zeros((1,3))
    for a1 in range(HSV_convert.shape[2]):
        text_color[0,a1]=np.average(HSV_convert[0,:,a1])
    return text_color  
