# Draw line between two points on image by clicking on the image

import cv2
img1 = cv2.imread("img/color.png")
img =cv2.resize(img1,(400,400))

point =[]

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        point.append((x,y))
        if len(point) >=2:
            cv2.line(img,point[-1],point[-2],(0,0,255),2)
        cv2.circle(img,(x,y),10,(0,0,255),2)
        cv2.imshow("Image",img)

cv2.imshow("Image",img)

cv2.setMouseCallback("Image", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()