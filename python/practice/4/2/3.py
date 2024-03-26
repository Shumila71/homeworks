class HashTable:
    def __init__(self):
        self.table = []

    def __setitem__(self, key, value):
        for i in range(len(self.table)):
            if self.table[i][0] == key:
                self.table[i] = (key, value)
                return
        self.table.append((key, value))

    def __getitem__(self, key):
        for k, v in self.table:
            if k == key:
                return v
        raise KeyError(key)

    def __len__(self):
        return len(self.table)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __delitem__(self, key):
        for i in range(len(self.table)):
            if self.table[i][0] == key:
                del self.table[i]
                return
        raise KeyError(key)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.table):
            raise StopIteration
        result = self.table[self.current]
        self.current += 1
        return result

ht = HashTable()
d = {}

for i in range(10):
    key = f'key{i}'
    value = f'value{i}'
    ht[key] = value
    d[key] = value

for pair_ht, pair_d in zip(ht, d.items()):
    assert pair_ht == pair_d

print("Все ок 3!")