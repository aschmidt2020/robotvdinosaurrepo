class Battlefield:
    def __init__(self, robot_fleet, dino_herd):
        self.fleet = robot_fleet
        self.herd = dino_herd
    
    def run_game(self):
        pass
    
    def display_welcome(self):
        print('\nWelcome to Robots versus Dinosaurs!')
    
    def battle(self):
        current_attacker_dinosaur = True #placeholder, will change to user input later
        while len(self.fleet.robot_list) > 0 or len(self.herd.dino_list) > 0:
            if current_attacker_dinosaur == True:
                dinosaur_attacking = 0 #placeholder
                robot_attacked = 0 #placeholder
                self.dino_turn(dinosaur_attacking, robot_attacked)
                while self.fleet.robot_list[robot_attacked].robot_health > 0:
                    break
                else:
                    self.fleet.robot_list.remove(self.fleet.robot_list[robot_attacked])
                    #display options
                
            elif current_attacker_dinosaur == False:
                robot_attacking = 0 #placeholder
                dino_attacked = 0 #placeholder
                self.robot_turn(robot_attacking, dino_attacked)
                while self.herd.dino_list[dino_attacked].dino_health > 0:
                    break
                else:
                    self.herd.dino_list.remove(self.herd.dino_list[dino_attacked])
                    #display options
                
            current_attacker_dinosaur = not current_attacker_dinosaur
            
    def dino_turn(self, dinosaur_attacking, robot_attacked):
        dinosaur_attacking = self.herd.dino_list[dinosaur_attacking]
        robot_attacked = self.fleet.robot_list[robot_attacked]
        dinosaur_attacking.dino_attack(robot_attacked)
    
    def robot_turn(self, robot_atttacking, dino_attacked):
        robot_atttacking = self.fleet.robot_list[robot_atttacking]
        dino_attacked = self.herd.dino_list[dino_attacked]
        robot_atttacking.robot_attack(dino_attacked)
    
    def show_dino_opponent_options(self):
        self.herd.display_dino_herd()
    
    def show_robot_opponent_options(self):
        self.fleet.display_robot_fleet()
    
    def display_winners(self):
        pass