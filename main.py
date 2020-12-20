from datetime import datetime

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

for package_id in package_id_list_2:
    package_address = package_id_address_map.get(package_id)
    package = Package(package_id, package_address)
    van2.add(package)

for package_id in package_id_list_3:
    package_address = package_id_address_map.get(package_id)
    package = Package(package_id, package_address)
    van3.add(package)

short_circuit = 0
is_done = len(van1) == len(van2) == len(van3) == 0

# Do While Loop emulation for Application Initial State
van1.tick(True)
van2.tick(True)
van3.tick(True)

# Server Event Loop
while not is_done:

    delivered1 = False
    delivered2 = False
    delivered3 = False

    clock.tick()
    print("\nCurrent Time:", clock.get_time())

    if clock.get_time() >= datetime.strptime("2020-01-01 10:20:00", "%Y-%m-%d %H:%M:%S"):
        van2.update(9, "410 S State St")

    if not delivered1:
        delivered1 = van1.tick()

    if clock.get_time() >= datetime.strptime("2020-01-01 09:05:00", "%Y-%m-%d %H:%M:%S"):
        if not delivered2:
            delivered2 = van2.tick()
    if delivered1 or delivered2:
        delivered3 = van3.tick()

    if delivered1 and delivered2 and delivered3:
        is_done = True
        total_mileage = round(van1.get_mileage() + van2.get_mileage() + van3.get_mileage(), 1)
        print("Total Mileage:", total_mileage)
