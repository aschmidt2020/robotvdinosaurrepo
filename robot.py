from weapon import Weapon

class Robot:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.robot_health = 30
        self.robot_power = 50
        print(f'\n{self.robot_name}, please select a weapon: ')
        self.robot_weapon = Weapon('Basic Weapon', 10, 10)
        self.select_weapon()
        
    def robot_attack(self, dinosaur): #reduces dinosaur health and robot power by attack power and weapon energy needed
        dinosaur.dino_health -= self.robot_weapon.attack_power
        self.robot_power -= self.robot_weapon.energy_needed
        print(f'\nAttacking {dinosaur.dino_name}...')
        print(f'You have successfully attacked {dinosaur.dino_name}. Their new health level is: {dinosaur.dino_health}.')
        print(f'{self.robot_name}, your new power level is: {self.robot_power}.\n')
    
    def select_weapon(self): #creates weapon list for each robot to pick from
        weapon_list = [ ]
        
        weapon_one = Weapon('Basic Weapon', 10, 10)
        weapon_two = Weapon('Advanced Weapon', 15, 20)
        weapon_three = Weapon('Sneaky Weapon', 20, 25)
        
        weapon_list.append(weapon_one)
        weapon_list.append(weapon_two)
        weapon_list.append(weapon_three)
        
        for weapon in weapon_list: #displays weapon options
            print(f'{weapon_list.index(weapon)} Weapon Name: {weapon.weapon_name}, Attack Power: {weapon.attack_power}, Energy Needed: {weapon.energy_needed}')
        
        selected_weapon = weapon_list[int(input('Please input index number of desired weapon: '))]
        
        self.robot_weapon = selected_weapon
        