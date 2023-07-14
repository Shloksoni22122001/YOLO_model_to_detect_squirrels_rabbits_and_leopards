# Squirrels, Rabbits, and Leopards Detection

## Description ✍️
- **YOLOv8 model to detect Leopards, Rabbits and Squirrels**
- This project aims to detect and classify images of squirrels, rabbits, and leopards using the YOLO (You Only Look Once) object detection algorithm. The program is developed using Google Colaboratory and the Ultralytics YOLO library.
- the images are from https://pixabay.com/ so they are open source.
⚠️ Note: this model is not 100% accurate its accuracy rating can be seen through the confusion matrix which is nearly 90%


## Clone the repository:
```
git clone https://github.com/Shloksoni22122001/YOLO_model_to_detect_squirrels_rabbits_and_leopards
```

## Authors 👑

- [@Shloksoni😎](https://www.github.com/Shloksoni22122001)


## Demo
![]![example-3](https://github.com/Shloksoni22122001/YOLO_model_to_detect_squirrels_rabbits_and_leopards/assets/117386665/f404f8f4-af1a-4256-b4ff-6cf929c4a5d0)
![example-4](https://github.com/Shloksoni22122001/YOLO_model_to_detect_squirrels_rabbits_and_leopards/assets/117386665/1a6a738a-88a1-4297-b26b-f85bd825d5f8)
![example-1](https://github.com/Shloksoni22122001/YOLO_model_to_detect_squirrels_rabbits_and_leopards/assets/117386665/f11ab259-c643-4ae0-b210-692272fc3fa6)
![example-2](https://github.com/Shloksoni22122001/YOLO_model_to_detect_squirrels_rabbits_and_leopards/assets/117386665/51188cbc-ceef-4693-8dbd-5efdb38071a3)



## Installation ⬇️
### Dependencies
1. Python == 3.10.12
2. Ultralytics == 8.0.134


⚠️ Note: this Project was made in google collab so installing requirements.txt on local PCs might take extra time and consume lots of extra space follow steps below for local PCs

### Installing dependencies
Creating the conda environment:
```
conda create -n <Environment_name> python=3.10.12
```
Activating the conda environment:
```
conda activate <Environment_name>
```
Installing opencv
```
pip install ultralytics
```

**or you can also refer to requirements.txt** 🤝

(!to run the requirements.txt directly here is the command)

```
pip install -r requirements.txt
```
## Usage/Examples 👨‍💻

- It is used to detect squirrels, rabbits and leopards from the image/video or live camera its parts or chunks of codes can be used in various places as per requirement 😊

- Every line or chunk are explained in code along with comments 🫡
    ```
    yolo detect predict model=path/to/best.pt source='<Path/to/image>'
    ```
## Acknowledgments

- [Ultralytics YOLO](https://github.com/ultralytics/yolov5) - The YOLO library used in this project.
- [Google Colaboratory](https://colab.research.google.com/) - The platform used for developing the program.

## Customization ⚙️

- Feel free to make this code your own and customize as this is not anyone's property😂

## License 🪪

This project is licensed under the [MIT License]

## **Conclusion**✔️

Conclusion:

In conclusion, this project demonstrates the application of the YOLO (You Only Look Once) object detection algorithm for detecting and classifying images of squirrels, rabbits, and leopards. The program, developed using Google Colaboratory and the Ultralytics YOLO library, provides a convenient and efficient solution for identifying these animals in images.

By utilizing pre-trained YOLO weights and fine-tuning the model on a specific dataset, the program achieves accurate and reliable detection results. The trained YOLO model included in this repository, `best.pt`, serves as a starting point for further development and experimentation.

The README provides clear instructions on how to get started with the program, including cloning the repository, installing dependencies, and running the detection script. It also highlights the importance of configuring the YOLO model through the `yolov8x.yaml` file and organizing the dataset appropriately for training.

It's worth noting that the dataset used for training is not included in this repository, emphasizing the need for users to acquire their own dataset or utilize publicly available sources. By following the provided structure and labeling guidelines, users can train the model on their specific animal detection tasks.

The project is licensed under the MIT License, ensuring that users can freely use, modify, and distribute the code, while acknowledging the contributions of the Ultralytics YOLO library and Google Colaboratory.

Overall, this project showcases the power and versatility of YOLO for object detection and provides a foundation for developing similar applications in wildlife monitoring, conservation, and related domains.
