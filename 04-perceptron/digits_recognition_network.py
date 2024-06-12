# 22200849, 22207839
# this file only provides a class
# Import class and function from Perceptron
from perceptron import Perceptron, threshold

class Network:
    def __init__(self, num_perceptrons, n_inputs_perceptron):
        """
        Initialize a neural network with multiple perceptrons.

        Parameters:
        - num_perceptrons: Number of perceptrons in the network
        - n_inputs_perceptron: Number of inputs for each perceptron
        """
        self.perceptrons = []
        for _ in range(num_perceptrons):
            # Create and append Perceptron instances to the network
            self.perceptrons.append(Perceptron(n_inputs_perceptron, threshold))

    def train(self, train_data):
        """
        Train each perceptron in the network using the provided training data.

        Parameters:
        - train_data: List of training data for each perceptron
        """
        weights = []

        for i in range(10):
            # Train each perceptron in the network
            weights.append(self.perceptrons[i].train(train_data[i]))

        return weights


    def accuracy_test(self, test_data, weights):
        """
        Evaluate the accuracy of the network using test data and return metrics.

        Parameters:
        - test_data: Dictionary containing test data for each digit

        Returns:
        - Tuple containing true positive, true negative, false positive, and false negative counts
        """
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        for key, value in test_data.items():
            for each_digit in value:
                for i in range(10):
                    if self.perceptrons[i].out_weights(each_digit, weights[i]) == 1 and i == key:
                        true_positive += 1
                    if self.perceptrons[i].out_weights(each_digit, weights[i]) == 1 and i != key:
                        false_positive += 1
                    if self.perceptrons[i].out_weights(each_digit, weights[i]) == 0 and i == key:
                        false_negative += 1
                    if self.perceptrons[i].out_weights(each_digit, weights[i]) == 0 and i != key:
                        true_negative += 1
        return true_positive, true_negative, false_positive, false_negative

    def calculate_metrics(self, TP, TN, FP, FN):
        """
        Calculate precision, recall, and F1 score based on true positive, true negative, false positive, and false negative. 
        It returns tuple containing precision, recall, and F1 score as percentage strings.

        Where:
        - TP: True positive count
        - TN: True negative count
        - FP: False positive count
        - FN: False negative count
        """
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        F1 = (2 * precision * recall) / (precision + recall)
        return "Precision: " + str(round(precision * 100, 2)) + "%", "Recall: " + str(round(recall * 100, 2)) + "%", "F1: " + str(round(F1 * 100, 2)) + "%"
