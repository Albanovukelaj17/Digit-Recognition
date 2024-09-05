import os
import tensorflow as tf
from flask import Flask, request, jsonify, render_template, send_from_directory
import numpy as np
from PIL import Image
import re
import base64
from io import BytesIO

import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


model_path = os.path.join(os.path.dirname(__file__), 'src/models/cnn_digit_model.h5')
model = tf.keras.models.load_model(model_path)

def prepare_image(data_image):
    data_image = data_image.convert('L')
    data_image = data_image.resize((28, 28))
    data_image = np.array(data_image) / 255.0

    # Save the image to a file (optional for debugging)
    plt.imsave('processed_image_debug.png', data_image, cmap='gray')

    data_image = data_image.reshape(1, 28, 28, 1)
    return data_image


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/javascript/<path:filename>')
def serve_javascript(filename):
    return send_from_directory(os.path.join(app.root_path, 'app/javascript'), filename)

@app.route('/submit_canvas', methods=['POST'])
def submit_canvas():
    data = request.get_json()
    image_data = data['image']


    image_data = re.sub('^data:image/.+;base64,', '', image_data)
    image = Image.open(BytesIO(base64.b64decode(image_data)))


    print(f"Original Image size: {image.size}, Mode: {image.mode}")


    processed_image = prepare_image(image)


    print(f"Processed Image shape: {processed_image.shape}")

    prediction = model.predict(processed_image)
    print(f"Prediction probabilities: {prediction}")
    predicted_class = np.argmax(prediction)
    print(f"Predicted class: {predicted_class}")


    print("Original Image size:", image.size)
    print("Processed Image shape:", processed_image.shape)


    return jsonify({'prediction': int(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True, port=5008)
