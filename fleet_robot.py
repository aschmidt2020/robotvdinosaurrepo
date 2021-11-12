from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_list = [ ]
        self.create_robot_fleet()
        
    def create_robot_fleet(self):
        robot_one = Robot('Robot One', 'Basic Weapon One', 10)
        robot_two = Robot('Robot Two', 'Basic Weapon One', 10)
        robot_three = Robot('Robot Three', 'Basic Weapon One', 10)
        
        self.robot_list.append(robot_one)
        self.robot_list.append(robot_two)
        self.robot_list.append(robot_three)
        
    def display_robot_fleet(self):
        print('This is the current robot fleet: ')
        for robot in self.robot_list:
            print (f'{self.robot_list.index(robot)} Robot Name: {robot.robot_name}, Robot Health: {robot.robot_health}')
