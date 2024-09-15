import cv2

img = cv2.imread('duit.jpg', 1)

cv2.imshow('Duit', img)
cv2.waitKey(delay=3000)
cv2.destroyAllWindows()