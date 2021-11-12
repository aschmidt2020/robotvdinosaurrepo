from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = [ ]
        self.create_dino_herd()
    
    def create_dino_herd(self,):
        dinosaur_one = Dinosaur('Dino One')
        dinosaur_two = Dinosaur('Dino Two')
        dinosaur_three = Dinosaur('Dino Three')
        
        self.dino_list.append(dinosaur_one)
        self.dino_list.append(dinosaur_two)
        self.dino_list.append(dinosaur_three)
    
    def display_dino_herd(self):
        print('\nThis is the current dinosaur herd: ')
        for dino in self.dino_list:
            print (f'{self.dino_list.index(dino)} Name: {dino.dino_name}, Atk Pwr: {dino.attack_option.attack_power}, Hlth: {dino.dino_health}, Energy: {dino.dino_energy}')