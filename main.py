from Individual import INDIVIDUAL
from population import POPULATION
import matplotlib.pyplot as plt
import random
import pickle
import copy
import constants as c
from ThrowingRobot import ROBOT

parents = POPULATION(1)
parents.Evaluate(False)


# for j in range(0,1):
#     print(j, end="")
#     parents.Print()
#     children = copy.deepcopy(parents)
#     children.Mutate()
#     children.Evaluate(True)
#     parents.ReplaceWith(children)
#     parents.fitness_graph()
#
# parents.Evaluate(False)



