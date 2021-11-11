from weapon import Weapon

class Robot:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.robot_health = 100
        self.robot_weapon = Weapon()
    
    def robo_attack(self, dinosaur):
        pass