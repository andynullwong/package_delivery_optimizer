# Andy Wong
# C950: Data Structures & Algorithms II
# ID: 001349684

from dao.package_dao import package_id_address_map
from env import package_id_list_1, package_id_list_2, package_id_list_3
from lookup import lookup
from model.clock import string_to_timestamp, clock
from model.package import Package
from model.van import Van

# Initialize 3 Vans in Default Hub
van1 = Van(1)
van2 = Van(2)
van3 = Van(3)

# Loading vans with packages
for package_id in package_id_list_1:
    (address, city, zipcode, deadline, weight) = package_id_address_map.get(package_id)
    package = Package(package_id, address, city, zipcode, deadline, weight)
    package.set_enroute(string_to_timestamp("2020-01-01 08:00:00"))
    van1.add(package)

for package_id in package_id_list_2:
    address, city, zipcode, deadline, weight = package_id_address_map.get(package_id)
    package = Package(package_id, address, city, zipcode, deadline, weight)
    package.set_enroute(string_to_timestamp("2020-01-01 09:05:00"))
    van2.add(package)

for package_id in package_id_list_3:
    address, city, zipcode, deadline, weight = package_id_address_map.get(package_id)
    package = Package(package_id, address, city, zipcode, deadline, weight)
    package.set_enroute(string_to_timestamp("2020-01-01 09:13:00"))
    van3.add(package)

is_done = len(van1) == len(van2) == len(van3) == 0

# Since Do While Loop is not supported in Python, emulation for Application Initial State by passing in a boolean
van1.tick(True)
van2.tick(True)
van3.tick(True)

# Server Event Loop. Will print out each 3 Van's current objective in one minute intervals after it leaves the first Hub
print("Delivery Route Time Series Simulation (1min)")
while not is_done:

    delivered1 = False
    delivered2 = False
    delivered3 = False

    clock.tick()
    print("\nCurrent Time:", clock.get_time())

    # The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
    if clock.get_time() >= string_to_timestamp("2020-01-01 10:20:00"):
        van2.update(9, "410 S State St")

    if not delivered1:
        delivered1 = van1.tick()

    # Packages in van2 cannot leave until 09:05
    if clock.get_time() >= string_to_timestamp("2020-01-01 09:05:00"):
        if not delivered2:
            delivered2 = van2.tick()

    # van3 cannot leave until at least one driver returns
    if delivered1 or delivered2:
        delivered3 = van3.tick()

    # Base Case for this while loop, when all three vans have empty payloads
    if delivered1 and delivered2 and delivered3:
        is_done = True
        total_mileage = round(van1.get_mileage() + van2.get_mileage() + van3.get_mileage(), 1)
        print("\nTotal Mileage:", total_mileage, "SUCCESS" if total_mileage <= 140 else "FAILED")
print("\nSimulation Completed!")

# Lookup Function
lookup()
