import cv2
import numpy as np

img = cv2.imread('../../images/5.jpg')
img_copy = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 0, 2)

# Moments
cnt = contours[27]
M = cv2.moments(cnt)
print(M)
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area


# Contour Area
for s in contours:
    area = cv2.contourArea(s)  # 轮廓面积
    print(area, cv2.moments(s)['m00'])

# Contour Perimeter
for s in contours:
    perimeter = cv2.arcLength(s, True)
    print(perimeter)

# Contour Approximation
epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
cv2.polylines(img, [approx], True, (0, 0, 255), 2)
cv2.imshow('approx', img)

#  Convex Hull

# Straight Bounding Rectangle
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img_copy, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('qwer', img_copy)

# Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
imm = cv2.drawContours(img_copy, [box], 0, (0, 0, 255), 2)
cv2.imshow('imm', imm)

# Minimum Enclosing Circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img_copy,center,radius,(0,255,0),2)
cv2.imshow('imgm', img)

# Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(img_copy,ellipse,(0,255,0),2)
cv2.imshow('img12', im)

# Fitting a Line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img_copy,(cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow('img1wq', img)
cv2.waitKey(0)
