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

    def __iter__(self):
        return iter(self.table)

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




ht = HashTable()
d = {}

for i in range(10):
    key = f'key{i}'
    value = f'value{i}'
    ht[key] = value
    d[key] = value

for key in d:
    assert key in ht

del ht['key5']
del d['key5']

for key in d:
    assert ht[key] == d[key]

assert len(ht) == len(d)
print("Все ок 2!")