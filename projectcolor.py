import cv2
from matplotlib import image
import numpy
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask =cv2.inRange(hsvimage, (0, 100, 100), (10, 255, 255))
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
def get_limtits(color):
    if color == 'red':
        lower = (0, 100, 100)
        upper = (10, 255, 255)
    elif color == 'green':
        lower = (50, 100, 100)
        upper = (70, 255, 255)
    elif color == 'blue':
        lower = (110, 100, 100)
        upper = (130, 255, 255)
    else:
        raise ValueError("Unsupported color")
    return lower, upper

mask = cv2.inRange(hsvimage, get_limtits('red')[0], get_limtits('red')[1])
cv2.imshow('mask', mask)
bbox = cv2.boundingRect(mask)
x, y, w, h = bbox   
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('frame', frame)      
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask =cv2.inRange(hsvimage, (0, 100, 100), (10, 255, 255))
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
        

