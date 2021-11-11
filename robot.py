from weapon import Weapon

class Robot:
    def __init__(self, robot_name, weapon_name, attack_power):
        self.robot_name = robot_name
        self.robot_health = 100
        self.robot_weapon = Weapon(weapon_name, attack_power)
        
    def robot_attack(self, dinosaur):
        dinosaur.dino_health -= self.robot_weapon.attack_power
        print(f'You have successfully attacked {dinosaur.dino_name}. Their new health level is: {dinosaur.dino_health}.')

#instantiated three robots and added to list
robot_list = [ ]

robot_one = Robot('Robot One', 'Basic Weapon One', 10)
robot_two = Robot('Robot Two', 'Basic Weapon One', 10)
robot_three = Robot('Robot Three', 'Basic Weapon One', 10)

robot_list.append(robot_one)
robot_list.append(robot_two)
robot_list.append(robot_three)
