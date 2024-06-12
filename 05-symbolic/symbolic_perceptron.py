# Author: [22211514]

import math
import random  

class Expr:
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Con(other)
        return Add(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Con(other)
        return Mul(self, other)

    def simplify(self):
        return self
    
    def __neg__(self):
        return Neg(self)  
    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Con(other)
        return Div(self, other)


class Con(Expr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"{self.val}"

    def __eq__(self, other):
        if isinstance(other, Con):
            return self.val == other.val
        return False

    def ev(self, env):
        return self

    def diff(self, name):
        return Con(0)

    def vs(self):
        return []


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def ev(self, env):
        return Con(env[self.name])

    def diff(self, name):
        return Con(1 if self.name == name else 0)

    def __eq__(self, other):
        if isinstance(other, Var):
            return self.name == other.name
        return False

    def vs(self):
        return [self.name]


class BinOp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.name} {self.right})"

    def ev(self, env):
        left_val = self.left.ev(env).val
        right_val = self.right.ev(env).val
        return Con(self.op(left_val, right_val))

    def __eq__(self, other):
        if isinstance(other, BinOp):
            return self.name == other.name and self.left == other.left and self.right == other.right
        return False

    def vs(self):
        return self.left.vs() + self.right.vs()


class Add(BinOp):
    name = "+"
    op = lambda self, x, y: x + y

    def diff(self, name):
        return self.left.diff(name) + self.right.diff(name)

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if left.vs() == []:
            left = left.ev({})
        if right.vs() == []:
            right = right.ev({})

        if isinstance(left, Con) and isinstance(right, Con):
            return Con(left.val + right.val)

        if left == Con(0):
            return right

        if right == Con(0):
            return left

        return left + right


class Mul(BinOp):
    name = "*"
    op = lambda self, x, y: x * y

    def diff(self, name):
        f = self.left
        f1 = f.diff(name)
        g = self.right
        g1 = g.diff(name)

        return f1 * g + f * g1

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if left.vs() == []:
            left = left.ev({})
        if right.vs() == []:
            right = right.ev({})

        if isinstance(left, Con) and isinstance(right, Con):
            return Con(left.val * right.val)

        if left == Con(0) or right == Con(0):
            return Con(0)

        if left == Con(1):
            return right

        if right == Con(1):
            return left

        return left * right

class Sub(BinOp):
    name = "-"
    op = lambda self, x, y: x - y

    def diff(self, name):
        return self.left.diff(name) - self.right.diff(name)

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if left.vs() == []:
            left = left.ev({})
        if right.vs() == []:
            right = right.ev({})

        if isinstance(left, Con) and isinstance(right, Con):
            return Con(left.val - right.val)

        if left == Con(0):
            return -right

        if right == Con(0):
            return left

        return left - right


class Div(BinOp):
    name = "/"
    op = lambda self, x, y: x / y if y != 0 else float('inf')

    def diff(self, name):
        f = self.left
        f1 = f.diff(name)
        g = self.right
        g1 = g.diff(name)

        return (f1 * g - f * g1)/(g*g)

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if left.vs() == []:
            left = left.ev({})
        if right.vs() == []:
            right = right.ev({})

        if isinstance(left, Con) and isinstance(right, Con):
            return Con(left.val / right.val)

        if left == Con(0) or right == Con(0):
            return Con(0)

        if left == Con(1):
            return right

        if right == Con(1):
            return left

        return left / right


class UnOp(Expr):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"({self.val})"

    def ev(self, env):
        return self.op(self.val.ev(env))

    def vs(self):
        return self.val.vs()

class Neg(UnOp):
    def __init__(self, val):
            super().__init__(val)
            self.name = "~"

    name = "~"

    op = lambda self, x: -1 * x

    def diff(self, name):
        f = self.val
        f1 = f.diff(name)
        return -1 * f1

    def simplify(self):
        val = self.val
        if val.vs() == []:
            val = val.ev({})

        if val.val < 0:
            return Con(-val.val)  

        if val == Con(0):
            return Con(0)

        return -1 * val

    def __str__(self):
        if isinstance(self.val, Con) and self.val.val < 0:
            return str(-self.val.val)
        return f"-{self.val}"

