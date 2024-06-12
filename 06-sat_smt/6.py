# Author: [22211514]

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

def trial6():
    r1, r2 = Bools("r1 r2")

    sign1 = r1 == r2  # both rooms have the same outcome
    sign2 = r2       # there is a lady in room 2

    s = Solver()

    # both signs are either true or false
    s.add(sign1 == sign2)

    if s.check() == sat:
        m = s.model()
        solution = (is_true(m[r1]), is_true(m[r2]))
        return s, [r1, r2], solution
    else:
        return None, None, "No solution"

# output
solver, variables, solution = trial6()

if solver and variables:
    print(f"Solution: Room 1 contains {'Lady' if solution[0] else 'Tiger'}, Room 2 contains {'Lady' if solution[1] else 'Tiger'}")
    print("Is the solution unique?", unique(solver, variables))
else:
    print(solution)
