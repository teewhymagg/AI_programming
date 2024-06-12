# 22200849, 22200839

from z3 import *


def unique(s, xs):
    m = s.model()
    for x in xs:
        s.push()
        s.add(x != m.eval(x, model_completion=True))
        if s.check() == sat:
            return False
        s.pop()
    return True


def trial12():
    rs = [Int(f"rs[{i}]") for i in range(9)]
    # rs[i] = 0, if tiger in room i+1
    #         1, if lady in room i+1
    #         2, if room i is empty i+1

    # lady+sign = true
    # tiger+sign = false
    # empty+sign = t/f

    range_cond = [(0 <= r) & (r <= 2) for r in rs]
    one_lady = Sum([If(r == 1, 1, 0) for r in rs]) == 1

    # THE LADY IS IN AN ODD-NUMBERED ROOM
    sign1 = Or([rs[i] == 1 for i in range(9) if i % 2 == 0])
    sign2 = rs[1] == 2  # THIS ROOM IS EMPTY
    sign4 = Not(sign1)  # SIGN I IS WRONG
    sign5 = Or(sign2, sign4)  # EITHER SIGN II OR SIGN IV IS RIGHT
    sign7 = rs[0] != 1  # THE LADY IS NOT IN ROOM I
    # EITHER SIGN V IS RIGHT OR SIGN VII IS WRONG
    sign3 = Or(sign5, Not(sign7))
    sign6 = Not(sign3)  # SIGN III IS WRONG
    # THIS ROOM CONTAINS A TIGER, AND ROOM IX IS EMPTY
    sign8 = And(rs[7] == 0, rs[8] == 2)
    # THIS ROOM CONTAINS A TIGER, AND VI IS WRONG
    sign9 = And(rs[8] == 0, Not(sign6))

    signs = [sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9]
    sign_cond = [Implies(rs[i] == 0, ~signs[i]) & Implies(
        rs[i] == 1, signs[i]) for i in range(9)]  # lady inside -> sign true, tiger -> false

    # if room is empty, no way to found lady
    # non empty, if lady, than room can't contain tiger -> contradiction
    # => tiger in room 8
    sign8_king = rs[7] != 2  # king was decent to tell if room was empty or not

    s = Solver()
    # print(sign_cond)
    s.add(range_cond)
    s.add(one_lady)
    s.add(sign_cond)
    s.add(sign8_king)

    return s, rs


m, xs = trial12()
if m.check() == sat:
    print(m.model())
    while not unique(m, xs):
        print(m.model())
else:
    print("No solution found")
