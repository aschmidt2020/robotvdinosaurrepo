from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = [ ]
        self.create_dino_herd()
    
    def create_dino_herd(self,):
        dinosaur_one = Dinosaur('Dino One', 10)
        dinosaur_two = Dinosaur('Dino Two', 10)
        dinosaur_three = Dinosaur('Dino Three', 10)
        
        self.dino_list.append(dinosaur_one)
        self.dino_list.append(dinosaur_two)
        self.dino_list.append(dinosaur_three)
    
    def display_dino_herd(self):
        print('This is the current dinosaur herd: ')
        for dino in self.dino_list:
            print (f'{self.dino_list.index(dino)} Dinosaur Name: {dino.dino_name}, Dinosaur Health: {dino.dino_health}')