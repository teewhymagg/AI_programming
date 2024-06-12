# 22200849, 22207839

# Import necessary libraries and functions from other files
from perceptron import rng 
import numpy as np
from math import exp
from perceptron_image import ideal, generate_samples, transform_data


def sigmoidal(y):
    """
    Sigmoid activation function. Returns: Output after applying the sigmoid activation function
    """
    return 1 / (1 + exp(-y))


class GradientPerceptron:
    def __init__(self, ninp):
        """
        Initialize a GradientPerceptron instance. Parameters - ninp: Number of input neurons
        """
        self.ninp = ninp
        # Initialize weights with small random values
        self.weights = (rng.random(self.ninp + 1) - 1) / 10

    def train(self, trainset, eta=0.01, batch_size=10, maxepoch=10000, patience=25.0, convergence_threshold=1e-6, consecutive_epochs=5):
        """
        Train the perceptron using gradient descent.

        Parameters:
        - trainset: Training dataset
        - eta: Learning rate (default: 0.01)
        - batch_size: Size of mini-batch (default: 10)
        - maxepoch: Maximum number of epochs (default: 10000)
        - patience: Patience for early stopping (default: 25.0)
        - convergence_threshold: Threshold for convergence (default: 1e-6)
        - consecutive_epochs: Number of consecutive epochs for considering convergence (default: 5)

        """
        last_losses = [float('inf')] * consecutive_epochs
        L = len(trainset)
        if batch_size > L:
            batch_size = L
        for e in range(maxepoch):
            delta = np.array([0.0 for _ in range(self.ninp + 1)])
            for i in rng.permutation(range(L))[:batch_size]:
                I = trainset[i][0]
                T = trainset[i][1]
                R = self.out(I)

                # Calculate delta for each weight
                delta[0] = delta[0] + eta * (T - R) * R * (1 - R)
                delta[1:] = delta[1:] + eta * (T - R) * R * (1 - R) * I

            # Update weights using the calculated delta
            self.weights += delta
            # Calculate and update the training loss
            loss = self.loss(trainset)
            last_losses.pop(0)
            last_losses.append(loss)

            if e % 10 == 0:
                print(f"epoch {e}: loss = {loss}")

            # Check for early stopping conditions
            if loss > 150.0:
                continue
            if all(abs(last_losses[i] - last_losses[i + 1]) < convergence_threshold for i in range(consecutive_epochs - 1)) or loss < patience:
                return self.weights
        return self.weights

    def out(self, xs):
        """
        Calculate the output of the perceptron.
        """
        S = self.weights[1:].dot(xs) + self.weights[0]
        o = self.activation(S)
        return o
    
    def out_weights(self, xs, weights):
        """
        Calculate the output of the perceptron with given weights.
        """
        S = weights[1:].dot(xs) + weights[0]
        o = self.activation(S)
        return o

    def activation(self, y):
        """
        Sigmoid activation function. Output after applying the sigmoid activation function
        """
        return 1 / (1 + exp(-y))

    def loss(self, dataset):
        """
        Calculate the loss on the dataset.
        """
        err = 0
        for i in range(len(dataset)):
            xs = dataset[i][0]
            t = dataset[i][1]
            o = self.out(xs)
            # Accumulate squared error for each sample
            err += (t - o) ** 2
        return err / 2

    def test(self, testset, threshold = 0.5):
        """
        Test the perceptron on a test set. Tuple containing counts of positive results, negative results, and others
        """
        print("Testing...")
        positive_result = 0
        negative_result = 0
        others = 0
        for element in range(len(testset)):
            I = testset[element][0]
            T = testset[element][1]
            R = self.out(I)
            # Count results based on threshold (0.5) and compare with the target
            if R >= threshold and T == 1:
                positive_result += 1
            elif R < threshold and T == 0:
                negative_result += 1
            else:
                others += 1
        return positive_result, negative_result, others


if __name__ == "__main__":
    # Define the desired digit for training and testing
    desired_number = 1

    # Create a GradientPerceptron instance with 20 input neurons
    P = GradientPerceptron(20)

    # Generate training data for the desired digit
    train_set = transform_data(generate_samples(ideal, 500), desired_number)

    # Train the perceptron and obtain the trained weights
    weights_of_train = P.train(train_set)

    # Generate test data for all digits
    test_set = generate_samples(ideal, 100)

    # Prepare test data specifically for the desired digit
    result_array = []
    for key, value in test_set.items():
        if key == desired_number:
            for i in range(1, len(value)):
                # Append flattened test samples with label 1 for the desired digit
                result_array.append((np.ravel(value[i]), 1))

    # Test the perceptron on the prepared test data with chosen threshold and print the results
    print(f"{P.test(result_array, threshold=0.5)[0]}: positively identified, {P.test(result_array, threshold=0.5)[1]}: negatevaly identified, {P.test(result_array, threshold=0.5)[2]}: others")

