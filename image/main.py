import time

import cv2
import numpy as np


origin_image = cv2.imread('material-images/test.jpeg')
# image = cv2.imread('material-images/test.jpeg', cv2.IMREAD_GRAYSCALE)


t = time.time()
fina_image_nu=str(int(t))+".jpeg"

# 图片信息
rows, cols, channel= origin_image.shape
# 转换为灰度图
gray_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2GRAY)
# 转换为HSV图
hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)
# 为了将灰度图片转换为黑白图片，对图片二值化处理
lower_red= np.array([0,186,0])
upper_red = np.array([180,255,254])
mask = cv2.inRange(hsv_image, lower_red, upper_red)
# 对黑白图片进行腐蚀瘦身
# kernel = np.ones((3,3),np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
erode = cv2.erode(mask, None, iterations=4)
# 对黑白图片进行膨胀
dilate = cv2.dilate(erode, None, iterations=4)

# --弹窗显示原始图片
cv2.imshow('1. origin-image', origin_image)
# --弹窗显示灰度图
cv2.imshow('2. gray-image', gray_image)
# --弹窗显示灰度图
cv2.imshow('3. hsv-image', hsv_image)
# --弹窗显示黑白图片
cv2.imshow('4. white-black-image', mask)
# # --弹窗显示腐蚀瘦身后的黑白图片
cv2.imshow('5. white-black-erode-image', erode)
# # --弹窗显示膨胀后的黑白图片
cv2.imshow('6. white-black-dilate-image', dilate)


for i in range(rows):
    for j in range(cols):
        if dilate[i, j] == 255:  # 像素点255表示白色
            origin_image[i, j] = (255, 0, 0)
#
cv2.imshow('7. final', origin_image)
cv2.imwrite("results/"+fina_image_nu, origin_image)

print("   results/"+fina_image_nu)

cv2.waitKey(0)
cv2.destroyAllWindows()

