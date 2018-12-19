import cv2
import numpy as np

img1 = cv2.imread('j_e.png')
img2 = cv2.imread('j_d.png')
img = cv2.imread('j.png')
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Out1', closing)
cv2.imshow('Out2', opening)
cv2.imshow('Out3', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()