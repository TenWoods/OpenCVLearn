import cv2
import numpy as np

drawing = False
mode = True
ix,iy = -1,-1

def mouseclick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 120, 0), -1)
            else:
                cv2.circle(img, (x, y), 3, (255, 120, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img', draw)
while True:
    cv2.imshow('img', img)
    if cv2.waitKey(1)&0xFF == 27:
        break
    elif cv2.waitKey(1)&0xFF == ord('m'):
        mode = not mode
cv2.destroyAllWindows()
