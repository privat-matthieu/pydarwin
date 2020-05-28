import sys

from pydarwin import GA
from pydarwin.ChromosomeSpecifications import ChromosomeSpecifications

cs = ChromosomeSpecifications()
cs.add("x", -10, 10)
cs.add("y", -10, 10)


def fitness(c):
    x = c["x"]
    y = c["y"]

    f = (x - 2)**2 - (y - 3)**2

    if(f == 0):
        return sys.float_info.max
    else:
        return abs(1 / f)


result = GA.solve(cs, fitness, 1000, 0.34, 2000)

x = result["x"]
y = result["y"]

f = (x - 2)**2 - (y - 3)**2

print(result, f)
