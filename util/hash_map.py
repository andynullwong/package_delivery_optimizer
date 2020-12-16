class HashMap:
    def __init__(self):
        self.capacity = 32
        self.length = 0
        self.map = [[] for _ in range(self.capacity)]
        self.iterator = 0
        self.iterator1 = 0
        self.iterator2 = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator < self.length:
            while len(self.map[self.iterator1]) == 0:
                self.iterator1 += 1
                self.iterator2 = 0
            value = self.map[self.iterator1][self.iterator2]
            if self.iterator2 == len(self.map[self.iterator1])-1:
                self.iterator1 += 1
                self.iterator2 = 0
            else:
                self.iterator2 += 1
            self.iterator += 1
            return value
        else:
            raise StopIteration

    def _get_hash(self, key):
        return hash(key) % self.capacity

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            self.length += 1
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            self.length += 1
            return True

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                self.length -= 1
                # if len(self.map[key_hash]) == 0:
                #     self.map[key_hash] = None
                return True
        return False

    def print(self):
        for row in self.map:
            print(row)
