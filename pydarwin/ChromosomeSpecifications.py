import random


class ChromosomeSpecifications:
    def __init__(self):
        self.specs = {}

    def add(self, name, min, max):
        self.specs[name] = (min, max)

    def make_new(self):
        result = {}

        for name in self.specs:
            min = self.specs[name][0]
            max = self.specs[name][1]
            result[name] = random.uniform(min, max)

        return result
