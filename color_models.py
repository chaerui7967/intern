import cv2

src = cv2.imread('ex_image.jpg')
# cv2.imshow('src', src)
# cv2.waitKey()
# cv2.destroyAllWindows()

src_xyz = cv2.cvtColor(src, cv2.COLOR_BGR2XYZ)
src_yuv = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
src_lab = cv2.cvtColor(src, cv2.COLOR_BGR2Lab) # L : 반사율, 색도1, 색도2
src_luv = cv2.cvtColor(src, cv2.COLOR_BGR2Luv) #CIE Luv
src_hls = cv2.cvtColor(src, cv2.COLOR_BGR2HLS) # 색상 밝기 채도



cv2.imshow('rgb',src)
cv2.imshow('xyz',src_xyz)
cv2.imshow('yuv',src_yuv)
cv2.imshow('hsv',src_hsv)
cv2.imshow('lab',src_lab)
cv2.imshow('luv',src_luv)
cv2.imshow('hls',src_hls)
cv2.waitKey()
cv2.destroyAllWindows()


## 이미지에서 색 판별로 사용가능할 만한 색 모델

