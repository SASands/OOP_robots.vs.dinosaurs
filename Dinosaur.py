

from Robot import Robot


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health_level = 250

    def attack(self, robot):
        #if the robot attacks a dinosaur decrement its hit power from opponents health (vice versa)
        # if self.attack_power 
        self.robot = robot

