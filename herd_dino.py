from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = [ ]
    
    def create_dino_herd(self, dinosaur):
        self.dino_list.append(dinosaur)
    
    def display_dino_herd(self):
        print('\n')
        for dino in self.dino_list:
            print (f'{self.dino_list.index(dino)} Dinosaur Name: {dino.dino_name}, Dinosaur Health: {dino.dino_health}')
        print('\n')


#instantiated three dinos and added to list
dinosaur_one = Dinosaur('Dino One', 10)
dinosaur_two = Dinosaur('Dino Two', 10)
dinosaur_three = Dinosaur('Dino Three', 10)

#creating dino fleet
dino_herd = Herd()
dino_herd.create_dino_herd(dinosaur_one)
dino_herd.create_dino_herd(dinosaur_two)
dino_herd.create_dino_herd(dinosaur_three)

dino_herd.display_dino_herd()