import cv2
import numpy as np

img = cv2.imread('lenawithnoise.png')
median = cv2.medianBlur(img, 5)
gauss = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('median', median)
cv2.imshow('gauss', gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()