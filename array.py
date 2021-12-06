# 0이 아닌 행렬 위치 찾기
import numpy as np
import cv2

im = cv2.imread('./ex_image.jpg')
print(im.shape)
# opencv hsv
# h = 0 ~ 179
# s = 0 ~ 255
# v = 0 ~ 255

lower_blue = np.array([90, 77, 77]) # 170 ~ 260
upper_blue = np.array([115, 255, 255])
lower_red = np.array([-10, 127, 127]) 
upper_red = np.array([17, 255, 255])
lower_mag = np.array([165,77,77])
upper_mag = np.array([175,255,255])

hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
red_range = cv2.inRange(hsv, lower_mag, upper_mag)

red_result = cv2.bitwise_and(hsv, hsv, mask=red_range)

rgb = cv2.cvtColor(red_result, cv2.COLOR_HSV2BGR)
print(red_range.sum())
print(rgb.sum())
cv2.imshow('result', red_range)
cv2.waitKey(0)
cv2.destroyAllWindows()

