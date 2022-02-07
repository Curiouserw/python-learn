import cv2
import numpy as np
from skimage.morphology import skeletonize

# load image
img = cv2.imread("material-images/test.jpeg")

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold image
thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)[1]

# apply morphology close
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# apply morphology open
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# apply morphology erode
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21,21))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)

# write result to disk
cv2.imwrite("5_thinned.png", thresh)

# skeletonize image and dilate
skeleton = cv2.threshold(thresh,0,1,cv2.THRESH_BINARY)[1]
skeleton = (255*skeletonize(skeleton)).astype(np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
skeleton_dilated = cv2.morphologyEx(skeleton, cv2.MORPH_DILATE, kernel)

# write result to disk
cv2.imwrite("5_skeleton_dilated.png", skeleton_dilated)

cv2.imshow("IMAGE", img)
cv2.imshow("RESULT1", thresh)
cv2.imshow("RESULT2", skeleton_dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
