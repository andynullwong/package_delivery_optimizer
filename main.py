from dao.package_dao import package_id_address_map
from env import package_id_list_1, package_id_list_2, package_id_list_3
from model.clock import Clock
from model.package import Package
from model.van import Van

# Initialize Clock
clock = Clock()

# Initialize 3 Vans in Default Hub
van1 = Van(1)
van2 = Van(2)
van3 = Van(3)

# Loading vans with inventory
for package_id in package_id_list_1:
    package_address = package_id_address_map.get(package_id)
    package = Package(package_id, package_address)
    van1.add(package)

# for package_id in package_id_list_2:
#     van2.add(package_id)
#
# for package_id in package_id_list_3:
#     van3.add(package_id)

short_circuit = 0
is_done = len(van1) + len(van2) + len(van3) == 0

# Do While Loop emulation for Application Initial State
van1.tick(True)

# Server Event Loop
while not is_done and short_circuit < 200:
    clock.tick()
    delivered = van1.tick()

    short_circuit += 1


# for p in package_hashmap:
#     package = Package(p[0], p[1])
#     van1.add(package)
#
# for payload in van1.get_payload():
#     current_hub = van1.get_location()
#     destination_hub = payload.get_hub_name()
#
#     current_mileage = get_distance_to_hub(current_hub, destination_hub)
#
#
# next_package = get_nearest_package(default_hub, van1.get_payload())
# print("Next Step:", next_package)  # ('Columbus Library', 2.8)
