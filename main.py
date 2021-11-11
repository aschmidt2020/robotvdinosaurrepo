#import #instantiate battlefield #run game #due Monday 11/15
from battlefield import Battlefield
from robot import robot_list
from dinosaur import dino_list

#creating battlefield one
battlefield_one = Battlefield(dino_list, robot_list)
battlefield_one.display_welcome()

#dipslaying current dino and robot lists
print('\nHere are your current players: ')
battlefield_one.show_dino_opponent_options()
battlefield_one.show_robot_opponent_options()

#sample attack on robot and dinosaur
#battlefield_one.dino_turn(dino_list[0], robot_list[0]) # this works, but does not use the fleet object I created
battlefield_one.dino_turn(0, 0)