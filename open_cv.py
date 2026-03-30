import cv2 
import os 
from matplotlib import image
import numpy
#image read
image_path = os.path.join('', 'python','d2.jpg')
img = cv2.imread('d2.jpg')
#image write
# cv2.imwrite('output.jpg', img)
#visulazie image
# cv2.imshow('image',img)
# cv2.waitKey(0)
# resize_img =cv2.resize(img, (300, 300))
# cv2.imshow('resized_image', resize_img)
# cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
cv2.imshow('gray_image', img_gray)
cv2.imshow('rgb_image', img_rgb)
cv2.waitKey(0)
#######################################
# ret = True
# while ret:
#     ret, frame = video.read()
#     if ret:
#         cv2.imshow('frame', frame)
#         cv2.waitKey(1)
video = cv2.VideoCapture(0)
#
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
cv2.imshow('gray_image', img_gray)
cv2.imshow('rgb_image', img_rgb)
cv2.waitKey(0)