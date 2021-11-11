from robot import robot_list #imported list from other file

class Fleet:
    def __init__(self):
        self.robot_list = []
        
    def create_robo_fleet(self):
        self.robot_list = robot_list