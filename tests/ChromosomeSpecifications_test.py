import random
import unittest

from pydarwin.ChromosomeSpecifications import ChromosomeSpecifications


class ChromosomeSpecificationsTest(unittest.TestCase):
    def test_add(self):
        cs = ChromosomeSpecifications()

        cs.add("Bob", 1, 5)
        specs = cs.specs

        self.assertEqual(1, len(specs))
        self.assertIsNotNone(specs["Bob"])
        self.assertEqual(1, specs["Bob"][0])
        self.assertEqual(5, specs["Bob"][1])

    def test_make_new(self):
        random.seed(0)

        cs = ChromosomeSpecifications()
        cs.add("Alice", 1, 5)
        cs.add("Eve", 1, 5)

        c = cs.make_new()

        self.assertEqual(2, len(c))
        self.assertIsNotNone(c["Alice"])
        self.assertIsNotNone(c["Eve"])
        self.assertEqual(4.3776874061001925, c["Alice"])
        self.assertEqual(4.03181761176121, c["Eve"])
