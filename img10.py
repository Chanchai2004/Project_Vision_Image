#check the color of the image by using mask

import cv2
import numpy

while True:
    img = cv2.imread("img/o.jpg")
    img=cv2.resize(img,(400,400))
    
    lower = numpy.array([8,48,6])
    upper = numpy.array([75,255,39])

    mask = cv2.inRange(img,lower,upper)
    

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

    cv2.imshow("Image",img)
    cv2.imshow("Mask",mask)
    
cv2.destroyAllWindows()