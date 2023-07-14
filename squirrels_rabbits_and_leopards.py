# Main Program

from google.colab import drive # only for google colab to import data from drive <optional>

drive.mount('/content/gdrive') # only for google colab to mount the drive at a point or folder <optional>

!pip install ultralytics # install dependencies <optional>

from ultralytics import YOLO # import YOLO model

model=YOLO('yolov8x.yaml') # declaring model as Yolov8x.yaml object

model.train(data='path_to/squirrels_rabbits_and_leopards.yaml',epochs=300) # give more epochs if want more accuracy

trainedmodel= YOLO('path_to/runs/detect/train/weights/best.pt') # getting trainedmodel to predict from it

trainedmodel.predict('Path/to/image') # give the image path to predict