## mmdetection

- Labeling

- - Labelme 를 통한 이미지 라벨링
  - 모델 선정 
  - faster_rcnn(모델)_r50(CNN 층의 수)_fpn(Neck)_1x(학습 epoch 수)_coco(학습 데이터 셋)

 

- - - /mmdetection/configs/ <- 사용가능한 모델

- Model

- - https://greeksharifa.github.io/references/2021/08/30/MMDetection/ 참고

- R - CNN

- - https://seongkyun.github.io/papers/2019/01/06/Object_detection/ 참고

  - 적절한 위치에 bounding box 생성

  - - 모든 박스에 대해서 cnn을 거쳐야 하므로 연산량이 매우 많다

- Fast R-CNN

- - 모든 박스들이 cnn 네트워크를 거쳐야하는 병목구조의 단점을 개선
  - 전체 이미지에대해 cnn을 거치고 출력된 맵단에서 객체 탐지를 수행
  - Cnn 네트워크가 아니라 selective search 외부 알고리즘으로 수행하여 병목현상이 발생

- Faster R-CNN

- - Region Proposal을 RPN이라는 네트워크를 이용하여 수행

  - Region Proposal 단계에서 병목현상을 해소

  - - 해당 단계를 selective search 가 아닌 CNN으로 해결

- SSD

- - url참조

-  Mask R-CNN

- - Pixel 로 이미지를 디텍션