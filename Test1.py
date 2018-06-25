import numpy as np
import cv2

#load image
img = cv2.imread('Lenna.png',0)

cv2.imshow('This is Lenna',img)

pressedKey = cv2.waitKey(0)

if pressedKey == 27:
    cv2.destroyAllWindows()
elif pressedKey == ord('s'):
    cv2.imwrite('grey.png',img)    
    cv2.destroyAllWindows()
