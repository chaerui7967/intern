import numpy as np
import cv2

# 동영상 info
# 전체 경로를 적어야함
cap = cv2.VideoCapture('/Users/chaegilho/projects/mmdetection/data/ls_test/20210804_165822.mp4')
print('video info')
print('총 프레임 개수 : ', cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('fps : ', cap.get(cv2.CAP_PROP_FPS))
print('동영상 길이 : ', cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS))
