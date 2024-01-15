import numpy as np
from classifiers import *
from pipeline import *

from tensorflow.keras.preprocessing.image import ImageDataGenerator

classifier = Meso4()
classifier.load('weights/Meso4_DF.h5')

dataGenerator = ImageDataGenerator(rescale=1./255)
generator = dataGenerator.flow_from_directory(
        'test_images',
        target_size=(256, 256),
        batch_size=1,
        class_mode='binary',
        subset='training')

# 3 - Predict
X, y = generator.next()
print('Predicted :', classifier.predict(X), '\nReal class :', y)

# 4 - Prediction for a video dataset

classifier.load('weights/Meso4_F2F.h5')

predictions = compute_accuracy(classifier, 'test_videos')
for video_name in predictions:
    print('`{}` video class prediction :'.format(video_name), predictions[video_name][0])
