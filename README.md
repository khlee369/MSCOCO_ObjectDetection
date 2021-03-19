# MSCOCO_ObjDet_Detail

MSCOCO object detection dataset의 format과 pycocotools의 간략한 사용법을 정리한 repository 입니다.

## MSCOCO Dataset Format
MSCOCO dataset은 실제 data인 image와 data를 설명하는 json 파일로 구성되어있음. 아래 내용은 json의 format을 설명함

세부 내용은 https://cocodataset.org/#format-data 참조

영상 설명은 https://www.youtube.com/watch?v=h6s61a_pqfM 참조

### common data format
```
{
    "info": info, 
    "images": [image], 
    "annotations": [annotation], 
    "licenses": [license],
}

info{
    "year": int, 
    "version": str, 
    "description": str, 
    "contributor": str, 
    "url": str, 
    "date_created": datetime,
}

image{
    "id": int, 
    "width": int, 
    "height": int, 
    "file_name": str, 
    "license": int, 
    "flickr_url": str, 
    "coco_url": str, 
    "date_captured": datetime,
}

license{
    "id": int, 
    "name": str, 
    "url": str,
}
```
### Object Detection
categories field가 추가되고 annotations field가 정의됨

annotation의 id는 annotation field의 각 item에 할당된 고유한 id이며 category_id가 object의 class(i.e. label)의 id 이다.

annotation의 iscrowd는 segmentation과 관련있음, single object인지 group/cluster of objects(object들이 이미지에서 overlap 수준으로 뭉쳐있는경우, 혹은 굉장히 많은경우)인지 표시

For **object detection** annotations, the format is **"bbox" : [x,y,width,height]**

Where:

x, y: the upper-left coordinates of the bounding box

width, height: the dimensions of your bounding box
```
annotation{
    "id": int,
    "image_id": int,
    "category_id": int,
    "segmentation": RLE or [polygon],
    "area": float,
    "bbox": [x,y,width,height],
    "iscrowd": 0 or 1,
}

categories[{
    "id": int,
    "name": str,
    "supercategory": str,
}]
```

## pycocotools examples
cocoapi github : https://github.com/cocodataset/cocoapi

cocoapi는 coco dataset을 visualize하고 id에 따라 image를 관리할수 있으며 **object detection evaluation을 지원함**

instances_val2017.json은 coco 2017 dataset에서 다운받음

yolov3_predictions.json은 yolov3 모델 output을 저장하였음, 참조링크 : https://github.com/ultralytics/yolov3/blob/master/tutorial.ipynb

minimal_2017.json는 object detection evaluation에 필요한 최소한의 field만 모은 json, make_minimal.py 참조

```
# yolov3_prediction.json
[{
    "image_id": int,
    "category_id": int,
    "bbox": [x,y,width,height],
    "score": float,
}]
```

### example
예제는 pycocoEvalDemo.ipynb 참조
```
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=70.58s).
Accumulating evaluation results...
DONE (t=8.79s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.433
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.630
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.470
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.284
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.485
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.538
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.346
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.581
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.634
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.474
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.686
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.766
```

