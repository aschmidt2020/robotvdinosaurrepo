from attack_option_dino import DinoAttack

class Dinosaur:
    def __init__(self, dino_name):
        self.dino_name = dino_name
        self.dino_health = 30
        self.dino_energy = 50
        print(f'\n{self.dino_name}, please select a attack option: ')
        self.attack_option = DinoAttack('Basic Attack', 10)
        self.set_attack_option()
    
    def dino_attack(self, robot): #reduces robot health and dinosaur energy by attack power
        robot.robot_health -= self.attack_option.attack_power
        self.dino_energy -= self.attack_option.attack_power
        print(f'\nAttacking {robot.robot_name}....')
        print(f'You have successfully attacked {robot.robot_name}. Their new health level is: {robot.robot_health}.')
        print(f'{self.dino_name}, your new energy level is: {self.dino_energy}.\n')

    def set_attack_option(self): #creates attack option tuple
        attack_one = DinoAttack ('Basic Attack', 10)
        attack_two = DinoAttack('Double Attack', 20)
        attack_three = DinoAttack('Low Energy Attack', 5)
        
        attack_tuple = (attack_one, attack_two, attack_three)
        
        for attack in attack_tuple: #displays attack options
            print(f'{attack_tuple.index(attack)} Attack Name: {attack.attack_name}, Attack Power: {attack.attack_power}')
        
        selected_attack = attack_tuple[int(input('Please input index number of desired weapon: '))]
        
        self.attack_option = selected_attack