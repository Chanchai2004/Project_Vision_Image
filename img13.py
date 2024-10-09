#scan face in video and draw rectangle around face by xml file
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

result = cv2.VideoWriter("output.avi", fourcc, 60.0, (1280, 720))

face_cascade = cv2.CascadeClassifier('Detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Detect/haarcascade_eye_tree_eyeglasses.xml')

while (cap.isOpened()):
    check, frame = cap.read()

    if check == True:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_detect = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        eye_detectd = eye_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)
            for (ex, ey, ew, eh) in eye_detectd:
                cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), thickness=5)
           
        result.write(frame)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()