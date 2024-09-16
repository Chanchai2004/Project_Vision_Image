# Detecting face and eyes in an image using Haar Cascade Classifier
import cv2

img = cv2.imread('img/boy.jpg', 1)



face_cascade = cv2.CascadeClassifier('Detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Detect/haarcascade_eye_tree_eyeglasses.xml')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=4)
eye_cascade = eye_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=4)

for x, y, w, h in face_cascade:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)
    for (ex, ey, ew, eh) in eye_cascade:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), thickness=5)





cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()