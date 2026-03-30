# import os
# import cv2
# import numpy as np
# img = cv2.imread('d2.jpg',20)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_threshold = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# img_threshold_inv = cv2.threshold(img_gray, 88, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('img', img)
# cv2.imshow('threshold_image', img_threshold[1])
# cv2.imshow('threshold_image_inv', img_threshold_inv[1])
# cv2.waitKey(0)
# ################################
# import os
# import cv2
# import numpy as np
# img = cv2.imread('d3.jpg',20)
# ret ,img_threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('img', img)
# cv2.imshow('threshold_image', img_threshold[1])
# cv2.waitKey(0)
# ###################edge detection
import os
import cv2
import numpy as np
img = cv2.imread('d3.jpg',20)
edges = cv2.Canny(img, 100, 200)
cv2.imshow('img', img)
cv2.imshow('edges', edges)
cv2.waitKey(0)
dilated_edges = cv2.dilate(edges, None, iterations=1)
cv2.imshow('dilated_edges', dilated_edges)
cv2.waitKey(0)
############drwing contours
#line
import cv2
img = cv2.imread('d2.jpg',20)

cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 5)
cv2.imshow('line', img)
cv2.waitKey(0)
cv2.rectangle(img, (0, 0), (200, 200), (255, 0, 0), -1)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.circle(img, (200, 200), 50, (255, 0, 0), -1)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.putText(img, "OpenCV", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 5)
cv2.imshow("img", img)
cv2.waitKey(0)
from PIL import Image

img = Image.new("RGB", (200, 200), color="red")
img.show()