import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

inputs = Input(shape=(28, 28, 1))
#28 x28 greyscale image , written number input

x = Conv2D(32, (3, 3), activation='relu')(inputs)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Flatten()(x) #1600 neurons
x = Dense(128, activation='relu')(x)#128 neurons


outputs = Dense(10, activation='softmax')(x) #solution 10 neurons


model = tf.keras.Model(inputs=inputs, outputs=outputs)


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.summary()
#sequential not working
#multilayer framework from tensorflow
