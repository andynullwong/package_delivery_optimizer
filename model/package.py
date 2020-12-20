from dao.hub_dao import address_hub_map


class Package:
    def __init__(self, package_id, address):
        self.package_id = package_id
        self.address = address
        self.hub_name = address_hub_map.get(address)
        self.enroute = None
        self.delivered = None

    def get_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def get_enroute(self):
        return self.enroute

    def get_delivered(self):
        return self.delivered

    def get_hub_name(self):
        return self.hub_name

    def set_address(self, new_address):
        self.address = new_address
        self.hub_name = address_hub_map.get(new_address)

    def set_enroute(self, timestamp):
        self.enroute = timestamp

    def set_delivered(self, timestamp):
        self.delivered = timestamp

    def get_status(self, timestamp):
        status = "delivered" if (self.delivered is not None and timestamp >= self.delivered) else "en_route" if (
                self.enroute is not None and timestamp >= self.enroute) else "at_hub"
        # status = "at_hub"
        # if timestamp >= self.enroute:
        #     print(timestamp)
        #     print(self.enroute)
        #     status = "en_route"
        # if timestamp >= self.delivered:
        #     status = "delivered"
        return status
