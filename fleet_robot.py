import robot
from robot import robot_list #imported list from other file

class Fleet:
    def __init__(self, robot_list):
        self.robot_list = robot_list
        
    #def create_robo_fleet(self, robot_list): - in UML has this step, do i need it?
        #self.robot_list = robot_list
        
    def display_robo_fleet(self):
        for robot in self.robot_list:
            print (f'Robot Name: {robot.robot_name}, Robot Health: {robot.robot_health}')

#creating fleet
robot_fleet = Fleet(robot_list)