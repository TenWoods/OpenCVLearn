import cv2
import numpy as np

isClick = True

def mouseclick(event, x, y, flags, param):
    global isClick
    if event == cv2.EVENT_LBUTTONDBLCLK:
        isClick = not isClick

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow('video')
cv2.setMouseCallback('video', mouseclick)
while (cap.isOpened()):
    cv2.setMouseCallback('video', mouseclick)
    ret,frame = cap.read()
    if ret == True:
        if isClick == True:
            cv2.putText(frame, 'zimu', (240, 240), font, 5, (100, 130, 111), 2)
        cv2.imshow('video', frame)
        out.write(frame)
    if (cv2.waitKey(1)&0xFF == ord('q')):
        break
cap.release()
out.release()
cv2.destroyAllWindows()


