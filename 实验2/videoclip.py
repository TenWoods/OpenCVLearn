import cv2
import numpy as np

count = 0
str = ['???', '!!!!', 'wryyyyyy!', 'oraoraora!', 'mudamudamuda!', 'the world!', 'nani!']

def mouseclick(event, x, y, flags, param):
    global count,str
    if flags == cv2.EVENT_FLAG_LBUTTON:
        count += 1
        print('?')
        print(count)
        if count >= len(str):
            count = 0

cap1 = cv2.VideoCapture('vtest.avi')
cap2 = cv2.VideoCapture(0)
out = cv2.VideoWriter('mixoutput.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20.0, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX
while (cap2.isOpened()):
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
    if ret1 and ret2:
        cv2.setMouseCallback('video', mouseclick)
        if (cv2.waitKey(1)&0xFF == ord('c')):
            count += 1
            print(count)
            if count >= len(str):
                count = 0
        rows,cols,channels = img2.shape
        roi = img1[0:rows, 0:cols ]
        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask_front = cv2.threshold(img2gray, 130, 255, cv2.THRESH_BINARY)#获取背景遮罩
        mask_inv = cv2.bitwise_not(mask_front) #获取图案遮罩
        img1_bg = cv2.bitwise_and(roi, roi, mask = mask_front)
        img2_fg = cv2.bitwise_and(img2, img2, mask = mask_inv)
        dst = cv2.add(img1_bg, img2_fg)
        cv2.putText(dst, str[count], (10, 240), font, 2, (100, 130, 111), 2)
        cv2.putText(img2, str[count], (10, 240), font, 2, (100, 130, 111), 2)
        cv2.imshow('video', dst)
        cv2.imshow('compare', img2)
        out.write(dst)
    else:
        print('???')
        break
    if (cv2.waitKey(1)&0xFF == ord('q')):
        break
cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

