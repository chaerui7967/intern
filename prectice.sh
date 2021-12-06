#!/usr/bin/env bash

python s_shot.py ../data/ls_test/20210804_165822.mp4 \
../work_dirs/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco.py \
../work_dirs/faster_rcnn_r50_fpn_1x_coco/latest.pth \
--show
