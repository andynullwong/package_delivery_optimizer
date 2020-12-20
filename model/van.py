from dao.history_dao import package_history
from dao.package_dao import get_nearest_package
from env import default_hub
from model.clock import clock


class Van:
    def __init__(self, van_id):
        self.id = van_id
        self.capacity = 16
        self.payload = []
        self.mileage = 0.0
        self.location = default_hub
        self.destination = None
        self.destination_miles = 0.0
        self.speed = 0.3  # miles/minute, miles per tick

    def __len__(self):
        return len(self.payload)

    def add(self, package_id):
        if len(self.payload) == self.capacity:
            return False
        self.payload.append(package_id)
        return True

    def update(self, package_id, address):
        for package in self.payload:
            if package_id == package.get_id():
                package.set_address(address)

    def remove(self, hub_name):
        for idx, package in enumerate(self.payload):
            if package.get_hub_name() == hub_name:
                package.set_delivered(clock.get_time())
                package_history.add(package.get_id(), package)
                # print("Van", self.id, "unloaded package", package.get_id(), "at", package.get_hub_name())
                del self.payload[idx]

    def add_mileage(self, mileage):
        self.mileage += mileage

    def get_id(self):
        return self.id

    def get_payload(self):
        return self.payload

    def get_mileage(self):
        return round(self.mileage, 1)

    def get_location(self):
        return self.location

    def get_speed(self):
        return self.speed

    def calculate_next(self):
        return get_nearest_package(self.location, self.payload)

    def tick(self, initial=False) -> bool:
        if initial:
            next_hub, destination_miles = self.calculate_next()
            self.destination = next_hub
            self.destination_miles += destination_miles
            return False
        else:
            if len(self.payload) != 0:
                self.mileage += self.speed
            if self.destination_miles <= 0.0:
                self.remove(self.destination)
                next_hub, destination_miles = self.calculate_next()
                self.location = self.destination
                self.destination = next_hub
                if self.location is self.destination:
                    print("Van", self.id, '| Returned to Hub')
                    return True
                self.destination_miles += destination_miles
                print("Van", self.id, '|', self.location, '|', self.destination, '|', self.destination_miles)
                return False
            self.destination_miles -= self.speed
            print("Van", self.id, '|', self.location, '|', self.destination, '|', self.destination_miles)
            return False
