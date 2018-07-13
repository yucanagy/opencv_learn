import cv2
import numpy as np
import time

img1 = cv2.imread('../images/5.jpg')
e1 = cv2.getTickCount()
t1 = time.time()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
    cv2.imshow('img1',img1)
    cv2.waitKey(0)
e2 = cv2.getTickCount()
t2 = time.time()
t = (e2 - e1)/cv2.getTickFrequency()
t1 = t2 - t1
cv2.useOptimized()
print(t, t1)
