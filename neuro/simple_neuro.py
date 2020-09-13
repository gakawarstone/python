import numpy as np
import random


class Neuron():
    def __init__(self):
        self.list_out_links = []
        self.list_input_values = []

    def get_value(self):
        outp = 0
        for i in self.list_input_values:
            outp += i
        return outp

    def give_value(self, value):
        """
        value must be a number
        """
        self.list_input_values.append(value)

    def link(self, weight=None):
        """
        weight is float from -1 to 1
        """
        if not weight:
            weight = random.uniform(-1, 1)
        self.list_out_links.append(weight)


def activate(x):
    return 1 / (1 + np.exp(-x))
