import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../images/5.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, {180, 256}, [0, 180, 0, 256])

plt.imshow(hist, interpolation='nearest')
plt.show()