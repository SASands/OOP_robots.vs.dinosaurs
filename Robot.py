
from Weapon import Weapon



class Robot():
    def __init__(self, name):
        self.name = name
        self.robot_health = 150
        self.robot_weapon = Weapon("Blaster", 25)
        

    def attack(self, Dinosaur):
        Dinosaur = Dinosaur

        
