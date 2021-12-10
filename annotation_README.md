# Anno
## Code review
<p> anntation 파일 정보를 가져옴 </p>

1. [anno_image.py](./anno_image.py)
	- < Class >
		 - AnnoImage : 이미지 파일 정보를 가져옴 ( name, depth, width, height, root_dir )
2. [anno_info.py](./anno_info.py)
	- < Class >
		 - AnnoInfo : annotation 파일 정보를 가져옴 ( description, url, data_created )
3. [anno_label.py](./anno_label.py)
	- < Class >
		 - AnnoLabel : class 라벨 정보 ( name, id )
4. [anno_object.py](./anno_object.py)
	- < Class >
		 - AnnoObject : roi box 좌표값 정보를 가져옴 ( common.geometry <-- 좌표값 x1y1 x2y2 값으로 box를 만듬)
		 	- image 이름, 라벨, box_type, bounding_box, difficult


## EX
1. annotation 파일?
	- image에 있는 사물/사람의 segmentation mask와 box 영역, 카테고리 등의 정보를 담고 있는 파일

> ex] annotation{
"id" : int,
"image_id": int,
"category_id": int,
"segmentation": RLE or [polygon],
"area": float,
"bbox": [x,y,width,height],
"iscrowd": 0 or 1,
} <p> categories[{
"id": int,
"name": str,
"supercategory": str,
}]

