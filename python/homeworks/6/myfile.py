class DecisionTree:
    def __init__(self, threshold=None, value=None, children=None):
        self.threshold = threshold
        self.value = value
        self.children = children if children is not None else {}

    def fit(self, data_points):
        for data_point, result in data_points.items():
            node = self
            for feature in data_point:
                if feature not in node.children:
                    node.children[feature] = DecisionTree()
                node = node.children[feature]
            node.value = result

    def predict(self, data_point):
        node = self
        for feature in data_point:
            if feature not in node.children:
                return None
            node = node.children[feature]
        return node.value


def main(data):
    tree = DecisionTree()
    lookup_table = {
        ("MUPAD", 1974, 1985, 2019): 0,
        ("MUPAD", 1974, 1985, 2014): 0,
        ("MUPAD", 1989, 1985, 2019): 1,
        ("MUPAD", 1989, 1985, 2014): 1,
        ("MUPAD", 2012, 1985, 2019): 2,
        ("MUPAD", 2012, 1985, 2014): 2,
        ("MUPAD", 1974, 2005, 2019): 3,
        ("MUPAD", 1989, 2005, 2019): 3,
        ("MUPAD", 2012, 2005, 2019): 3,
        ("MUPAD", 1974, 2005, 2014): 4,
        ("MUPAD", 1989, 2005, 2014): 4,
        ("MUPAD", 2012, 2005, 2014): 4,
        ("MUPAD", 1974, 1965, 2019): 5,
        ("MUPAD", 1989, 1965, 2019): 5,
        ("MUPAD", 2012, 1965, 2019): 5,
        ("MUPAD", 1974, 1965, 2014): 5,
        ("MUPAD", 1989, 1965, 2014): 5,
        ("MUPAD", 2012, 1965, 2014): 5,
        ("VHDL", 1974, 1965, 2019): 6,
        ("VHDL", 1974, 1985, 2019): 6,
        ("VHDL", 1974, 2005, 2019): 6,
        ("VHDL", 1974, 1965, 2014): 6,
        ("VHDL", 1974, 1985, 2014): 6,
        ("VHDL", 1974, 2005, 2014): 6,
        ("VHDL", 1989, 1965, 2019): 7,
        ("VHDL", 1989, 1985, 2019): 7,
        ("VHDL", 1989, 2005, 2019): 7,
        ("VHDL", 1989, 1965, 2014): 8,
        ("VHDL", 1989, 1985, 2014): 8,
        ("VHDL", 1989, 2005, 2014): 8,
        ("VHDL", 2012, 1965, 2019): 9,
        ("VHDL", 2012, 1985, 2019): 9,
        ("VHDL", 2012, 2005, 2019): 9,
        ("VHDL", 2012, 1965, 2014): 9,
        ("VHDL", 2012, 1985, 2014): 9,
        ("VHDL", 2012, 2005, 2014): 9,
        ("CLEAN", 2012, 1965, 2019): 10,
        ("CLEAN", 2012, 1985, 2019): 10,
        ("CLEAN", 2012, 2005, 2019): 10,
        ("CLEAN", 2012, 1965, 2014): 10,
        ("CLEAN", 2012, 1985, 2014): 10,
        ("CLEAN", 2012, 2005, 2014): 10,
        ("CLEAN", 1974, 1965, 2019): 10,
        ("CLEAN", 1974, 1985, 2019): 10,
        ("CLEAN", 1974, 2005, 2019): 10,
        ("CLEAN", 1974, 1965, 2014): 10,
        ("CLEAN", 1974, 1985, 2014): 10,
        ("CLEAN", 1974, 2005, 2014): 10,
        ("CLEAN", 1989, 1965, 2019): 10,
        ("CLEAN", 1989, 1985, 2019): 10,
        ("CLEAN", 1989, 2005, 2019): 10,
        ("CLEAN", 1989, 1965, 2014): 10,
        ("CLEAN", 1989, 1985, 2014): 10,
        ("CLEAN", 1989, 2005, 2014): 10,
    }
    tree.fit(lookup_table)
    return tree.predict(data)


print(main(["VHDL", 1974, 1985, 2014]))
