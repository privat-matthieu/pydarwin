import random
import unittest

from pydarwin import GA
from pydarwin.ChromosomeSpecifications import ChromosomeSpecifications


class GATest(unittest.TestCase):
    def test_make_population(self):
        random.seed(0)

        cs = ChromosomeSpecifications()
        cs.add("X", 0, 1)
        cs.add("Y", 0, 1)

        result = GA.make_population(cs, 5)

        self.assertEqual(5, len(result))

    def test_sort_population(self):
        random.seed(0)

        p = [{
            "X": 1
        }, {
            "X": 2000
        }, {
            "X": 500
        }]

        def fitness(c):
            return (1 + c["X"])

        GA.sort_population(p, fitness)

        self.assertEqual(2000, p[0]["X"])
        self.assertEqual(500, p[1]["X"])
        self.assertEqual(1, p[2]["X"])

    def test_elite_selection(self):
        p = [{
            "X": 1
        }, {
            "X": 2000
        }, {
            "X": 500
        }]

        p = GA.elite_selection(p, 0.67)

        self.assertEqual(2, len(p))
        self.assertEqual(1, p[0]["X"])
        self.assertEqual(2000, p[1]["X"])

    def test_crossover(self):
        random.seed(0)

        p = [{
            "X": 1,
            "Y": 2
        }, {
            "X": 2000,
            "Y": 4000
        }, {
            "X": 500,
            "Y": 1000
        }]

        p = GA.crossover(p, 6)

        self.assertEqual(6, len(p))
        self.assertEqual(2000, p[0]["X"])
        self.assertEqual(4000, p[0]["Y"])
