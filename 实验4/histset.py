import cv2
import numpy as np


def calcHist(img1, img2, sizex, sizey):  
    hist1 = cv2.calcHist([img1], [0], None, [256], [0.0,255.0])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0.0,255.0])
    percent1 = hist1 / (sizex * sizey)
    percent2 = hist2 / (sizex * sizey)
    addpercent1 = percent1
    for i in range(1, len(percent1)):
        addpercent1[i] = percent1[i] + percent1[i - 1]
    addpercent2 = percent2
    for i in range(1, len(percent2)):
        addpercent2[i] = percent2[i] + percent2[i - 1]
    change = np.zeros(256)
    for i in range(0, 256):
        for j in range(0, 256):
            if (j == 255):
                if (addpercent1[i] < addpercent2[0]):
                    change[i] = 0
                else:
                    change[i] = 255
                break
            elif (addpercent1[i] >= addpercent2[j] and addpercent1[i] < addpercent2[j + 1]):
                if ((addpercent1[i] - addpercent2[j]) < (addpercent1[i] - addpercent2[j + 1])):
                    change[i] = (int)(addpercent2[j] * 256)
                else:
                    change[i] = (int)(addpercent2[j+1] * 256)
                break
    for i in range(0, len(img1)):
        for j in range(0, len(img1[0])):
            img1[i][j] = change[img1[i][j]]
    print(change)

img1 = cv2.imread('Fig7A.jpg')
img2 = cv2.imread('Fig7B.jpg')
cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
cv2.cvtColor(img2, cv2.COLOR_BGR2HLS)
colors1 = cv2.split(img1)
colors2 = cv2.split(img2)
cv2.imshow('img1or', img1)
for i in range(0, 3):
    calcHist(img1[:,:,i], img2[:,:,i], len(colors1[i]), len(colors1[i][0]))
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()