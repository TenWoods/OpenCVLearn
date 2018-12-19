import cv2
import numpy as np

clickCount = 0
point = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])

def mouseclick(event, x, y, flags, param):
    global clickCount
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clickCount += 1
        if clickCount < 4:
            point[clickCount] = (x, y)
        

img = cv2.imread('flowers.tif')
rows,cols,ch = img.shape
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
cv2.namedWindow('Input')
cv2.setMouseCallback('Input', mouseclick)
cv2.imshow('Input',img)
while True:
    cv2.imshow('Input',img)
    print(clickCount)
    if clickCount >= 4:
        break
    if cv2.waitKey(1)&0xFF == 27:
        break
M=cv2.getPerspectiveTransform(point,pts2)
dst=cv2.warpPerspective(img,M,(500, 362))
cv2.imshow('Output',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()