from weapon import Weapon

class Robot:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.robot_health = 30 #TODO currently set to 30 for quick testing purposes
        print(f'{self.robot_name}, please select a weapon: ')
        self.robot_weapon = Weapon('Basic Weapon', 10)
        self.select_weapon()
        
    def robot_attack(self, dinosaur):
        dinosaur.dino_health -= self.robot_weapon.attack_power
        print(f'\nAttacking {dinosaur.dino_name}...')
        print(f'You have successfully attacked {dinosaur.dino_name}. Their new health level is: {dinosaur.dino_health}.\n') 
    
    def select_weapon(self):
        weapon_list = [ ]
        
        weapon_one = Weapon('Basic Weapon', 10)
        weapon_two = Weapon('Advanced Weapon', 20)
        weapon_three = Weapon('Sneaky Weapon', 15 )
        
        weapon_list.append(weapon_one)
        weapon_list.append(weapon_two)
        weapon_list.append(weapon_three)
        
        for weapon in weapon_list:
            print(f'{weapon_list.index(weapon)} Weapon Name: {weapon.weapon_name} Attack Power {weapon.attack_power}')
            
        selected_weapon = weapon_list[int(input('Please input index number of desired weapon: '))]
        self.robot_weapon = selected_weapon