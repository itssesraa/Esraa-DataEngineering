import cv2 
import numpy as np
import pandas as pd
cap=cv2.VideoCapture(0)
print(cv2.__version__)
img =cv2.imread('d2.jpg',0)# 0 for grayscal ,1 for color 
print(img)
cv2.imshow('img', img)      
k = cv2.waitKey(500)
if k == 27:
    cv2.destroyAllWindows() 
elif k == ord('s'):
    cv2.imwrite('d2_copy.jpg', img)
    cv2.destroyAllWindows()    
cv2.waitKey(2500)    
############################################
cap = cv2.VideoCapture(0)    
    