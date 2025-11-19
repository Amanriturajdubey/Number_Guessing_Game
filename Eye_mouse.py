import cv2
import mediapipe
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    cv2.imshow('Eye contolled Mouse',frame)
    cv2.waitKey(1)
