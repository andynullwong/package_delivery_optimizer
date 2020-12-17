class Van:
    def __init__(self):
        self.capacity = 16
        self.payload = []
        self.mileage = 0

    def __len__(self):
        return len(self.payload)

    def add(self, package_id):
        if len(self.payload) == self.capacity:
            return False
        self.payload.append(package_id)
        return True

    def remove(self, package_id):
        self.payload.remove(package_id)

    def move(self, mileage):
        self.mileage += mileage

    def get_payload(self):
        return self.payload

    def get_mileage(self):
        return self.mileage
