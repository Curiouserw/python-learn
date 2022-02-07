import cv2
import numpy as np
#定义窗口名称
winName='Mask'
#定义滑动条回调函数，此处pass用作占位语句保持程序结构的完整性
def nothing(x):
    pass
origin_image=cv2.imread('material-images/test.jpeg')
# gray_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2GRAY)
# 转换为HSV图
hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)


value = None
def update(x):
    # 回调函数 更新value的值
    global value
    value = x
    print('Update Value, value ={}'.format(value))
#新建窗口
cv2.namedWindow(winName)
#新建6个滑动条，表示颜色范围的上下边界，这里滑动条的初始化位置即为黄色的颜色范围
cv2.createTrackbar('LowerbH',winName,0,180,nothing)
cv2.createTrackbar('UpperbH',winName,0,180,nothing)
cv2.createTrackbar('LowerbS',winName,0,255,nothing)
cv2.createTrackbar('UpperbS',winName,0,255,nothing)
cv2.createTrackbar('LowerbV',winName,0,255,nothing)
cv2.createTrackbar('UpperbV',winName,0,255,nothing)
while(1):
    #函数cv2.getTrackbarPos()范围当前滑块对应的值
    lowerbH = cv2.getTrackbarPos('LowerbH', winName)
    upperbH = cv2.getTrackbarPos('UpperbH', winName)
    lowerbS = cv2.getTrackbarPos('LowerbS', winName)
    upperbS = cv2.getTrackbarPos('UpperbS', winName)
    lowerbV = cv2.getTrackbarPos('LowerbV', winName)
    upperbV = cv2.getTrackbarPos('UpperbV', winName)

    img_target=cv2.inRange(hsv_image,(lowerbH,lowerbS,lowerbV),(upperbH,upperbS,upperbV))

    cv2.imshow(winName,img_target)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()