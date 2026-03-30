import cv2
import numpy as np

# create image
img = np.zeros((600, 900, 3), dtype=np.uint8)

# sky
cv2.rectangle(img, (0, 0), (900, 500), (255, 255, 120), -1)

# ground
cv2.rectangle(img, (0, 500), (900, 600), (60, 180, 75), -1)

# sun
cv2.circle(img, (150, 120), 50, (0, 255, 255), -1)
cv2.circle(img, (150, 120), 65, (0, 255, 255), 3)

# clouds
cv2.circle(img, (400, 100), 30, (255, 255, 255), -1)
cv2.circle(img, (430, 100), 30, (255, 255, 255), -1)
cv2.circle(img, (460, 100), 30, (255, 255, 255), -1)

# tree function
def draw_tree(x):
    # trunk
    cv2.line(img, (x, 500), (x, 430), (30, 65, 115), 15)
    
    # leaves (triangle)
    pts = np.array([[x-30, 430], [x+30, 430], [x, 360]])
    cv2.fillPoly(img, [pts], (60, 180, 75))

# draw multiple trees
draw_tree(700)
draw_tree(600)
draw_tree(800)

# house base
cv2.rectangle(img, (300, 400), (450, 500), (180, 120, 70), -1)

# roof
roof = np.array([[300, 400], [450, 400], [375, 320]])
cv2.fillPoly(img, [roof], (50, 50, 200))

# door
cv2.rectangle(img, (360, 450), (390, 500), (0, 0, 0), -1)

# windows
cv2.rectangle(img, (320, 420), (350, 450), (255, 255, 255), -1)
cv2.rectangle(img, (400, 420), (430, 450), (255, 255, 255), -1)

# flowers
for i in range(50, 900, 80):
    cv2.circle(img, (i, 550), 5, (0, 0, 255), -1)

# show image
cv2.imshow("Beautiful Scene", img)
cv2.waitKey(0)
cv2.destroyAllWindows()