from Individual import INDIVIDUAL
from population import POPULATION
import matplotlib.pyplot as plt
import random
import pickle
import copy
import constants as c
from ThrowingRobot import ROBOT

f = open ('best.p', 'rb')
best = pickle.load(f)
f.close()

best.p[1].start_sim(False)
