#scan face in image and draw rectangle around face by xml file

import cv2

img = cv2.imread("img/manyboy.jpg")

# provide the correct path to the XML file
face_cascade = cv2.CascadeClassifier('Detect/haarcascade_frontalface_default.xml')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scaleFactor = 2
minNeighber = 3
face_detect=face_cascade.detectMultiScale(gray_img, scaleFactor, minNeighber)

for x, y, w, h in face_detect:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)


cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


