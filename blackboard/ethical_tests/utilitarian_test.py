# To-Do:
from math import sqrt

import ethical_test


def bar():
    print("bar")


class UtilitarianTest(ethical_test.EthicalTest):

    def __init__(self, test_data):
        super().__init__(test_data)

    def run_test(self, data):
        pass

class WorldModel():

    def __init__(self, size=[5,5], robot_location=[0,0], user_location=[0,4], danger_location=[4,4],
                 danger_radius = 1, robot_goal=[4,1]):
        self.size = size
        self.robot_init_location = robot_location
        self.user_init_location = user_location
        self.danger = danger_location
        self.robot_goal = robot_goal
        self.danger_radius = danger_radius


class Human_model():

    def __init__(self, current_location, previous_location):
        self.location = current_location
        self.previous_location = previous_location # m (gradient)
        self.speed = 1 #meter for step

    def _simulate(self, danger):
        shortest_distance_to_danger = abs((self.location[0]-self.previous_location[0]) * (self.previous_location[
                                                                                         1]-danger[1]) - (
            self.previous_location[0]-danger[0])*(self.location[1]-self.previous_location[1])) / sqrt((self.location[
            0]-self.previous_location[0])**2 + (self.location[1]-self.previous_location[1])**2)

        return shortest_distance_to_danger

    def is_in_danger(self, danger, danger_radius):
        if self._simulate(danger) < danger_radius:
            return True
        else:
            return False
