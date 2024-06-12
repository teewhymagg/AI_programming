# 22208430
from z3 import *
def trial10():

    r1, r2, r3 = Bools("r1 r2 r3")
    # ri True means there is a lady in room i
    # ri False --> tiger!
    # one_lady = (r1 & ~r2 & ~r3) | (~r1 & ~r2 & r3) | (~r1 & r2 & ~r3)
    one_lady = Sum([If(r, 1, 0) for r in [r1, r2, r3]]) == 1

    sign1 = Not(r2)
    sign2 = Not(r2)
    sign3 = Not(r1)

    one_sign = (sign1 & sign2 & ~sign3) | (sign1 & ~sign2 & sign3) | (~sign1 & sign2 & sign3) | (sign1 & ~sign2 & ~sign3) | (~sign1 & ~sign2 & sign3) | (~sign1 & sign2 & ~sign3)
    # one_sign = Sum([If(sign, 1, 0) for sign in [sign1, sign2, sign3]]) <= 1
    print(one_sign)
    s = Solver()
    s.add(one_lady)
    s.add(one_sign)

    return s, [r1, r2, r3]


m, xs = trial10()
if m.check() == sat:
    print(m.model())
    while not unique(m, xs):
        print(m.model())
else:
    print("No solution found")
