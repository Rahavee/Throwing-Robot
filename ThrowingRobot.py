import pyrosim
import constants as c
import random


class ROBOT:
    def __init__(self, sim):
        self.send_objects(sim)
        self.send_joints(sim)

    def send_objects(self, sim):
        self.O0 = sim.send_box(position=(0,0,c.blockHeight / 2), sides=(c.blockLength, c.blockWidth,c.blockHeight), color=(1,0,0),density=5)
        self.O1 = sim.send_cylinder(position=(0,0,c.blockHeight + c.arm1Height / 2), length=c.arm1Height, radius=c.radius,
                                    color=(0,1,0),orientation=(0,0, 1))
        self.O2 = sim.send_cylinder(position=(0,0,c.blockHeight+c.arm1Height+c.arm2Height/2), length =c.arm2Height, radius=c.radius,color=(1,0,1), orientation=(0,0,1))
        self.O3 = sim.send_box(position=(0,0,c.blockHeight+c.arm1Height+c.arm2Height+c.handHeight/2), sides=(c.handLength,c.handLength,c.handHeight), color=(0,0,1))
        self.O4 = sim.send_sphere(position=(0,0,c.blockHeight+c.arm1Height+c.arm2Height+c.handHeight+c.ballRadius), radius=c.ballRadius, color=(0.5,0.5,0.5))
        self.O5 = sim.send_box(position=(c.handLength/3,c.handLength/2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.handHeight/2),
                               sides=(c.handHeight, c.handHeight, c.handLength), color=(0,0,1))
        self.O6 = sim.send_box(position=(-c.handLength/3,c.handLength/2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.handHeight/2),
                               sides=(c.handHeight, c.handHeight, c.handLength), color=(0,0,1))

    def send_joints(self, sim):
        self.jointList = {}
        self.jointList[0] = sim.send_ball_and_socket_joint(self.O0, self.O1, anchor=(0,0,c.blockHeight))
        self.jointList[1]=sim.send_hinge_joint(self.O1, self.O2, anchor=(0,0,c.blockHeight+c.arm1Height), axis=(1,0,0))
        self.jointList[2]= sim.send_ball_and_socket_joint(self.O2, self.O3, anchor=(0,0,c.blockHeight+c.arm1Height+c.arm2Height))
        self.jointList[3]=sim.send_hinge_joint(self.O3, self.O5, anchor=(c.handLength/3,c.handLength/2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight ), axis=(1,0,0))
        self.jointList[3] = sim.send_hinge_joint(self.O3, self.O6, anchor=(-c.handLength /3, c.handLength / 2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight), axis=(1, 0, 0))



