class Dinosaur:
    def __init__(self, dino_name, attack_power):
        self.dino_name = dino_name
        self.attack_power = attack_power
        self.dino_health = 100
    
    def dino_attack(self, robot):
        robot.robot_health -= self.attack_power 
        print(f'\nYou have successfully attacked {robot.robot_name}. Their new health level is: {robot.robot_health}.')
