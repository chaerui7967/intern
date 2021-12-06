import numpy as np
import cv2

# 동영상 info
# 전체 경로를 적어야함
cap = cv2.VideoCapture('/Users/chaegilho/test_py/final.mp4')
print('video info')
print('총 프레임 개수 : ', cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('fps : ', cap.get(cv2.CAP_PROP_FPS))
print('동영상 길이 : ', cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS))
num = cap.get(cv2.CAP_PROP_POS_MSEC)

r_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

while 1:
    ret, frame = cap.read()

    print(ret)
    print(len(frame))

    print('@'*50)

    p_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print(p_frame)    

    cv2.imshow(str(p_frame),frame)
    print(cap.get(cv2.CAP_PROP_POS_MSEC))
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    # if cv2.waitKey(0) == 27:
    #     break
    # else:
    #     cv2.destroyAllWindows()

    # 프레임이 마지막까지 갔다면 현재 프레임을 0으로 셋팅
    if int(p_frame) == int(r_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)