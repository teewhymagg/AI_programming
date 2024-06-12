# 22200849, 22207839

# Import classes and functions from other files
from perceptron_gradient import GradientPerceptron
from digits_recognition_network import Network
from perceptron_image import transform_data, generate_samples, ideal
import numpy as np
import pickle
import os

class GradientNetwork(Network):
    def __init__(self, num_perceptrons, n_inputs_perceptron):
        # Initialize a neural network with gradient perceptrons.
        self.perceptrons = []
        for _ in range(num_perceptrons):
            # Create and append Gradient Perceptrons to the network
            self.perceptrons.append(GradientPerceptron(n_inputs_perceptron))

    def train(self, train_data):
        """
        Train each perceptron in the network using the provided training data.
        """
        weights = []

        for perceptron in range(10):
            # Train each perceptron in the network with gradient descent
            weights.append(self.perceptrons[perceptron].train(train_data[perceptron], eta=0.1, batch_size=10, maxepoch=5000, patience=20.0, convergence_threshold=0.0001, consecutive_epochs=5))

        return weights
    
    def accuracy_test(self, test_data, weights):
        """
        Evaluate the accuracy of the network using test data and return metrics. Returns tuple containing true positive, true negative, false positive, and false negative counts
        """
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        for key, value in test_data.items():
            for each_digit in value:
                for perceptron in range(10):
                    if self.perceptrons[perceptron].out_weights(each_digit, weights[perceptron]) >= 0.5 and perceptron == key:
                        true_positive += 1
                    if self.perceptrons[perceptron].out_weights(each_digit, weights[perceptron]) >= 0.5 and perceptron != key:
                        false_positive += 1
                    if self.perceptrons[perceptron].out_weights(each_digit, weights[perceptron]) < 0.5 and perceptron == key:
                        false_negative += 1
                    if self.perceptrons[perceptron].out_weights(each_digit, weights[perceptron]) < 0.5 and perceptron != key:
                        true_negative += 1
        return true_positive, true_negative, false_positive, false_negative


if __name__ == "__main__":
    weights_file_path = 'network_perceptron_sigmoidal_weights.pkl'

    if not os.path.exists(weights_file_path):
        # Generate training data for all digits
        train_data_all = {}

        for i in range(10):
            train_data_all[i] = transform_data(generate_samples(ideal, 500), i)

        # Create a neural network with 10 input neurons and 20 inputs
        net = GradientNetwork(10, 20)

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
    print("Sigmoidal Network")
    print(*net.calculate_metrics(*net.accuracy_test({k: [np.ravel(data) for data in v] for (k, v) in generated_test_data.items()}, weights=loaded_weights)), sep="\n")
