import constants as c
import cv2
import formatPhoto as fPh


img=cv2.imread('van.jpg')


#res_img=fPh.fPh(img)
res_img=img

for i in range(c.h):
    for j in range(c.l):
        (b,g,r) = res_img[i,j]
        print(c.colors[((b+g+r)//3)//15],end='')
    print('')