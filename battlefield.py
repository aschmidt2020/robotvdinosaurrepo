from fleet_robot import Fleet
from herd_dino import Herd

class Battlefield:
    def __init__(self, dino_list, robot_list):
        self.fleet = Fleet(robot_list)
        self.herd = Herd(dino_list)
    
    def run_game(self):
        pass
    
    def display_welcome(self):
        print('\nWelcome to Robots versus Dinosaurs!')
    
    def battle(self):
        pass
    
    def dino_turn(self, dinosaur_attacking, robot_attacked):
        dinosaur_attacking = self.herd[dinosaur_attacking]
        robot_attacked = self.fleet[robot_attacked]
        dinosaur_attacking.dino_attack(robot_attacked)
    
    def robot_turn(self, robot_atttacking, dino_attacked):
        robot_atttacking.robot_attack(dino_attacked)
    
    def show_dino_opponent_options(self):
        self.herd.display_dino_herd()
    
    def show_robot_opponent_options(self):
        self.fleet.display_robot_fleet()
    
    def display_winners(self):
        pass