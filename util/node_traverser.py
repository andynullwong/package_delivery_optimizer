import math

from dao.hub_daos import hub_hashmap, get_distance_hashmap, distance_matrix

# default_hub = "Western Governors University"
default_hub = hub_hashmap.get(0)


# get_distance("Columbus Library", "Council Hall") # 5.1
def get_distance(location1, location2):
    return float(distance_matrix.get(location1).get(location2))


# arguments is current location and list of packages on van
# def find_shortest_edge(current_node, node_hashmap):
#     closest_node = None
#     closest_location = math.inf
