

from Robot import Robot


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health_level = 250

    def attack(self, robot):
        robot.robot_health -= self.attack_power
        print(robot.robot_health -= self.attack_power)
        



