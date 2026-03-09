
**Model Data**

We use a frozen inference graph `frozen_inference_graph.pb` for this benchmark which is too large for being included on GitHub. It can be downloaded from here: http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet50_coco_2018_01_28.tar.gz

```bash
sha256sum 600.workflows/650.vid/faster_rcnn_resnet50_coco_2018_01_28.tar.gz
0f898f96d6c416de192c516fb6fa773ae9f5ee253eb2ab4015445fbd6eb0ab76  600.workflows/650.vid/faster_rcnn_resnet50_coco_2018_01_28.tar.gz

# extract the file and move it 
tar -xf faster_rcnn_resnet50_coco_2018_01_28.tar.gz

sha256sum 600.workflows/650.vid/faster_rcnn_resnet50_coco_2018_01_28/frozen_inference_graph.pb
e12cca9868c73f83940adafdcb18cda429ff398454505a721f95277b728c82af  faster_rcnn_resnet50_coco_2018_01_28/frozen_inference_graph.pb
```

The config file `faster_rcnn_resnet50_coco_2018_01_28.pbtxt` is taken from [`opencv-extra`](https://github.com/opencv/opencv_extra) repository, as we use OpenCV.

[Original path in opencv-extra](https://raw.githubusercontent.com/opencv/opencv_extra/refs/heads/master/testdata/dnn/faster_rcnn_resnet50_coco_2018_01_28.pbtxt)

**Video Data**

As input data, we use the video [4K Road traffic video for object detection and tracking - free download now!](https://www.youtube.com/watch?v=MNn9qKG2UFI) published by Karol Majek on a Creative Commons license. We used the following command to download the video:

```bash
yt-dlp -S res,ext:mp4:m4a --recode mp4 https://www.youtube.com/watch\?v\=MNn9qKG2UFI
```

The video was acquired on 4th of July, 2024 and stored as `full_video.mp4`. Then, we created the input test cases with the following commands:

```bash
ffmpeg -ss 0:00 -i full_video.mp4 -t 0:00:00.200 -map 0 -c copy video_test.mp4
ffmpeg -ss 0:00 -i full_video.mp4 -t 0:00:02 -map 0 -c copy video_small.mp4
ffmpeg -ss 0:00 -i full_video.mp4 -t 0:00:10 -map 0 -c copy video_large.mp4
```