class Exp(UnOp):
    name = "e^"

    op = lambda self, x: math.exp(x)

    def diff(self, name):
        f = self.val
        f1 = f.diff(name)
        return self.op(f) * f1

    def simplify(self):
        val = self.val
        if val.vs() == []:
            val = val.ev({})
        return math.exp(val)
    def __str__(self):
        return f"e^({str(self.val)})"
    
def linear(xs):
    s = Var("w0") # bias
    for i in range(len(xs)):
        s = s + Var(f"w{i+1}")*xs[i]
    return s
def sigmoid(xs):
    s = Var("w0")  # bias
    for i, x in enumerate(xs):
        s = s + Var(f"w{i+1}") * x
    return Con(1) / (Exp(-s) + Con(1))  



class P():
    def __init__(self, ninp, sigma, weights=None):
        self.ninp = ninp    # number of inputs
        self.sigma = sigma  # input vector -> symbolic expression
        self.weights = {}   # environment for parameters
        vals = weights if weights else [random.uniform(-0.1, 0.1) for _ in range(self.ninp + 1)]
        for i in range(self.ninp + 1):  # ninp weights and a bias
            self.weights[f"w{i}"] = vals[i]
                         
    def output(self, inp):
        activation = self.sigma([Con(x) for x in inp]).ev(self.weights)
        if not isinstance(activation, Con):
            raise TypeError("Activation function did not return a constant value.")
        return activation.val

    def loss(self, dataset):
        err = 0
        for xs, t in dataset:
            o = self.output(xs)
            err += (t - o) ** 2
        return err / len(dataset)

    def train(self, trainset, patience=20):
        maxepoch = 100000
        batchsize = 20
        alpha = 1e-3
        best_loss = float('inf')
        epochs_without_improvement = 0

        for e in range(maxepoch):
            for _ in range(batchsize):
                xs, t = random.choice(trainset)
                updates = {}
                for w in self.weights.keys():
                    output = self.output(xs)
                    expected = float(t)  
                    diff_result = self.sigma([Con(x) for x in xs]).diff(w).ev(self.weights)
                    if not isinstance(diff_result, Con):
                        raise TypeError("Differentiation did not return a constant value.")
                    grad = (output - expected) * diff_result.val  
                    updates[w] = -alpha * grad
                for w in self.weights.keys():
                    self.weights[w] += updates[w]
            if e % 10 == 0:
                print(f"epoch {e}: loss = {self.loss(trainset)}")
            current_loss = self.loss(trainset)
            if e % 10 == 0:
                print(f"epoch {e}: loss = {current_loss}")

            # early stopping logic
            if current_loss < best_loss:
                best_loss = current_loss
                epochs_without_improvement = 0
            else:
                epochs_without_improvement += 1
                if epochs_without_improvement >= patience:
                    print(f"Stopping early at epoch {e} due to no improvement in loss.")
                    break
# testing the implementation
# simple dataset
dataset = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]  

# initialize perceptron with linear activation function
perceptron = P(ninp=2, sigma=linear)

perceptron.train(dataset)

# evaluate and inspect outputs
loss = perceptron.loss(dataset)
print(f"Final loss: {loss}")

test_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
for inp in test_inputs:
    output = perceptron.output(inp)
    print(f"Input: {inp}, Output: {output}")

x1 = Con(0.5)  
x2 = Con(0.7)  

# linear function
linear_expr = linear([x1, x2])
print("This is the linear expression:", linear_expr) 

# sigmoid function
sigmoid_expr = sigmoid([x1, x2])
print("This is the sigmoidal expression:", sigmoid_expr)  
