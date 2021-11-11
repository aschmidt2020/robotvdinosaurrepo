#import #instantiate battlefield #run game #due Monday 11/15
from battlefield import Battlefield
from fleet_robot import robot_fleet
from herd_dino import dino_herd

#creating battlefield one
battlefield_one = Battlefield(robot_fleet, dino_herd)
battlefield_one.display_welcome()

#dipslaying current dino and robot lists
battlefield_one.show_dino_opponent_options()
battlefield_one.show_robo_opponent_options()
