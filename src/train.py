from data_loader import load_data
from model import create_model
import tensorflow as tf


#load the dat_loader mnist data
(x_train, y_train), (x_test, y_test) = load_data()



#create the model
model = create_model()

#train model
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

#accuracy
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Accuracy: {test_acc}")

#save model
model.save('models/cnn_digit_model.h5')

#like wandbai history
import matplotlib.pyplot as plt

#accuracy of validation and training
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
