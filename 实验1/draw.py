import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (200, 300), (400, 300), (255, 0, 0), 5)
cv2.rectangle(img, (100, 300), (50, 500), (0, 255, 0), 1)
cv2.circle(img, (250, 250), 50, (0, 0, 255), 5)
cv2.ellipse(img, (100, 100), (40, 50), 0, 0, 360, (255, 255, 0), 1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, '???', (200, 500), font, 4, (120,200, 12), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()