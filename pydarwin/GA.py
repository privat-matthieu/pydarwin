import math
import random

from pydarwin.ChromosomeSpecifications import ChromosomeSpecifications


def solve(chromosome_specs: ChromosomeSpecifications, fitness_function, population_size: int, elite_ratio: float, iterations: int):
    """ Executes the genetic optimization of the given chromosomes.

    Args:
        chromosome_specs: A description of the composition of chromosomes.
        fitness_function: abc
        population_size: The size of the population.
        elite_ratio: The top percentage of chromosomes to be returned. Value between 0 and 1.
        iterations: The number of times the program will loop.
    """
    population = make_population(chromosome_specs, population_size)

    for i in range(0, iterations):
        sort_population(population, fitness_function)
        elite = elite_selection(population, elite_ratio)
        population = crossover(elite, population_size)

    return elite[0]


def make_population(chromosome_specs: ChromosomeSpecifications, population_size):
    result = []
    for i in range(0, population_size):
        c = chromosome_specs.make_new()
        result.append(c)

    return result


def sort_population(population, fitness_function):
    for c in population:
        s = fitness_function(c)
        c["__score__"] = s

    population.sort(key=lambda c: c["__score__"], reverse=True)


def elite_selection(population, elite_ratio):
    eliteIndex = math.floor(elite_ratio * len(population))

    return population[: eliteIndex]


def crossover(elite, population_size):
    result = []
    for i in range(0, population_size):
        subject1 = random.choice(elite)
        subject2 = random.choice(elite)

        cut = random.random() * len(subject1)

        counter = 0

        offspring = {}
        for name in subject1:
            offspring[name] = subject1[name] if counter < cut else subject2[name]
            counter += 1

        result.append(offspring)

    return result
