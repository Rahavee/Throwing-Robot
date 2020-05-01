from Individual import INDIVIDUAL
import constants as c
import copy
import random

class POPULATION:
    def __init__(self, pop_size):
        self.p={}
        self.pop_size=pop_size
        for i in range(0, self.pop_size):
            self.p[i] = INDIVIDUAL(i)

    def Print(self):
        for i in self.p:
            if (i in self.p):
                self.p[i].Print()
        print()

    def Evaluate(self, pb):
        for i in self.p:
            self.p[i].fitness = 0
        for i in self.p:
            self.p[i].start_sim(pb)
        for i in self.p:
            self.p[i].compute_fitness()

    def Mutate(self):
        for i in self.p:
            self.p[i].mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness>other.p[i].fitness:
                self.p[i]=other.p[i]

    def fitness_graph(self):
        self.graph = []
        for i in self.p:
            low = 30
            if self.p[i].fitness<low:
                low = self.p[i].fitness
                self.graph.append(low)

