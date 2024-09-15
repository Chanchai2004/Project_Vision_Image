import cv2

img = cv2.imread('img/duit.jpg', 1)
imgresize =cv2.resize(img,(600,400))

cv2.imshow('Duit', imgresize)
cv2.waitKey(delay=3000)
cv2.destroyAllWindows()