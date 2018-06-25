import numpy as np
import cv2

#load image


img = cv2.imread('Lenna.png',-1)

cv2.imshow('This is Lenna',img)

rect =cv2.rectangle(img,(255,255),(275,275),(225,255,0),3)

circ =cv2.circle(img,(290,290),100,(205,205,255),3)

line =cv2.line(img,(345,265),(365,285),(225,255,0),3)

row,col,chan = img.shape

rot = cv2.getRotationMatrix2D((256,256),90,1)

im2 = cv2.warpAffine(rect,rot,(512,512))

cv2.imshow('This is Lenna',im2)

while True:
    a = cv2.waitKey(0)

    print (a)
    #press d to rotate
    if a==100:
        print("Hello")
        rot = cv2.getRotationMatrix2D((256,256),90,1)

        im2 = cv2.warpAffine(im2,rot,(512,512))

        cv2.imshow('This is Lenna',im2)

pressedKey = cv2.waitKey(0)

if pressedKey==27:
    print("exit")
    
pressedKey = cv2.waitKey(1000)

cv2.destroyAllWindows()
