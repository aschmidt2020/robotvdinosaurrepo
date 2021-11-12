from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_list = [ ]
        self.create_robot_fleet()
        
    def create_robot_fleet(self):
        robot_one = Robot('Robot One') 
        robot_two = Robot('Robot Two')
        robot_three = Robot('Robot Three')
        
        self.robot_list.append(robot_one)
        self.robot_list.append(robot_two)
        self.robot_list.append(robot_three)
        
        
    def display_robot_fleet(self):
        print('\nThis is the current robot fleet: ')
        for robot in self.robot_list:
            print (f'{self.robot_list.index(robot)} Name: {robot.robot_name}, Wpn Atk Pwr: {robot.robot_weapon.attack_power}, Hlth: {robot.robot_health}, Pwr Lvl: {robot.robot_power}')
