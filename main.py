#import #instantiate battlefield #run game #due Monday 11/15
from battlefield import Battlefield
from fleet_robot import robot_fleet
from herd_dino import dino_herd

#creating battlefield one
battlefield_one = Battlefield(robot_fleet, dino_herd)
battlefield_one.display_welcome()

#dipslaying current dino and robot lists
print('\nHere are your current players: ')
battlefield_one.show_dino_opponent_options()
battlefield_one.show_robot_opponent_options()

#sample attack on robot and dinosaur
battlefield_one.dino_turn(0, 0) #represents dino 1 and robot 1
battlefield_one.robot_turn(1, 1) #represents robot 2 and dino 2