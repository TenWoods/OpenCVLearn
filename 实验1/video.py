import numpy as np 
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('outputtest.avi', fourcc, 20.0, (640, 480))
while (cap.isOpened()):
    ret,frame = cap.read() #ret表示是否读取成功
    if ret == True:
        #frame = cv2.flip(frame, 0) #沿x轴翻转
        out.write(frame)
        cv2.imshow('frame', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
out.release()
cv2.destroyAllWindows()