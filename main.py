from Individual import INDIVIDUAL
from population import POPULATION
import matplotlib.pyplot as plt
import random
import pickle
import copy
import constants as c
from ThrowingRobot import ROBOT

parents = POPULATION(20)
parents.Evaluate(True)


for j in range(0,1000):
    print(j, end="")
    parents.Print()
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)

parents.Evaluate(False)
f= open('best.p','wb')
pickle.dump(parents,f)
f.close()
