import cv2
import numpy as np


def nothing(x):
    print(x)
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0 : OFF\n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)


drawing = False
mode = True


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img1, (ix, iy), (x, y), color, 2)
            else:
                cv2.circle(img1, (x, y), 15, color, 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img1, (ix, iy), (x, y), color, 2)
        else:
            cv2.circle(img1, (x, y), 15, color, 2)


img1 = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image1')
cv2.setMouseCallback('image1', draw_circle)

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
        color
    else:
        img[:] = [b, g, r]
        color = [b, g, r]

    cv2.imshow('image1', img1)
    k = cv2.waitKey(1) & 0xFF

    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyWindow()
