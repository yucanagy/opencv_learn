import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../images/5.jpg', 0)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])  # np计算直方图

cdf = hist.cumsum()  # 数组降维 变为一维数组
cdf_normalized = cdf*float(hist.max())/cdf.max()

cdf_m = np.ma.masked_equal(cdf, 0)  # 屏蔽等于0的部分
cdf_m = (cdf_m-cdf_m.min()) * 255 / (cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # 将被屏蔽的部分用0填充
img2 = cdf[img]

plt.subplot(121)
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')  # plt绘制直方图
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')


plt.subplot(122)
plt.plot(cdf_normalized, color='b')
plt.hist(img2.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
cv.imshow('cl1', cl1)
cv.waitKey(0)