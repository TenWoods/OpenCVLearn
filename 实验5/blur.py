import cv2
import numpy as np

img = cv2.imread('lenawithnoise.png')
blur3 = cv2.blur(img, (3, 3))
blur5 = cv2.blur(img, (5, 5))
blur7 = cv2.blur(img, (7, 7))
cv2.imshow('res', blur3)
cv2.waitKey(0)
cv2.imshow('res', blur5)
cv2.waitKey(0)
cv2.imshow('res', blur7)
cv2.waitKey(0)
cv2.destroyAllWindows()

