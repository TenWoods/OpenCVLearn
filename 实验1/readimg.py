import cv2
import numpy as np

img = cv2.imread('test1.jpg', 1)
sp = img.shape
print (sp)
cv2.line(img, (0, 0), (sp[1], sp[0]), (0, 0, 0), 10)
cv2.imshow('img', img)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('test2.jpg', img)
    cv2.destroyAllWindows()
