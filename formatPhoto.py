import cv2
import numpy
import constants as c
 
def fPh(img):

    h=img.shape[0]
    l=img.shape[1]
     
    if(l>h*c.Id):
        res=numpy.array([[img[i,j] for j in range(l) if j>(h*c.Id)//2 and j<(l-h*c.Id)//2] for i in range(h)])
    elif(l<h*c.Id):
        res=numpy.array([[img[i,j] for j in range(l) if i>(l/c.Id)//2 and i<(h-l/c.Id)//2] for i in range(h)])
    else:
        res=img

    return cv2.resize(res,(c.l,c.h),cv2.INTER_AREA)
