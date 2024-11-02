import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model("fruit_ripeness_model.h5")

# Define function to predict ripeness
def predict_ripeness(image_path):
    img = image.load_img(image_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        print("The fruit is ripe.")
    else:
        print("The fruit is unripe.")

# Example usage
predict_ripeness("path_to_test_image.jpg")  # Replace with actual test image path
