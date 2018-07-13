import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/5.jpg')
img[100, 100] = [255, 255, 255]
img[100, 100, 0] = 222
it2 = img.item(10, 10, 2)
img.itemset((10, 10, 2), 100)
shape = img.shape
size = img.size
dtype = img.dtype
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
b1 = img[:, :, 0]
# img[:, :, 0] = 0
# img[:, :, 1] = 0
# img[:, :, 2] = 0

BLUE = [255, 0, 0]
img1 = cv2.imread('../images/5.jpg')
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10,  10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10,10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()

cv2.imshow('img', img)
cv2.waitKey(0)
