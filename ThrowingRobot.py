from builtins import range, len

import pyrosim
import constants as c
import random


class ROBOT:
    def __init__(self, sim, wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_actuators(sim)
        self.send_neurons(sim)
        self.send_synapses(sim,wts)

    def send_objects(self, sim):
        self.O0 = sim.send_box(position=(0, 0, c.blockHeight / 2), sides=(c.blockLength, c.blockWidth, c.blockHeight),
                               color=(1, 0, 0), density=5, collision_group='bot')
        self.O1 = sim.send_cylinder(position=(0, 0, c.blockHeight + c.arm1Height / 2), length=c.arm1Height,
                                    radius=c.radius,
                                    color=(0, 1, 0), orientation=(0, 0, 1), collision_group='bot')
        self.O2 = sim.send_cylinder(position=(0, 0, c.blockHeight + c.arm1Height + c.arm2Height / 2),
                                    length=c.arm2Height, radius=c.radius, color=(1, 0, 1), orientation=(0, 0, 1),
                                    collision_group='bot')
        self.O3 = sim.send_box(position=(0, 0, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight / 2),
                               sides=(c.handLength, c.handLength, c.handHeight), color=(0, 0, 1), collision_group='bot')
        self.O4 = sim.send_sphere(
            position=(0, 0, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.ballRadius + 0.2),
            radius=c.ballRadius, color=(0.5, 0.5, 0.5), collision_group='pop')
        self.O5 = sim.send_box(position=(c.handLength / 3, -c.handLength / 2,
                                         c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.handHeight / 2),
                               sides=(c.handHeight, c.handHeight, c.handLength), color=(0, 0, 1), collision_group='bot')
        self.O6 = sim.send_box(position=(-c.handLength / 3, -c.handLength / 2,
                                         c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight + c.handHeight / 2),
                               sides=(c.handHeight, c.handHeight, c.handLength), color=(0, 0, 1), collision_group='bot')

        #####the other object.
        self.O7 = sim.send_sphere(
            position=(0.6, 20, 0.7),
            radius=0.7, color=(0.5, 0.5, 0.5), collision_group="thro")
        sim.add_impulse_to_body(self.O7, force=(-2, 0, 0))
        sim.assign_collision('bot', 'pop')

    def send_joints(self, sim):
        self.jointList = {}

        ##the ball and socket joint from the first object to the arm

        self.jointList[0] = sim.send_hinge_joint(self.O0, self.O1, anchor=(0, 0, c.blockHeight), axis=(0, 1, 0))
        self.jointList[1] = sim.send_hinge_joint(self.O1, self.O2, anchor=(0, 0, c.blockHeight + c.arm1Height),
                                                 axis=(1, 0, 0))
        self.jointList[2] = sim.send_hinge_joint(self.O2, self.O3,
                                                 anchor=(0, 0, c.blockHeight + c.arm1Height + c.arm2Height),
                                                 axis=(1, 0, 0))
        self.jointList[3] = sim.send_hinge_joint(self.O3, self.O5, anchor=(
        c.handLength / 3, -c.handLength / 2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight), axis=(1, 0, 0))
        self.jointList[4] = sim.send_hinge_joint(self.O3, self.O6, anchor=(
        -c.handLength / 3, -c.handLength / 2, c.blockHeight + c.arm1Height + c.arm2Height + c.handHeight),
                                                 axis=(1, 0, 0))
        self.jointList[5] = sim.send_hinge_joint(self.O0, self.O1, anchor=(0, 0, c.blockHeight), axis=(1, 0, 0))

    def send_sensors(self, sim):
        self.sensorList = {}
        ray1 = sim.send_ray(self.O0, position=(0, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray2 = sim.send_ray(self.O0, position=(1,0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray3 = sim.send_ray(self.O0, position=(2, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray4 = sim.send_ray(self.O0, position=(3, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray5 = sim.send_ray(self.O0, position=(4, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray6 = sim.send_ray(self.O0, position=(-1, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray7 = sim.send_ray(self.O0, position=(-2, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray8 = sim.send_ray(self.O0, position=(-3, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        ray9 = sim.send_ray(self.O0, position=(-4, 0.15, 0.15), direction=(0, 1, 0), max_length=100)
        self.sensorList[0] = sim.send_ray_sensor(ray1, which_sense='d')
        self.sensorList[1] = sim.send_ray_sensor(ray2, which_sense='d')
        self.sensorList[2] = sim.send_ray_sensor(ray3, which_sense='d')
        self.sensorList[3] = sim.send_ray_sensor(ray4, which_sense='d')
        self.sensorList[4] = sim.send_ray_sensor(ray5, which_sense='d')
        self.sensorList[5] = sim.send_ray_sensor(ray6, which_sense='d')
        self.sensorList[6] = sim.send_ray_sensor(ray7, which_sense='d')
        self.sensorList[7] = sim.send_ray_sensor(ray8, which_sense='d')
        self.sensorList[8] = sim.send_ray_sensor(ray9, which_sense='d')

        self.P1x=sim.send_position_x_sensor(self.O4)
        self.P1y=sim.send_position_y_sensor(self.O4)
        self.P2x=sim.send_position_x_sensor(self.O7)
        self.P2y=sim.send_position_y_sensor(self.O7)

    def send_actuators(self, sim):
        self.actuatorList = {}
        for joint in range(len(self.jointList)):
            self.actuatorList[joint] = sim.send_rotary_actuator(self.jointList[joint])

    def send_neurons(self, sim):
        self.SN = {}
        for sensor in range(len(self.sensorList)):
            self.SN[sensor] = sim.send_sensor_neuron(sensor_id=self.sensorList[sensor])

        self.MN = {}
        for actuator in range(len(self.actuatorList)):
            self.MN[actuator] = sim.send_motor_neuron(motor_id=self.actuatorList[actuator])

    def send_synapses(self, sim, wts):
        for sn in self.SN:
            for mn in self.MN:
                sim.send_synapse(source_neuron_id=self.SN[sn], target_neuron_id=self.MN[mn], weight=wts[sn][mn])
