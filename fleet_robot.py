from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_list = [ ]
        
    def create_robot_fleet(self, robot):
        self.robot_list.append(robot)
        
    def display_robot_fleet(self):
        print('\n')
        for robot in self.robot_list:
            print (f'{self.robot_list.index(robot)} Robot Name: {robot.robot_name}, Robot Health: {robot.robot_health}')
        print('\n')

#instantiated three robots and added to list
robot_one = Robot('Robot One', 'Basic Weapon One', 10)
robot_two = Robot('Robot Two', 'Basic Weapon One', 10)
robot_three = Robot('Robot Three', 'Basic Weapon One', 10)

#creating robot fleet
robot_fleet = Fleet()
robot_fleet.create_robot_fleet(robot_one)
robot_fleet.create_robot_fleet(robot_two)
robot_fleet.create_robot_fleet(robot_three)

robot_fleet.display_robot_fleet