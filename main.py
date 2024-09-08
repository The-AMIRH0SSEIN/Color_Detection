#importing the modules
import cv2
import numpy as np
from PIL import Image

#camera 
#also you can use another index for imput camera(use 0 if you use your webcam)
cap = cv2.VideoCapture(0)

color_detection = None
low_blue = np.array([100, 150, 0])
up_blue = np.array([140, 255, 255])

low_green = np.array([55, 100, 50])
up_green = np.array([75, 255, 255])
while (True):
    ret,frame = cap.read()
    if (not ret):
        break
    HSV_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #conver bgr to hsv    
    blue_mask = cv2.inRange(HSV_frame, low_blue, up_blue)
    green_mask = cv2.inRange(HSV_frame, low_green, up_green)
 


    #convert to pillow format and detecting the bounding box
    Pil_b_mask = Image.fromarray(blue_mask)
    blue_boundingbox = Pil_b_mask.getbbox()

    Pil_g_mask = Image.fromarray(green_mask)
    green_boundingbox = Pil_g_mask.getbbox()
    print(f'blue {blue_boundingbox}')
    print(f'green {green_boundingbox}')
    if(blue_boundingbox != None):
        xb1 , yb1 , xb2 , yb2 = blue_boundingbox
        cv2.rectangle(frame,(xb1,yb1),(xb2,yb2),(255,0,0) , 2)
        cv2.putText(frame,"blue", (xb1, yb1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    if(green_boundingbox != None):
        xg1 , yg1 , xg2 , yg2 = green_boundingbox
        cv2.rectangle(frame,(xg1,yg1),(xg2,yg2),(0,255,0) , 2)
        cv2.putText(frame,"green", (xg1, yg1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Color Detection', frame)
    cv2.imshow('blue Detection', blue_mask)
    cv2.imshow('green Detection', green_mask)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()