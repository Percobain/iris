#import all the required modules
import numpy as np
import cv2

#importing the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#To capture the video stream from webcam.
# To capture the video stream from webcam.
cap = cv2.VideoCapture(0)

# Read the captured image, convert it to Gray image and find faces
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # Flip horizontally
    cv2.imshow('img', img)  # Display the flipped image
    cv2.resizeWindow('img', 500, 400)  # Resize the window
    cv2.line(img, (500, 200), (0, 200), (0, 255, 0), 1)
    cv2.line(img, (250, 0), (250, 500), (0, 255, 0), 1)
    cv2.circle(img, (250, 200), 5, (255, 255, 255), -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)
    cv2.rectangle(img, (230, 180), (270, 220), (0, 255, 0), 5)

    # Detect the face and make a rectangle around it
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # Center of roi (Rectangle)
        xx = int(x + (x + h)) / 2
        yy = int(y + (y + w)) / 2
        print('X:')
        print(xx)
        print('Y:')
        print(yy)
        center = (xx, yy)

    # Display the stream.
    cv2.imshow('img', img)

    # Hit 'Esc' to terminate execution
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()