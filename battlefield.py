from fleet_robot import Fleet
from herd_dino import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome() #displaying welcome
        
        print('\nHere are your current players: ') #showing initial characters
        self.show_dino_opponent_options()
        self.show_robot_opponent_options()
    
        print('\nThis begins the battle...') #starting game
        self.battle()
        
    def display_welcome(self):
        print('\nWelcome to Robots versus Dinosaurs!')
    
    def battle(self):
        current_attacker_dinosaur = input('Please select who you would like to go first (Dinosaurs or Robots): ')
        if current_attacker_dinosaur == 'Dinosaurs':
            current_attacker_dinosaur = True
        elif current_attacker_dinosaur == 'Robots':
            current_attacker_dinosaur = False
        else:
            current_attacker_dinosaur = input('Please select Dinosaurs or Robots: ')
            
        while len(self.fleet.robot_list) > 0 and len(self.herd.dino_list) > 0:
            if current_attacker_dinosaur == True:
                self.show_robot_opponent_options()
                dinosaur_attacking = int(input('Please select index number of attacking dinosaur: '))
                    #if self.herd.dino_list[dinosaur_attacking].dino_energy < self.herd.dino_list[dinosaur_attacking].attack_power
                    #not needed because dinosaur energy is at even interval of attack power
                robot_attacked = int(input('Please select index number of robot you would like to attack: '))
                self.dino_turn(dinosaur_attacking, robot_attacked)
                while self.fleet.robot_list[robot_attacked].robot_health > 0 and self.herd.dino_list[dinosaur_attacking].dino_energy >0:
                    break
                if self.fleet.robot_list[robot_attacked].robot_health <= 0:
                    self.fleet.robot_list.remove(self.fleet.robot_list[robot_attacked])
                elif self.herd.dino_list[dinosaur_attacking].dino_energy <= 0:
                    self.herd.dino_list.remove(self.herd.dino_list[dinosaur_attacking])
                           
            elif current_attacker_dinosaur == False:
                self.show_dino_opponent_options()
                robot_attacking = int(input('Please select index number of attacking robot: '))
                if self.fleet.robot_list[robot_attacking].robot_power < self.fleet.robot_list[robot_attacking].robot_weapon.energy_needed:
                    robot_attacking = int(input('Please select robot with adequate energy level: '))
                dino_attacked = int(input('Please select index number of dinosaur you would like to attack: '))
                self.robot_turn(robot_attacking, dino_attacked)
                while self.herd.dino_list[dino_attacked].dino_health > 0 and self.fleet.robot_list[robot_attacking].robot_power >= 0:
                    break
                if self.herd.dino_list[dino_attacked].dino_health <= 0:
                    self.herd.dino_list.remove(self.herd.dino_list[dino_attacked])
                if self.fleet.robot_list[robot_attacking].robot_power <= 0:
                    self.fleet.robot_list.remove(self.fleet.robot_list[robot_attacking])
                    
            current_attacker_dinosaur = not current_attacker_dinosaur
         
        if len(self.fleet.robot_list) == 0 or len(self.herd.dino_list) == 0:
            if len(self.fleet.robot_list) == 0:
                self.display_winners('Dinosaur')
            elif len(self.herd.dino_list) == 0:
                self.display_winners('Robot')
               
    def dino_turn(self, dinosaur_attacking, robot_attacked): #dino_attack from dinosaur.py
        dinosaur_attacking = self.herd.dino_list[dinosaur_attacking]
        robot_attacked = self.fleet.robot_list[robot_attacked]
        dinosaur_attacking.dino_attack(robot_attacked)
    
    def robot_turn(self, robot_atttacking, dino_attacked): #robot_attack from robot.py
        robot_atttacking = self.fleet.robot_list[robot_atttacking]
        dino_attacked = self.herd.dino_list[dino_attacked]
        robot_atttacking.robot_attack(dino_attacked)
    
    def show_dino_opponent_options(self):
        self.herd.display_dino_herd()
    
    def show_robot_opponent_options(self):
        self.fleet.display_robot_fleet()
    
    def display_winners(self, winning_team):
        print(f'\nThe {winning_team} team has won the game.')