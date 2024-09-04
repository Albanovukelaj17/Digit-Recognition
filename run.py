from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import base64
from io import BytesIO
import re

app = Flask(__name__)
model = tf.keras.models.load_model('models/cnn_digit_model.keras')


def prepare_image(data_image):

    data_image = data_image.convert('L')
    data_image = data_image.resize((28, 28))
    data_image = np.array(data_image) / 255.0
    data_image = data_image.reshape(1, 28, 28, 1)
    return data_image

#route um den submit methode zu nutzten, an backende zu geben
@app.route('/submit_canvas', methods=['POST'])
def submit_canvas():
    data = request.get_json()
    image_data = data['image']

    image_data = re.sub('^data:image/.+;base64,', '', image_data)
    #python imaging library
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    processed_image = prepare_image(image)
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)


    return jsonify({'prediction': int(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True)
