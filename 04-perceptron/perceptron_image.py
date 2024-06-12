# 22200849, 22207839

# Import necessary libraries
import numpy as np
import pickle
import os
from digits_recognition_network import Network  # 'digits_recognition_network.py' contains Network class

# Ideal representations of digits
ideal = {
    0: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]],

    1: [[0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]],

    2: [[0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 1, 1]],

    3: [[0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0]],

    4: [[1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]],

    5: [[1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0]],

    6: [[0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]],

    7: [[1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]],

    8: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]],

    9: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 0]]
}


def generate_samples(ideal, num_samples):
    """
    Generate random samples based on ideal representations with some noise.
    """
    data = {}

    for i in ideal.keys():
        data[i] = [np.array(ideal[i])]
        for _ in range(num_samples - 1):
            new_digit = np.array(ideal[i]) + np.random.normal(0., 0.5, size=np.shape(ideal[i]))
            data[i].append(new_digit.tolist())

    return data


def transform_data(generated_data, desired_number):
    """
    Transform generated data into a format suitable for training.
    """
    result_array = []
    for key, value in generated_data.items():
        if key == desired_number:
            for i in range(1, len(value)):
                result_array.append((np.ravel(value[i]), 1))
        else:
            for i in range(1, int(len(value) / 4)):
                result_array.append((np.ravel(value[i]), 0))
    return result_array


if __name__ == "__main__":
    weights_file_path = 'network_perceptron_threshold_weights.pkl'

    if not os.path.exists(weights_file_path):
        # Generate training data for all digits
        train_data_all = {}

        for i in range(10):
            train_data_all[i] = transform_data(generate_samples(ideal, 500), i)

        # Create a neural network with 10 input neurons and 20 inputs
        net = Network(10, 20)

        # Train the network using the generated training data
        weights = net.train(train_data_all)

        # Save the weights to a pickle file
        with open(weights_file_path, 'wb') as file:
            pickle.dump(weights, file)
    else:
        print("Using existing weights file for testing.")

    # weights from the pickle file
    with open(weights_file_path, 'rb') as file:
        loaded_weights = pickle.load(file)

    # test data for all digits
    generated_test_data = generate_samples(ideal, 10)

    # neural network with 10 input neurons and 20 inputs
    net = Network(10, 20)

    # calculating and printint metrics on the accuracy of the network on the generated test data
    print("Treshold Network")
    print(*net.calculate_metrics(*net.accuracy_test({k: [np.ravel(data) for data in v] for (k, v) in generated_test_data.items()}, weights=loaded_weights)), sep="\n")
