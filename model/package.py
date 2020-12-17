from dao.hub_dao import address_to_hub_hashmap, distance_matrix


class Package:
    def __init__(self, package_id, address, state, zipcode, deadline, notes):
        self.package_id = package_id
        self.address = address
        self.hub_name = address_to_hub_hashmap.get(address)
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.notes = notes

    def get_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address
        self.hub_name = address_to_hub_hashmap.get(new_address)

    def get_distance_to_hub(self, next_hub_name):
        return float(distance_matrix.get(self.hub_name).get(next_hub_name))
