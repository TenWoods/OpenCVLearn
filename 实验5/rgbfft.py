import cv2
import numpy as np
import matplotlib.pyplot as plt

def lowpass(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    rows, cols = img.shape
    crow,ccol = (int)(rows/2) , (int)(cols/2)
    #理想低通滤波
    fshift[crow+30:len(fshift),:] = 0
    fshift[0:crow-30,:] = 0
    fshift[:,ccol+30:len(fshift)] = 0
    fshift[:,0:ccol-30] = 0
    #magnitude_spectrum = 20*np.log(np.abs(fshift))
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    # plt.subplot(131),plt.imshow(img, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    # plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    # plt.subplot(133),plt.imshow(img_back)
    # plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    # #plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
    # #plt.title('Output Image'), plt.xticks([]), plt.yticks([])
    # plt.show()
    return img_back

def hightpass(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    # f = np.log(np.abs(f))
    # fshift = np.log(np.abs(fshift))
    rows, cols = img.shape
    crow,ccol = (int)(rows/2) , (int)(cols/2)
    fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    # plt.subplot(131),plt.imshow(img, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    # plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    # plt.subplot(133),plt.imshow(img_back)
    # plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    # plt.show()
    return img_back

def bandpass(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    rows, cols = img.shape
    crow,ccol = (int)(rows/2) , (int)(cols/2)
    #带状滤波
    fshift[crow+30:,:] = 0
    fshift[0:crow-30,:] = 0
    fshift[:,ccol+30:] = 0
    fshift[:,0:ccol-30] = 0
    fshift[crow-20:crow+20, ccol-20:ccol+20] = 0
    #magnitude_spectrum = 20*np.log(np.abs(fshift))
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    # plt.subplot(131),plt.imshow(img, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    # plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    # plt.subplot(133),plt.imshow(img_back)
    # plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    # plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
    # plt.title('Output Image'), plt.xticks([]), plt.yticks([])
    # plt.show()
    return img_back

img = cv2.imread('child.jpg')
img_gray = cv2.imread('child.jpg', 0)
cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img_b = img[:,:,0]
img_g = img[:,:,1]
img_r = img[:,:,2]
img[:,:,0] = lowpass(img_gray)
img[:,:,1] = hightpass(img_gray)
img[:,:,2] = bandpass(img_gray)
cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()