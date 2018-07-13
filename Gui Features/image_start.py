import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('5.jpg', 0)
b, g, r = cv2.split(img)  # opencv:bgr; plt:rgb
img2 = cv2.merge([r, g, b])
plt.imshow(img2, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('mess.png', img)
    cv2.destroyAllWindows()
