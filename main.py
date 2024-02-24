import cv2
import numpy as np
import face_recognition

imgDev = face_recognition.load_image_file("ImageFile\dev.jpg")
imgDev = cv2.cvtColor(imgDev,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgDev)[0]
encodeDev = face_recognition.face_encodings(imgDev)[0]
cv2.rectangle(imgDev,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

cv2.imshow('Dev',imgDev)
cv2.waitKey(0)