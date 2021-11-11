from fleet_robot import Fleet
from herd_dino import Herd

class Battlefield:
    def __init__(self, dino_list, robo_list):
        self.fleet = Fleet(robo_list)
        self.herd = Herd(dino_list)
    
    def run_game(self):
        pass
    
    def display_welcome(self):
        print('\nWelcome to Robots versus Dinosaurs!')
    
    def battle(self):
        pass
    
    def dino_turn(self, dinosaur_attacking, robot_attacked):
        dinosaur_attacking.dino_attack(robot_attacked)
    
    def robo_turn(self, robot_atttacking, dino_attacked):
        robot_atttacking.robot_attack(dino_attacked)
    
    def show_dino_opponent_options(self):
        self.herd.display_dino_herd()
    
    def show_robo_opponent_options(self):
        self.fleet.display_robo_fleet()
    
    def display_winners(self):
        pass