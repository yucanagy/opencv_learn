import cv2
import numpy as np
from matplotlib import pyplot as plt

# image addition
img1 = cv2.imread('../images/5.jpg')
img2 = cv2.imread('../images/11.jpg')
img = img2 + [np.uint8(0), np.uint8(0), np.uint8(0)]
cv2.imshow('img', img)


# image blending 修改透明度叠加
dst1 = cv2.addWeighted(img1, 0.1, img2, 0.9, 0)
dst2 = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)
dst3 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
dst4 = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
dst5 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
dst6 = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
dst7 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
dst8 = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
dst9 = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)
b, g, r = cv2.split(dst1)
dst1 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst2)
dst2 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst3)
dst3 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst4)
dst4 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst5)
dst5 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst6)
dst6 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst7)
dst7 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst8)
dst8 = cv2.merge([r, g, b])
b, g, r = cv2.split(dst9)
dst9 = cv2.merge([r, g, b])

plt.subplot(331), plt.imshow(dst1, 'gray'), plt.title('dst1'), plt.xticks([0, 100]), plt.yticks([0, 100])
plt.subplot(332), plt.imshow(dst2), plt.title('dst2')
plt.subplot(333), plt.imshow(dst3), plt.title('dst3')
plt.subplot(334), plt.imshow(dst4), plt.title('dst4')
plt.subplot(335), plt.imshow(dst5), plt.title('dst5')
plt.subplot(336), plt.imshow(dst6), plt.title('dst6')
plt.subplot(337), plt.imshow(dst7), plt.title('dst7')
plt.subplot(338), plt.imshow(dst8), plt.title('dst8')
plt.subplot(339), plt.imshow(dst9), plt.title('dst9')
plt.show()

# bitwise operations
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 110, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('img1_bg', img1_bg)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.namedWindow('img2_fg',)
cv2.imshow('img2_fg', img2_fg)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
