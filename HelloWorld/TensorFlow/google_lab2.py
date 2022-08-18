import tensorflow as tf
import matplotlib.pyplot as plt

# print(tf.__version__) TensorFlow version

mnist = tf.keras.datasets.fashion_mnist # loading api dataset
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

plt.imshow(training_images[0])

#print(training_labels[0])
#print(training_images[0])

training_images = training_images / 255.0 #normalising the data
test_images = test_images / 255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

# SEQUENTIAL - defines a sequence of layers in the NN
# FLATTEN - creates a one-dimensional array
# DENSE - adds a layer of neurons
# ACTIVATION - functions tell each layer of neurons what to do
# RELU - of X is greater than 0 return X, else return 0
# SOFTMAX - Picks the largest value from a set