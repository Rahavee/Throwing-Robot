from builtins import len, range

import pyrosim
import math
import numpy
import random
import constants as c
from ThrowingRobot import ROBOT


class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = numpy.random.randint(100, size=(11, 5))
        self.genome = (self.genome * 0.02) - 1
        self.fitness = 0

    def start_sim(self, pb):
        if pb:
            self.sim = pyrosim.Simulator(play_blind=pb, eval_steps=c.eval)
        if pb == False:
            self.sim = pyrosim.Simulator(play_blind=pb, eval_steps=c.eval, play_paused=True)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def compute_fitness(self):
        self.sim.wait_to_finish()
        O1x = self.sim.get_sensor_data(sensor_id=self.robot.P1x)
        O1y = self.sim.get_sensor_data(sensor_id=self.robot.P1y)
        O2x = self.sim.get_sensor_data(sensor_id=self.robot.P2x)
        O2y = self.sim.get_sensor_data(sensor_id=self.robot.P2y)

        touch_data = self.sim.get_sensor_data(sensor_id=self.robot.sensorList[1])
        distance = 400
        count = 0
        for i in range(c.eval):
            dis_in_i = (((O1x[i] - O2x[i]) ** 2) + ((O1y[i] - O2y[i]) ** 2)) ** 0.5
            if dis_in_i < distance:
                distance = dis_in_i
            if touch_data[i] == 1:
                count = count + 1

        self.fitness = (distance/15) +(count/1000)
        del self.sim

    def mutate(self):
        gene_to_mutate_row = random.randint(0, 10)
        gene_to_mutate_column = random.randint(0, 4)
        self.genome[gene_to_mutate_row][gene_to_mutate_column] = random.gauss(
            self.genome[gene_to_mutate_row][gene_to_mutate_column],
            math.fabs(self.genome[gene_to_mutate_row][gene_to_mutate_column]))
        if self.genome[gene_to_mutate_row][gene_to_mutate_column] > 1:
            self.genome[gene_to_mutate_row][gene_to_mutate_column] = 1
        if self.genome[gene_to_mutate_row][gene_to_mutate_column] < 1:
            self.genome[gene_to_mutate_row][gene_to_mutate_column] = -1

    def Print(self):
        print("[", self.ID, self.fitness, end="")
