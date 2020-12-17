import math

from dao.hub_dao import hub_hashmap, distance_matrix

from model.van import Van

# default_hub = "Western Governors University"
default_hub = hub_hashmap.get(0)


# get_distance("Columbus Library", "Council Hall") # 5.1
def get_distance(location1, location2):
    return float(distance_matrix.get(location1).get(location2))


# arguments is current location and list of packages on van
def find_next_edge(van: Van):
    closest_node = None
    closest_location = math.inf

