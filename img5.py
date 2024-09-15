#position in image 
import cv2
img = cv2.imread("duit.jpg")

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = "x: " + str(x) + ", y: " + str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.imshow("Image",img)



cv2.imshow("Image",img)
cv2.setMouseCallback("Image", clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()
