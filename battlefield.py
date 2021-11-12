from fleet_robot import Fleet
from herd_dino import Herd

class Battlefield:
    def __init__(self):
        self.display_welcome() #displaying welcome moved to under init so that it will always present first
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        print('\n***********Current Players List***********') #showing initial characters
        self.show_dino_opponent_options()
        self.show_robot_opponent_options()
    
        print('\n***********This begins the battle...***********')
        self.battle()
        
    def display_welcome(self):
        print('\n***********Welcome to Robots versus Dinosaurs!***********')
        print('This game is best played with two players.')
        print('In this game robots and dinosaurs will battle. There will be 3 robots and 3 dinosaurs.')
        print('Dinosaurs have an energy level of 50, and a health of 30.')
        print('You will choose an attack option for the dinosaur. Each attack option has a certain power.')
        print('Robots start with a health of 30 and a power level (energy level) of 50.')
        print('For robots, you will get to choose a weapon. This weapon has a certain attack power and energy level needed to use the weapon.')
        print('If you have less energy or power than you need for your attack, you may attack one more time to deplete this energy.')
        print('Example: Energy = 10, Attack Energy Needed = 20. You may still attack with this player, but it will result in the attacking player being removed.')
        print("You will start the game by choosing each robot's weapon and choosing who will start, Dinosaurs or Robots.")
        print("Let's begin by selecting robot weapons!")
    
    def battle(self):
        current_attacker_dinosaur = int(input('Please select who you would like to go first (0 - Dinosaurs or 1 - Robots): '))
        if current_attacker_dinosaur == 0:
            current_attacker_dinosaur = True
        elif current_attacker_dinosaur == 1:
            current_attacker_dinosaur = False
                    
        while len(self.fleet.robot_list) > 0 and len(self.herd.dino_list) > 0:
            if current_attacker_dinosaur == True:
                print('\n***********DINOSAURS ATTACKING***********')
                self.show_dino_opponent_options()
                self.show_robot_opponent_options()
                
                dinosaur_attacking = int(input('\nPlease select index number of attacking dinosaur: '))
                robot_attacked = int(input('Please select index number of robot you would like to attack: '))
                
                while dinosaur_attacking > len(self.herd.dino_list) - 1: #prevents from choosing player that is not available
                    dinosaur_attacking = int(input('\nPlease select a dinosaur from current players: '))
                                                                
                while robot_attacked > len(self.fleet.robot_list) - 1: #prevents from choosing player that is not available
                    robot_attacked = int(input('\nPlease select a different robot to attack: '))
                                
                self.dino_turn(dinosaur_attacking, robot_attacked)
                
                if self.fleet.robot_list[robot_attacked].robot_health <= 0: #results in 0 health or less than 0 health being removed from list
                    self.fleet.robot_list.remove(self.fleet.robot_list[robot_attacked])
                    
                if self.herd.dino_list[dinosaur_attacking].dino_energy <= 0: #results in 0 energy or less than 0 energy being removed from list
                    self.herd.dino_list.remove(self.herd.dino_list[dinosaur_attacking])
                           
            elif current_attacker_dinosaur == False:
                print('\n***********Robots attacking***********')
                self.show_robot_opponent_options()
                self.show_dino_opponent_options()
                
                robot_attacking = int(input('\nPlease select index number of attacking robot: '))
                dino_attacked = int(input('Please select index number of dinosaur you would like to attack: '))
                
                while robot_attacking > len(self.fleet.robot_list) - 1:
                    robot_attacking = int(input('Please select robot from current players: '))
            
                while dino_attacked > len(self.herd.dino_list) - 1: 
                    dino_attacked = int(input('Please select a different dinosaur to attack: '))
                
                self.robot_turn(robot_attacking, dino_attacked)
                
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