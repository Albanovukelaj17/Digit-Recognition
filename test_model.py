import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


model = tf.keras.models.load_model('src/models/cnn_digit_model.h5')


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


test_image = x_test[0] / 255.0
test_image = test_image.reshape(1, 28, 28, 1)


prediction = model.predict(test_image)
predicted_class = np.argmax(prediction)


plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted: {predicted_class}, Actual: {y_test[0]}")
plt.show()
# passt alles