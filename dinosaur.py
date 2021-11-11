class Dinosaur:
    def __init__(self, dino_name, attack_power):
        self.dino_name = dino_name
        self.attack_power = attack_power
        self.dino_health = 100
    
    def dino_attack(self, robot):
        robot.robot_health -= self.attack_power 

#instantiated three dinos and added to list
dino_list = [ ]

dinosaur_one = Dinosaur('Dino One', 10)
dinosaur_two = Dinosaur('Dino Two', 10)
dinosaur_three = Dinosaur('Dino Three', 10)

dino_list.append(dinosaur_one)
dino_list.append(dinosaur_two)
dino_list.append(dinosaur_three)
