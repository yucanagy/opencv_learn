import cv2
import numpy as np
from matplotlib import pyplot as plt

# Scaling
img = cv2.imread('../images/5.jpg')
height, width = img.shape[:2]
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('res', res)

# Translation
rows, cols, tr = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('dst', dst)

# Rotation
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rota = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('rota', rota)

# Affine Transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
b, g, r = cv2.split(img)
plt.subplot(121), plt.imshow(cv2.merge([r, g, b])), plt.title('Input')
b, g, r = cv2.split(dst)
plt.subplot(122), plt.imshow(cv2.merge([r, g, b])), plt.title('Output')
plt.show()

# Perspective Transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

cv2.waitKey(0)