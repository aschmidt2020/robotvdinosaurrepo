from weapon import Weapon

class Robot:
    def __init__(self, robot_name, weapon_name, attack_power):
        self.robot_name = robot_name
        self.robot_health = 30
        self.robot_weapon = Weapon(weapon_name, attack_power)
        
    def robot_attack(self, dinosaur):
        dinosaur.dino_health -= self.robot_weapon.attack_power
        print(f'\nAttacking {dinosaur.dino_name}...')
        print(f'You have successfully attacked {dinosaur.dino_name}. Their new health level is: {dinosaur.dino_health}.')
