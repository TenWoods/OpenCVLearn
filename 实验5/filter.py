import cv2
import numpy as np

img = cv2.imread('lenawithnoise.png')
kernel = np.ones((5,5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('ori', img)
cv2.imshow('res', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()