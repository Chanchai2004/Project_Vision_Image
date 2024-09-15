#read color from img and show color in new window
import cv2
import numpy

imginput = cv2.imread("color.png")
img =cv2.resize(imginput,(400,400))
def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        
        imgcolor = numpy.zeros([300,300,3],numpy.uint8)
        imgcolor[:] = [blue,green,red]
        
        cv2.imshow("Image",imgcolor)



cv2.imshow("Image",img)
cv2.setMouseCallback("Image", clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()
