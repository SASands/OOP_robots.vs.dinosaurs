from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaur = []
        pass

    def create_herd(self):
        dino1 = Dinosaur("Billy", 35)
        dino2 = Dinosaur("Bobby", 20)
        dino3 = Dinosaur("Bradly", 25)
        self.dinosaur.append(dino1)
        self.dinosaur.append(dino2)
        self.dinosaur.append(dino3)

