# 22200849, 22207839

# Import necessary libraries and functions from other files
import numpy as np
from perceptron import Perceptron, threshold

# Create a Perceptron instance with 2 inputs and a threshold activation function
P = Perceptron(2, threshold)

# Define a training set for the AND logic gate
set_and = [
    (np.array([0, 0]), 0),
    (np.array([0, 1]), 0),
    (np.array([1, 0]), 0),
    (np.array([1, 1]), 1),
]

# Train the perceptron on the AND logic gate training set
print(P.train(set_and))

# Define a test set for the AND logic gate
test_set_and = [
    (np.array([0, 1]), 0)
]

# Attempting to force incorrect behavior.
# Expecting to see 0 as the output
print(P.test(test_set_and))
