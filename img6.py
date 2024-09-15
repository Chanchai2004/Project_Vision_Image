#datetime in vdo
import cv2
import datetime

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    check, frame = cap.read()

    if check == True:
        currentdate = str(datetime.datetime.now())
        cv2.putText(frame, currentdate, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), cv2.LINE_4)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()