from helpers import Map, load_map_10, load_map_40, show_map
import math

def create_closedSet(self):
    """ Creates and returns a data structure suitable to hold the set of nodes already evaluated"""
    return set()

def create_openSet(self):
    """ Creates and returns a data structure suitable to hold the set of currently discovered nodes 
    that are not evaluated yet. Initially, only the start node is known."""
    if self.start != None:
        return {self.start}
    
    raise(ValueError, "Must create start node before creating an open set. Try running PathPlanner.set_start(start_node)")

def create_cameFrom(self):
    """Creates and returns a data structure that shows which node can most efficiently be reached from another,
    for each node."""
    return {}

def create_gScore(self):
    """Creates and returns a data structure that holds the cost of getting from the start node to that node, 
    for each node. The cost of going from start to start is zero."""
    if self.map is None or self.start is None:
        raise ValueError("Map and start node must be defined before creating gScore.")
    
    gScore = {node: float('inf') for node in self.map.intersections.keys()}  # Set all nodes to infinity
    gScore[self.start] = 0  # Start node cost is 0
    
    return gScore

def create_fScore(self):
    """Creates and returns a data structure that holds the total cost of getting from the start node to the goal
    by passing by that node, for each node. That value is partly known, partly heuristic.
    For the first node, that value is completely heuristic."""
    
    if self.map is None or self.start is None or self.goal is None:
        raise ValueError("Map, start node, and goal node must be defined before creating fScore.")

    fScore = {node: float('inf') for node in self.map.intersections.keys()}  
    fScore[self.start] = 0  # Set start node's fScore to 0 instead of heuristic

    return fScore

def set_map(self, M):
    """Method used to set map attribute """
    self._reset(self)
    self.start = None
    self.goal = None
    self.map = M

def set_start(self, start):
    """Method used to set start attribute """
    self._reset(self)
    self.start = start  # Set the start node
    self.goal = None  # Reset goal node
    self.closedSet = None  # Clear closed set
    self.openSet = None  # Clear open set
    self.cameFrom = None  # Clear cameFrom
    self.gScore = None  # Clear gScore
    self.fScore = None  # Clear fScore
    self.path = None  # Clear any existing path
    
def set_goal(self, goal):
    """Method used to set goal attribute """
    self._reset(self)
    self.goal = goal  # Set the goal node
    self.start = None  # Reset start node
    self.closedSet = None  # Clear closed set
    self.openSet = None  # Clear open set
    self.cameFrom = None  # Clear cameFrom
    self.gScore = None  # Clear gScore
    self.fScore = None  # Clear fScore
    self.path = None  # Clear any existing path

def is_open_empty(self):
    """returns True if the open set is empty. False otherwise. """
    return len(self.openSet) == 0  # Return True if openSet is empty, otherwise False

def get_current_node(self):
    """ Returns the node in the open set with the lowest value of f(node)."""
    current_node = min(self.openSet, key=lambda node: self.fScore[node])
    return current_node

def get_neighbors(self, node): 
    """Returns the neighbors of a node""" 
    if not isinstance(self.map, Map):
        raise ValueError("Map is not a valid Map instance.")
    
    if node not in self.map._graph:
        raise ValueError(f"Node {node} not found in the graph.")

    return list(self.map._graph.neighbors(node))  # Get neighbors using NetworkX

def get_gScore(self, node):
    """Returns the g Score of a node"""
    return self.gScore.get(node, float('inf'))  # Return infinity if node is not in gScore

def distance(self, node_1, node_2):
    """Computes the Euclidean L2 Distance between two nodes"""
    if not isinstance(self.map, Map):
        raise ValueError("Map is not a valid Map instance.")
    
    if node_1 not in self.map.intersections or node_2 not in self.map.intersections:
        raise ValueError(f"One or both nodes {node_1}, {node_2} not found in the map intersections.")

    x1, y1 = self.map.intersections[node_1]  # Get coordinates from intersections
    x2, y2 = self.map.intersections[node_2]

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Compute Euclidean distance

def get_tentative_gScore(self, current, neighbor):
    """Returns the tentative g Score of a node"""
    gScore_current = self.get_gScore(current)
    
    # Calculate the distance from current node to neighbor (assuming Euclidean distance)
    distance_current_to_neighbor = self.distance(current, neighbor)
    
    # Return the tentative gScore (current gScore + distance to neighbor)
    return gScore_current + distance_current_to_neighbor

def heuristic_cost_estimate(self, node):
    """ Returns the heuristic cost estimate of a node """
    if self.goal is None:
        raise ValueError("Goal node must be defined before calculating heuristic")
    
    # Calculate the Euclidean distance from the current node to the goal node
    return self.distance(node, self.goal)
    
def calculate_fscore(self, node):
    """Calculate the f score of a node. """
    # F = G + H
    g_score = self.get_gScore(node)  # Get gScore of the node
    h_score = self.heuristic_cost_estimate(node)  # Get heuristic estimate (h)
    return g_score + h_score  # f = g + h

def record_best_path_to(self, current, neighbor):
    """Record the best path to a node """
    self.cameFrom[neighbor] = current
    
    # Calculate the tentative gScore for the neighbor
    tentative_gScore = self.get_gScore(current) + self.distance(current, neighbor)
    
    # Update the gScore for the neighbor if the new gScore is better (lower)
    self.gScore[neighbor] = tentative_gScore
    
    # Calculate and update the fScore for the neighbor
    self.fScore[neighbor] = self.calculate_fscore(neighbor)