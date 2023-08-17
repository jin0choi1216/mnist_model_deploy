import cv2
import numpy as np

# 불러온 이미지를 디코딩
def preprocess_image(file):
    image = file.read()
    image_array = np.frombuffer(image, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # Preprocess the image (resize, normalization, etc.) as needed
    return image

# 이미지를 넣기 위한 전처리
def preprocess_for_model(image):
    # Resize the image to 28x28 and convert to grayscale
    resized_image = cv2.resize(image, (28, 28), interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Normalize the pixel values to [0, 1]
    normalized_image = gray_image / 255.0

    # Reshape the image to match the model's input shape
    reshaped_image = normalized_image.reshape(28, 28, 1)

    return reshaped_image