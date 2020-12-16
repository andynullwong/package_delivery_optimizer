import math

from util.csv_reader import get_distance_hashmap, get_iterable_hubs, get_hubs, get_distance_matrix


default_hub = get_hubs().get(0)


def get_distance(location1, location2):
    return float(get_distance_hashmap().get(location1).get(location2))


def delete_node(location):
    for hub in get_iterable_hubs():
        get_distance_matrix().get(hub).delete(location)
        get_distance_matrix().get(location).delete(hub)


def find_shortest_edge(hashmap):
    closest_hub = None
    closest_location = math.inf

    for hub in get_iterable_hubs():
        if hub != default_hub and hashmap.get(hub) is not None:
            if float(hashmap.get(hub)) < float(closest_location):
                closest_hub = hub
                closest_location = float(hashmap.get(hub))
    return closest_hub, closest_location


def traverse_algo(departure=default_hub, mileage=0.0):
    hub_pointer = get_distance_matrix().get(departure)
    closest_hub, closest_location = find_shortest_edge(hub_pointer)
    if departure != default_hub:
        delete_node(departure)

    if closest_hub is None:
        closest_hub = default_hub
        closest_location = get_distance(departure, default_hub)
        print(departure, "->", closest_hub, mileage + closest_location)
        return closest_hub, mileage+closest_location
    else:
        print(departure, "->", closest_hub, mileage + closest_location)
        return traverse_algo(closest_hub, mileage+closest_location)


def test_output():
    print("=====Testing Matrix====")
    for hub in get_iterable_hubs():
        for nested_hub in get_iterable_hubs():
            if get_distance_matrix().get(hub).get(nested_hub) is not None:
                print(hub, "\t", nested_hub, "\t", get_distance_matrix().get(hub).get(nested_hub))


# test_output()
# delete_node('Western Governors University')
# print('-----------------')
# test_output()

# print(find_shortest_edge(get_distance_matrix().get('Western Governors University')))

print(traverse_algo())
