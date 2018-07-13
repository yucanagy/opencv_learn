import cv2
import numpy as np
from matplotlib import pyplot as plt
import skimage
from skimage import img_as_float32

img = cv2.imread('../images/5.jpg')

# 2D Convolution ( Image Filtering )
kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
plt.subplot(121), plt.imshow(img), plt.title('original')
plt.subplot(122), plt.imshow(dst), plt.title('averaging')
plt.show()


img = skimage.util.random_noise(img, mode='gaussian')
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])
img = img_as_float32(img)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# Image Blurring (Image Smoothing)
blur = cv2.blur(img, (50, 50))  # Averaging
plt.subplot(121), plt.imshow(img), plt.title('Averaging')
plt.subplot(122), plt.imshow(blur), plt.title('Averaging1')
plt.show()

blur = cv2.GaussianBlur(img, (5, 5), 0) # Gaussian Filtering
plt.subplot(121), plt.imshow(img), plt.title('Gaussian')
plt.subplot(122), plt.imshow(blur), plt.title('Gaussian1')
plt.show()

blur = cv2.medianBlur(img, 5)  # Median Filtering
plt.subplot(121), plt.imshow(img), plt.title('Median')
plt.subplot(122), plt.imshow(blur), plt.title('Median1')
plt.show()

blur = cv2.bilateralFilter(img, 9, 75, 75)  # Bilateral Filtering
plt.subplot(121), plt.imshow(img), plt.title('Bilateral')
plt.subplot(122), plt.imshow(blur), plt.title('Bilateral1')
plt.show()




