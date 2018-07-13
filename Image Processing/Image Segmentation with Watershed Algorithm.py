import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/77.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('sure_fg', sure_fg)
cv2.imshow('dist', dist_transform)
cv2.imshow('sure_bg', sure_bg)
cv2.imshow('unknown', unknown)
cv2.waitKey(0)

