import cv2

image = cv2.imread('material-images/test.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,105, 255, cv2.THRESH_BINARY_INV)[1]
thresh = 255 - thresh

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
result = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

cv2.imshow('thresh', thresh)
cv2.imshow('result', result)
cv2.waitKey(0)