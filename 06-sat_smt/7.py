# 22200836
from z3 import *

def trial7():
    r1, r2 = Bools("r1 r2")

    sign2 = r1
    sign1 = r1 != r2

    s = Solver()

    cond1 = r1 == sign1
    cond2 = r2 != sign2

    s.add(cond1, cond2)

    return s, [r1, r2]



def unique(s, xs):
    m = s.model()
    for x in xs:
        s.push()
        s.add(x != m.eval(x, model_completion=True))
        if s.check() == sat:
            return False
        s.pop()
    return True


solver, variables = trial7()

if solver.check() == sat:
    # Extract the model (solution)
    model = solver.model()
    r1_val = model.evaluate(variables[0])
    r2_val = model.evaluate(variables[1])

    # Check for uniqueness
    is_unique = unique(solver, variables)

    # Print the results
    print("Room I has a lady:", is_true(r1_val))
    print("Room II has a lady:", is_true(r2_val))
    print("Is the solution unique:", is_unique)
else:
    print("No solution found")
