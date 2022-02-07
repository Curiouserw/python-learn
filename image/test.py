import matplotlib.pyplot as plt
import cv2

# cv2.imread()接口读图像，读进来直接是BGR 格式数据格式在 0~255，通道格式为(W,H,C)
img_BGR = cv2.imread('material-images/test.jpeg')
plt.subplot(2, 2, 1)
plt.imshow(img_BGR)
plt.axis('off')
plt.title('BGR')

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
plt.subplot(2, 2, 2)
plt.imshow(img_RGB)
plt.axis('off')
plt.title('RGB')

img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
print(img_BGR.shape)
print(img_GRAY.shape)
print(type(img_GRAY))
print(img_GRAY.astype)

print(img_GRAY.dtype.name, img_BGR.dtype.name)

from skimage import io, data

img = data.chelsea()
print(img.dtype.name)

plt.subplot(2, 2, 3);
plt.imshow(img_GRAY);
plt.axis('off');
plt.title('GRAY')

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
plt.subplot(2, 2, 4);
plt.imshow(img_HSV);
plt.axis('off');
plt.title('HSV')
plt.show()