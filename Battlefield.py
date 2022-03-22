from Herd import Herd
from Fleet import Fleet


class Battlefield:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.fleet.create_fleet()
        self.herd.create_herd()
    
    def display_welcome(self):
        input ("Welcome to Dinosaur's VS Robot's; Let's Fight")
        print(input)

    def battle(self):
        self.herd.dinosaur[0].attack(self.fleet.robots[0])
        
        self.fleet.robots[0].attack(self.herd.dinosaur[0])
    
        
    def dinos_turn(self, dinosaur):
        self.dinosaur = dinosaur
        Herd()
        return dinosaur

    def robots_turn(self, robot):
        self.robot = robot
        Fleet()



    def run_battle(self):
        user_input = input("What team would you like to attack first? D or R?  ")
        if user_input == ("D"):
            print ("Dino's are on the offensive, Watch out Robots!")
            self.dinos_turn(dinosaur)
        else: 
            print ("Robot's are attacking, watch out Dinosaurs!")
            robots_turn()



    def display_the_winners(self):
        pass













    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass



    


    
