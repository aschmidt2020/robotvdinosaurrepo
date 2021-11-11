from fleet_robot import Fleet
from herd_dino import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        pass
    
    def display_welcome(self):
        print('Welcome to Robots versus Dinosaurs!')
    
    def battle(self):
        pass
    
    def dino_turn(self, dinosaur_attacking, robot_attacked):
        dinosaur_attacking.dino_attack(robot_attacked)
        print(f'You have successfully attacked {robot_attacked}. Their new health level is: {robot_attacked.robot_health}.')
    
    def robo_turn(self, robot_atttacking, dino_attacked):
        robot_atttacking.robot_attack(dino_attacked)
        print(f'You have successfully attacked {dino_attacked}. Their new health level is: {dino_attacked.dino_health}.')
    
    def show_dino_opponent_options(self):
        self.herd.display_dino_herd()
    
    def show_robo_opponent_options(self):
        self.fleet.display_robo_fleet()
    
    def display_winners(self):
        pass