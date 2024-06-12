# 22200836
from z3 import *


# Variables
Am, Br, Ca, Ir = Ints('Am Br Ca Ir')
Butterflies, Dolphins, Horses, Turtles = Ints(
    'Butterflies Dolphins Horses Turtles')
Bowling, Handball, Swimming, Tennis = Ints('Bowling Handball Swimming Tennis')
Black, Blue, Red, White = Ints('Black Blue Red White')

# Creating solver
s = Solver()

s.add([And(1 <= x, x <= 4) for x in [Am, Br, Ca, Ir,
                                     Butterflies, Dolphins, Horses, Turtles,
                                     Bowling, Handball, Swimming, Tennis,
                                     Black, Blue, Red, White]])

# Distinct values
s.add(Distinct([Am, Br, Ca, Ir]))
s.add(Distinct([Butterflies, Dolphins, Horses, Turtles]))
s.add(Distinct([Bowling, Handball, Swimming, Tennis]))
s.add(Distinct([Black, Blue, Red, White]))

# Constraints
s.add(Bowling - 2 == Swimming)
s.add(Ir - 1 == Handball)
s.add(Black == 2)
s.add(Horses + 1 == Red)
s.add(Am == Turtles - 1)
s.add(Bowling > Tennis)
s.add(Handball + 1 == White)

# Output
if s.check() == sat:
    print("Solution found:")
    print(s.model())
else:
    print("No solution found")
