import tensorflow as tf
from app.utils import preprocess_for_model
import numpy as np


# 모델을 불러와서 예측
def load_model_and_predict(image):
    # Load your trained TensorFlow model
    model = tf.keras.models.load_model('models/mnist_model.h5')  # Example

    # Preprocess the image for model input
    processed_image = preprocess_for_model(image)  # You need to define this function

    # Perform prediction using the loaded model
    prediction = model.predict(np.expand_dims(processed_image, axis=0)) # (1, 이미지 높이, 이미지 너비, 채널 수)

    # You may need to post-process prediction results here
    # Convert the prediction to a class label
    predicted_class = predict_class(prediction)

    # return prediction.tolist() # 확률로 출력
    return predicted_class

# 예측결과를 해당 클레스로 출력
def predict_class(prediction):
    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(prediction)
    
    # Convert the class index to the actual class label (0 to 9 in this case)
    predicted_class = str(predicted_class_index)
    
    return predicted_class
