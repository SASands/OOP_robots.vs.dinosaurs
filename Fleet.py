from urllib import robotparser
from Robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        pass

    def create_fleet(self):  
        robot1 = Robot("Cyburn")
        robot2 = Robot("Metally")
        robot3 = Robot("Links")
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
