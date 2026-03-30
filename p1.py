
import cv2
import numpy as np
img =np.zeros((600,900,3),dtype=np.uint8)
#background 
cv2.rectangle(img,(0,0),(900,500),(255,255,85),-1)
cv2.rectangle(img,(0,500),(900,600),(75,180,70),-1)
#sun
cv2.circle(img, (200, 150), 60, (0,255,255), -1)
cv2.circle(img, (200, 150), 75, (220, 255, 255), 8)
#tree stem
cv2.line (img, (710, 500), (710, 420), (30, 65, 115), 15)
#tree leaves

#tree leafs
cv2.line (img, (690, 420), (730, 420), (30, 65, 115), 15) 
trinanlage2=np.array([[690, 420], [730, 420], [710, 350]])
cv2.fillPoly(img, [trinanlage2], (75, 180, 70))
#tree
cv2.line(img, (690, 420), (730, 420), (30, 65, 115), 15)
cv2.fillPoly(img, [trinanlage2], (75, 180, 70))

print(img)
cv2.imshow('img', img)
x = cv2.waitKey(0)
