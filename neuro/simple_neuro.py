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


class Network():
    def __init__(self):
        self.layers_list = []

    def create_layer(self, neurons_number):
        self.layers_list.append([Neuron() for i in range(neurons_number)])

    def link_layers(self):
        for i in range(len(self.layers_list) - 1):
            for j in range(len(self.layers_list[i])):
                for k in range(len((self.layers_list[i + 1]))):
                    self.layers_list[i][j].link()

    def count(self):
        for i in range(len(self.layers_list) - 1):
            for j in range(len(self.layers_list[i])):
                for k in range(len((self.layers_list[i + 1]))):
                    n = self.layers_list[i][j].get_value()
                    weigth = self.layers_list[i][j].list_out_links[k]
                    self.layers_list[i+1][k].give_value(n * weigth)


def activate(x):
    return 1 / (1 + np.exp(-x))


def main():
    nw = Network()
    nw.create_layer(1)
    nw.layers_list[0][0].give_value(2)
    nw.create_layer(4)
    nw.create_layer(1)
    nw.link_layers()
    nw.count()
    print(activate(nw.layers_list[2][0].get_value()))


if __name__ == '__main__':
    main()
