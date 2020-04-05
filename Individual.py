import pyrosim
from ThrowingRobot import ROBOT


class INDIVIDUAL:
    def __init__(self):
        self.fitness = 0

    def start_sim(self):
        self.sim = pyrosim.Simulator( play_blind=False, eval_steps=500, play_paused=True)
        self.robot = ROBOT(self.sim)
        self.sim.start()
        self.sim.wait_to_finish()
