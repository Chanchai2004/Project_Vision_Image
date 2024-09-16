#use trackbar to change the threshold value of the image
import cv2

def display(value):
    pass

cv2.namedWindow("Output")
cv2.createTrackbar("value", "Output", 128, 255,display)

while True:
    gray_img = cv2.imread("img/fish.jpg", cv2.IMREAD_GRAYSCALE)
    gray_img=cv2.resize(gray_img,(1000,1000))
    thresh_value=cv2.getTrackbarPos("value", "Output")
    thresh, result=cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_BINARY, gray_img)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
    cv2.imshow("Output", result)

cv2.destroyAllWindows()