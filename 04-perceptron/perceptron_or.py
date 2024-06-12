# 22200849, 22207839

# Import necessary libraries and functions from other files
import numpy as np
from perceptron import Perceptron, threshold 

# Initialize the random number generator with a seed for reproducibility
rng = np.random.default_rng(123)

# Create a Perceptron instance with 2 inputs and a threshold activation function
P = Perceptron(2, threshold)

# Define a training set for the OR logic gate
set_or = [
    (np.array([0, 0]), 0),
    (np.array([0, 1]), 1),
    (np.array([1, 1]), 1),
    (np.array([1, 0]), 1)
]

# Train the perceptron on the OR logic gate training set
print(P.train(set_or))

# Define a test set for the OR logic gate
test_set_or = [
    (np.array([1, 0]), 1),
]

# Test the perceptron on the OR logic gate test set
# Expecting to get 1
P.test(test_set_or)

