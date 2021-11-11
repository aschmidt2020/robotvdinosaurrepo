from dinosaur import dino_list

class Herd:
    def __init__(self, dino_list):
        self.dino_list = dino_list
    
    #def create_dino_herd(self, dino_list): - in UML do I need this step?
        #self.dino_list = dino_list
    
    def display_dino_herd(self):
        print('\n')
        for dino in self.dino_list:
            print (f'Dinosaur Name: {dino.dino_name}, Dinosaur Health: {dino.dino_health}')

#creating herd
dino_herd = Herd(dino_list)