class Dinosaur:
    def __init__(self, dino_name, attack_power):
        self.dino_name = dino_name
        self.attack_power = attack_power
        self.dino_health = 30  #TODO currently set to 30 for quick testing purposes
    
    def dino_attack(self, robot):
        robot.robot_health -= self.attack_power 
        print(f'\nAttacking {robot.robot_name}....')
        print(f'You have successfully attacked {robot.robot_name}. Their new health level is: {robot.robot_health}.\n')
