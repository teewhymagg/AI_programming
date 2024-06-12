# 22208430

import math
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
        return self.op(self.left.ev(env), self.right.ev(env))

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
    op = lambda self, x, y: x / y

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
            return Con(-val.val)  # If the operand is already negative, make it positive.

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


ex1 = Add(Mul(Con(2.5), Var("x1")), Var("x2"))
env = {"x1": 2, "x2": -1}
ex2 = Add(Con(2.5), Con(-2.5))
ex3 = Mul(Var("x1"), Con(1))
x1 = Var("x1")
x2 = Var("x2")
one = Con(1.0)
half = Con(0.5)
zero = Con(0)
ex4 = Sub(Var("x1"), Con(3.0))
ex5 = Div(Var(x1), Con(2))
ex6 = Neg(Var(x1))
print(ex6)
ex7 = Exp(Var(x2))
print(ex7)
ex8 = Div(Con(1.0), Add(Exp(Neg(x2)), Con(1)))
print(ex8)
