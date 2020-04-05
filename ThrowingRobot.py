from builtins import range, len

import pyrosim
import constants as c
import random


class ROBOT:
    def __init__(self, sim):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim)

    def send_objects(self, sim):
        self.O0 = sim.send_box(position=(0,0,c.blockHeight / 2), sides=(c.blockLength, c.blockWidth,c.blockHeight), color=(1,0,0),density=5, collision_group="throw")
        self.O1 = sim.send_cylinder(position=(0,0,c.blockHeight + c.arm1Height / 2), length=c.arm1Height, radius=c.radius,
                                    color=(0,1,0),orientation=(0,0, 1), collision_group="throw")
        self.O2 = sim.send_cylinder(position=(0,0,c.blockHeight+c.arm1Height+c.arm2Height/2), length =c.arm2Height, radius=c.radius,color=(1,0,1), orientation=(0,0,1), collision_group="throw")
        self.O3 = sim.send_box(position=(0,0,c.blockHeight+c.arm1Height+c.arm2Height+c.handHeight/2), sides=(c.handLength,c.handLength,c.handHeight), color=(0,0,1), collision_group="throw")
        self.O4 = sim.send_sphere(position=(0,0,c.blockHeight+c.arm1Height+c.arm2Height+c.handHeight+c.ballRadius), radius=c.ballRadius, color=(0.5,0.5,0.5), collision_group="throw")
        self.O5 = sim.send_box(position=(c.handLength/3,c.handLength/2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.handHeight/2),
                               sides=(c.handHeight, c.handHeight, c.handLength), color=(0,0,1), collision_group="throw")
        self.O6 = sim.send_box(position=(-c.handLength/3,c.handLength/2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.handHeight/2),
                               sides=(c.handHeight, c.handHeight, c.handLength), color=(0,0,1), collision_group="throw")

        #####the other object.
        self.O7 = sim.send_sphere(
            position=(5, 20,0.7),
            radius=0.7, color=(0.5, 0.5, 0.5), collision_group="throw")
        sim.add_impulse_to_body(self.O7,force=(-2,0,0))

    def send_joints(self, sim):
        self.jointList = {}
        self.jointList[0] = sim.send_ball_and_socket_joint(self.O0, self.O1, anchor=(0,0,c.blockHeight))
        self.jointList[1]=sim.send_hinge_joint(self.O1, self.O2, anchor=(0,0,c.blockHeight+c.arm1Height), axis=(1,0,0))
        self.jointList[2]= sim.send_ball_and_socket_joint(self.O2, self.O3, anchor=(0,0,c.blockHeight+c.arm1Height+c.arm2Height))
        self.jointList[3]=sim.send_hinge_joint(self.O3, self.O5, anchor=(c.handLength/3,c.handLength/2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight ), axis=(1,0,0))
        self.jointList[4] = sim.send_hinge_joint(self.O3, self.O6, anchor=(-c.handLength /3, c.handLength / 2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight), axis=(1, 0, 0))

    def send_sensors(self,sim):
        self.sensorList = {}
        self.sensorList[0]= sim.send_light_sensor(self.O0)
        self.sensorList[1]=sim.send_light_sensor(self.O1)
        ray1 = sim.send_ray(self.O0, position=(0,0.15,0.15),direction=(0,1,0), max_length=100)
        ray2 = sim.send_ray(self.O0, position=(0.3, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray3 = sim.send_ray(self.O0, position=(0.6, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray4 = sim.send_ray(self.O0, position=(-0.3, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray5 = sim.send_ray(self.O0, position=(-0.6, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        self.sensorList[2]=sim.send_ray_sensor(ray1, which_sense='d')
        self.sensorList[3] = sim.send_ray_sensor(ray2, which_sense='d')
        self.sensorList[4] = sim.send_ray_sensor(ray3, which_sense='d')
        self.sensorList[5] = sim.send_ray_sensor(ray4, which_sense='d')
        self.sensorList[6] = sim.send_ray_sensor(ray5, which_sense='d')

    def send_neurons(self,sim):
        self.SN={}
        for sensor in range(len(self.sensorList)):
            self.SN[sensor]=sim.send_sensor_neuron( sensor_id = self.sensorList[sensor])

        self.MN={}
        for joint in range(len(self.jointList)):
            self.MN[joint]=sim.send_motor_neuron( motor_id = self.jointList[joint])

    def send_synapses(self,sim):
        for sn in self.SN:
            for mn in self.MN:
                sim.send_synapses(source_neuron_id=self.SN[sn], target_neuron_id=self.MN[mn], weight=0.5)









