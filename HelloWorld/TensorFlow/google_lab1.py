import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])]) # create simple network
model.compile(optimizer='sgd', loss="mean_squared_error") # stochastic gradient decent for the optimizer

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float) # adding the data
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# model.fit(xs, ys, epochs=50) # running the model

print(model.predict([10.0])) # predicting the probability of 31. So it calculated that there is a very high probability
# that the relationship between X and Y is Y=3X+1, but it can't know for sure with only six data points



