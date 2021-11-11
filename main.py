#import #instantiate battlefield #run game #due Monday 11/15
from battlefield import Battlefield
from robot import robot_list
from dinosaur import dino_list

#creating battlefield one
battlefield_one = Battlefield(dino_list, robot_list)
battlefield_one.display_welcome()

#dipslaying current dino and robot lists
battlefield_one.show_dino_opponent_options()
battlefield_one.show_robo_opponent_options()

#sample attack
battlefield_one.dino_turn(dino_list[0], robot_list[0])
battlefield_one.show_robo_opponent_options()