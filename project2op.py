#read image
import cv2
import mediapipe as mp
img = cv2.imread('d2.jpg')
cv2.imshow('img', img)

#detect faces
face = mp.solutions.face_detection
with face.FaceDetection(min =0 ,model=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)
    print(results.detections)
    
    for detection in results.detections:
        loction_data = detection.location_data
        relative_bounding_box = loction_data.relative_bounding_box
        h, w, c = img.shape
        x = int(relative_bounding_box.xmin * w)
        y = int(relative_bounding_box.ymin * h)
        width = int(relative_bounding_box.width * w)
        height = int(relative_bounding_box.height * h)
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.imshow('img', img)  
        
# #bulr faces
# #save image

import cv2
import mediapipe as mp
import numpy as np

# read image
img = cv2.imread('d2.jpg')

# detect faces
face = mp.solutions.face_detection

with face.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    # create empty mask (black image)
    mask = np.zeros_like(img)

    if results.detections:
        for detection in results.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            h, w, c = img.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            x, y = max(0, x), max(0, y)

            # draw white rectangle on mask (face area)
            cv2.rectangle(mask, (x, y), (x + width, y + height), (255, 255, 255), -1)

    # apply mask (show only faces)
    result = cv2.bitwise_and(img, mask)

# show results
cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Face Only', result)

# save output
cv2.imwrite('face_mask.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
