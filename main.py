#due Monday 11/15
from battlefield import Battlefield
from fleet_robot import robot_fleet
from herd_dino import dino_herd

#creating battlefield one
battlefield_one = Battlefield(robot_fleet, dino_herd)

#running battlefield one game
battlefield_one.run_game()