from helpers import Map, load_map_10, load_map_40, show_map
import math
from PathPlanner import PathPlanner
import PathPlanner_functions
from test import test

# load map_10 and visualize
map_10 = load_map_10()
#show_map(map_10)
map_40 = load_map_40()
#show_map(map_40)

# Adding functions dynamically to the PathPlanner class defined in PathPlanner.py
PathPlanner.create_closedSet = PathPlanner_functions.create_closedSet
PathPlanner.create_openSet = PathPlanner_functions.create_openSet
PathPlanner.create_cameFrom = PathPlanner_functions.create_cameFrom
PathPlanner.create_gScore = PathPlanner_functions.create_gScore
PathPlanner.create_fScore = PathPlanner_functions.create_fScore
PathPlanner.set_map = PathPlanner_functions.set_map
PathPlanner.set_start = PathPlanner_functions.set_start
PathPlanner.set_goal = PathPlanner_functions.set_goal
PathPlanner.is_open_empty = PathPlanner_functions.is_open_empty
PathPlanner.get_current_node = PathPlanner_functions.get_current_node
PathPlanner.get_neighbors = PathPlanner_functions.get_neighbors
PathPlanner.get_gScore = PathPlanner_functions.get_gScore
PathPlanner.distance = PathPlanner_functions.distance
PathPlanner.get_tentative_gScore = PathPlanner_functions.get_tentative_gScore
PathPlanner.heuristic_cost_estimate = PathPlanner_functions.heuristic_cost_estimate
PathPlanner.calculate_fscore = PathPlanner_functions.calculate_fscore
PathPlanner.record_best_path_to = PathPlanner_functions.record_best_path_to

# Testing Path Planner
planner = PathPlanner(map_40, 5, 34)
path = planner.path
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)

# Testing the PathPlanner using test.py
test(PathPlanner)
# visualize the path
#start = 5
#goal = 34
#show_map(map_40, start=start, goal=goal, path=PathPlanner(map_40, start, goal).path)



