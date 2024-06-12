# 22200849, 22207839

# Import necessary libraries
import numpy as np

# Initialize the random number generator with a seed for reproducibility
rng = np.random.default_rng(123)

# Define a Perceptron class
class Perceptron:
    def __init__(self, ninp, activation):
        # Initialize the perceptron with the number of inputs and the activation function
        self.ninp = ninp
        # Initialize weights with small random values
        self.weights = (rng.random(self.ninp + 1) - 1) / 10
        # Set the activation function for the perceptron
        self.activation = activation

    def out(self, xs):
        # Calculate the weighted sum and apply the activation function
        S = self.weights[1:].dot(xs) + self.weights[0]
        o = self.activation(S)
        return o

    def out_weights(self, xs, weights):
        S = weights[1:].dot(xs) + weights[0] 
        o = self.activation(S)
        return o

    def train(self, trainset):
        # Training parameters
        eta = 0.01
        maxiter = 1000
        # Number of training samples
        L = len(trainset)

        while maxiter > 0:
            oldweights = np.copy(self.weights)

            # Iterate over a random permutation of the training set
            for i in rng.permutation(range(L)):
                I = trainset[i][0]
                T = trainset[i][1]
                R = self.out(I)

                # Update weights if there is a misclassification
                if T != R:
                    self.weights[0] = self.weights[0] + eta * (T - R)
                    self.weights[1:] = self.weights[1:] + eta * (T - R) * I

            # Check for convergence by comparing old and new weights
            if (oldweights == self.weights).all():
                return self.weights

            maxiter = maxiter - 1
        return self.weights

    def test(self, testset):
        print("Testing...")
        Rs = []
        # Test the perceptron on a test set
        for i in range(len(testset)):
            I = testset[i][0]
            T = testset[i][1]
            R = self.out(I)
            Rs.append(R)
            print(f"Input: {I}, Target: {T}, Output: {R}")
        return Rs
    
    def test_weights(self, testset, weights):
        print("Testing...")
        Rs = []
        # Test the perceptron on a test set
        for i in range(len(testset)):
            I = testset[i][0]
            T = testset[i][1]
            R = self.out_weitghts(I, weights)
            Rs.append(R)
            print(f"Input: {I}, Target: {T}, Output: {R}")
        return Rs

# Define a threshold activation function
def threshold(y):
    if y > 0:
        return 1
    if y <= 0:
        return 0

if __name__ == "__main__":
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
        (np.array([1, 1]), 1),
    ]

    # Test the perceptron on the OR logic gate test set
    # Expecting to get 1
    P.test(test_set_or)
