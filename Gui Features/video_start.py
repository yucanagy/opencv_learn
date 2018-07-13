import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.open()
ret = cap.get(3)
ret = cap.set(3, 320)
ret = cap.set(4, 240)

fourcc = cv2.VideoWriter_fourcc(*'3IVD')
out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # frame = cv2.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
