# Deepfake Detection Project

This project aims to detect deepfake images and videos. 
Deepfakes are synthetic media where a person in an existing image or video is replaced with someone else's likeness, created using artificial intelligence. 
This detection system helps identify and mitigate the impact of deepfake content. You can add any images and videos you want to test the model to the test_images/test_videos file.

## Requirements

- Python 3.8
- Numpy 1.14.2
- Keras 2.1.5

If you want to use the complete pipeline with the face extraction from the videos, you will also need the following libraries :

- [Imageio](https://pypi.org/project/imageio/)
- [FFMPEG](https://www.ffmpeg.org/download.html)
- [face_recognition](https://github.com/ageitgey/face_recognition)

once you have installed all the dependencies you can run the example.py file to test the model.
