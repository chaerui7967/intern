# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser
import cv2
import mmcv
import numpy as np
from tqdm import tqdm
from mmdet.apis import inference_detector, init_detector

from datetime import datetime
import time


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('video', help='Video file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument('--out', help='Out Image file')
    parser.add_argument(
        '--device', default='cpu', help='Device used for inference')
    parser.add_argument(
        '--score-thr', type=float, default=0.3, help='Bbox score threshold')
    parser.add_argument('--show', action='store_true', help='Show video')
    parser.add_argument(
        '--wait-time',
        type=float,
        default=1,
        help='The interval of show (s), 0 is block')
    args = parser.parse_args()
    return args

def frame_crop(frame,x1,y1,x2,y2):
    cut_frame = frame[y1:y2,x1:x2]
    return cut_frame

def main():
    args = parse_args()
    assert args.out or args.show, \
        ('Please specify at least one operation (save/show the '
         'video) with the argument "--out" or "--show"')

    model = init_detector(args.config, args.checkpoint, device=args.device)

    # color range
    lower_blue = np.array([90, 77, 77])
    upper_blue = np.array([115, 255, 255])
    lower_red = np.array([-10, 127, 127]) 
    upper_red = np.array([17, 255, 255])
    lower_mag = np.array([165,77,77])
    upper_mag = np.array([175,255,255])

    # img txt
    red = (0,0,255)

    video_reader = cv2.VideoCapture(args.video)
    video_writer = None
    ch_frame = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video_reader.get(cv2.CAP_PROP_FPS)
    x1,y1,x2,y2 =0,0,0,0
    event = 1

    cnt = True
    cnt1 = False


    for a in tqdm(range(ch_frame),desc='progress_bar', mininterval = 0.01):
        print(datetime.fromtimestamp(time.time()))

        ret, frame = video_reader.read()

        result = inference_detector(model, frame)
        result1 = list()
        result1.append(result[0])
        x1,y1,x2,y2 = int(list(result[0])[0][0]),int(list(result[0])[0][1]),int(list(result[0])[0][2]),int(list(result[0])[0][3])
        frame2 = frame_crop(frame,x1,y1,x2,y2) # indicator pick
        
        if a == 0: # size pick
            w = x2-x1
            h = y2-y1
            # if args.out:
            #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            #     video_writer = cv2.VideoWriter(
            #         args.out, fourcc, fps,
            #         (w, h))
            #     print(w, h)

        frame2 = cv2.resize(frame2,(w,h)) # resize 
        # video_writer.write(frame2)
        

        # event
        hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
        active_range = cv2.inRange(hsv, lower_blue, upper_blue)
        per90_range = cv2.inRange(hsv, lower_red, upper_red)
        per105_range = cv2.inRange(hsv, lower_mag, upper_mag)

        # active_result = cv2.bitwise_and(hsv, hsv, mask=active_range)
        per90_result = cv2.bitwise_and(hsv, hsv, mask=per90_range)
        per105_result = cv2.bitwise_and(hsv, hsv, mask=per105_range)

        # event
        if (per105_result.sum() != 0) or (per90_result.sum() != 0) :
            cnt = True
        else:
            cnt = False


        if event == 1 or cnt != cnt1:
            if cnt :
                cnt1 = True
                print('True')
                # print(frame2.shape)
                print(video_reader.get(cv2.CAP_PROP_POS_MSEC)/1000)
                event_time = str(video_reader.get(cv2.CAP_PROP_POS_MSEC)/1000)
                frame2 = cv2.putText(frame2, event_time, org=(200,140), fontFace=0, fontScale=1, color=red,thickness=1)
                num = './s_shot/' + str(event) + 'event_True.jpg'
                cv2.imwrite(num, frame2)
            else :
                cnt1 = False
                print('False')
                print(video_reader.get(cv2.CAP_PROP_POS_MSEC)/1000)
                event_time = str(video_reader.get(cv2.CAP_PROP_POS_MSEC)/1000)
                frame2 = cv2.putText(frame2, event_time, org=(200,140), fontFace=0, fontScale=1, color=red,thickness=1)
                num = './s_shot/' + str(event) + 'event_False.jpg'
                cv2.imwrite(num,frame2)
            event += 1
        print(datetime.fromtimestamp(time.time()))
            

        if args.show:
            cv2.imshow('indicator',frame2)
            cv2.waitKey(10)
                
        
    # if video_writer:
    #     video_writer.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
