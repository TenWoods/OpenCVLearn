import cv2
import numpy as np

cap=cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])
while(1):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
    #res = cv2.morphologyEx(res, cv2.MORPH_GRADIENT, kernel)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:  
        #找到面积最大的轮廓  
        c = max(cnts, key = cv2.contourArea) 
        rect = cv2.minAreaRect(c) 
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0,0, 255), 3)
    cv2.imshow('res', res)
    cv2.imshow('frame',frame)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
cv2.destroyAllWindows()