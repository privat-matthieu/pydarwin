# Pydarwin
A simple genetic algorithm designed to take user input for parameters such as a population size, the percentage of a population considered "elite", and the number of iterations of the algorithm to naturally find the most optimal result based on a fitness function.

## Getting Pydarwin Into Your Project
To use Pydarwin, you must first install it.

```bash
pip install pydarwin
```

To use Pydarwin to its fullest extent, the following imports are required:

```python
from pydarwin import GA
from pydarwin.ChromosomeSpecifications import ChromosomeSpecifications
```

## Example Of Use - A Simple Cannon
To demonstrate the use of Pydarwin, we can look at a simple cannon using basic principles of ballistics to find the optimal shot power and angle of fire to hit a defined target.

### Cannon Set-Up
Before we can implement Pydarwin's features, we must first define two basic things for this example: the target's location and the equation for projectile range. Here we define our target to be at d = 500.

```python
# The target's location
d = 500

# Range equation
# R = ((V0)^2 * (sin(2*Theta))) / g

def rangeEquation(power, theta):
    R = ((power**2) * (math.sin(math.radians(2 * theta)))) / 9.81
    return R
```

### Using Pydarwin To Hit The Target
The processes of finding the optimal target requires two steps. First, we must define what our chromosomes shall be. Second, we must define our fitness function that will analyze the different chromosomes.

Step 1:

```python
# Step 1: Define Chromosomes (Here is the Power/Angle and their ranges)
cs = ChromosomeSpecifications()
cs.add("power", 0, 100)
cs.add("theta", 0, 90)
```

All chromosomes that are created have three things associated with them. When adding new chromosomes, you must define a name for the chromosome (in this case they are "power" and "theta"), a minimum value, and a maximum value. In this example, the power and angle each have their own ranges that they may operate within. These numbers can be changed however you see fit.

Step 2:

```python
# Step 2: Define the fitness of the chromosomes
def fitness(c):
    power = c["power"]
    theta = c["theta"]
    
    R = rangeEquation(power, theta)
    distOff = abs(d - R)
    
    if(distOff == 0):
        return sys.float_info.max
    else:
        return abs(1 / distOff)
```

In the second step, we create our fitness function. This is the function that shall define what constitutes an "optimum" chromosome. We start this fitness function by bringing our created chromosomes (c), and giving them the names "power" and "theta" to distinguish them.

Next we call our range equation defined before we began using Pydarwin, using our chromosomes as arguments. This will allow the fitness function to see the various values for the power and angle created by our chromosomes.

In this case, we want our optimal point to be the one that hits closest to our target (d). The way Pydarwin is built, the genetic algorithm will naturally take the chromosome with the highest value as the optimal, so we must return the inverse of our distance here. This way, the chromosome that hits closest to our target shall be considered the "largest" value by the algorithm. If we happen to hit exactly where we want, we return instead the highest possible float that we are able to. In this way, nothing could ever beat it since it is already the highest possible value, and shall be taken as our optimal chromosome.

### Running Pydarwin

To run Pydarwin and allow the genetic algorithm to find the optimal chromosome for you, you simply need to run GA.solve, as shown:

```python
result = GA.solve(cs, fitness, 2000, 0.2, 2000)
```

The solve() method takes for parameters the chromosome specifications that you defined in Step 1 of Using Pydarwin (in this example they are cs), the fitness function that you defined in Step 2 of Using Pydarwin, the size of the population, the percentage (in decimal) of chromosomes that shall be considered "elite", and the number of iterations of the fitness function.

What is happening in the solve() method at a glance:

1. Create a population made up of chromosomes using the defining properties created until we reach the population size defined in the solve() method's parameters.

2. A for-loop is created that will loop until the number of iterations defined has been reached.

3. In the loop, we begin by sorting the population based on the fitness function, with the most optimal chromosome being placed at index 0.

4. We then take the elite chromosomes. In this case, we define the elite to be considered as the best 20% of chromosomes.

5. From the elite, we create a new population by combining elements of the elite chromosomes, until we once again reach the population size defined.

6. Repeat until the number of iterations has been reached.

7. Return our best chromosome (located in index 0 after we sort the array of chromosomes).

The solve() method and the methods it uses can be found in GA.py, located in the Pydarwin public Github repository.