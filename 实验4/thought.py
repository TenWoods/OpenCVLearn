import cv2
import numpy as np

img = cv2.imread('Fig6.png')
cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow('ori',img)
img[:,:,0] = cv2.equalizeHist(img[:,:,0])
img[:,:,1] = cv2.equalizeHist(img[:,:,1])
img[:,:,2] = cv2.equalizeHist(img[:,:,2])
cv2.imshow('img',img)
cv2.waitKey(0)