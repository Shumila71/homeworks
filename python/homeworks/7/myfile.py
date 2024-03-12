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
        (2017,1971,1968,'C++'): 12,
        (2017,1971,1964,'C++'): 12,
        (2017,1971,1968,'NU'): 12,
        (2017,1971,1964,'NU'): 12,
        (2017,1971,1968,'MINID'): 12,
        (2017,1971,1964,'MINID'): 12,
        (2017,1965,1968,'C++'): 12,
        (2017,1965,1964,'C++'): 12,
        (2017,1965,1968,'NU'): 12,
        (2017,1965,1964,'NU'): 12,
        (2017,1965,1968,'MINID'): 12,
        (2017,1965,1964,'MINID'): 12,
        (2017,1978,1968,'C++'): 12,
        (2017,1978,1964,'C++'): 12,
        (2017,1978,1968,'NU'): 12,
        (2017,1978,1964,'NU'): 12,
        (2017,1978,1968,'MINID'): 12,
        (2017,1978,1964,'MINID'): 12,
        (1982,1971,1982,'C++'): 6,
        (1982,1965,1982,'C++'): 6,
        (1982,1978,1982,'C++'): 6,
        (1982,1965,1968,'C++'): 7, 
        (1982,1965,1964,'C++'): 7, 
        (1982,1978,1968,'C++'): 8,
        (1982,1978,1964,'C++'): 8,
        (1982,1978,1968,'NU'): 9,
        (1982,1965,1968,'NU'): 9,
        (1982,1971,1968,'NU'): 9,
        (1982,1978,1964,'NU'): 10,
        (1982,1965,1964,'NU'): 10,
        (1982,1971,1964,'NU'): 10,
        (1960,1965,1968,'C++'): 3,
        (1960,1965,1968,'NU'): 3,
        (1960,1965,1968,'MINID'): 3,
        (1960,1965,1964,'C++'): 4,
        (1960,1965,1964,'NU'): 4,
        (1960,1965,1964,'MINID'): 4,
        (1960,1971,1964,'C++'): 0,
        (1960,1971,1968,'C++'): 0,
        (1960,1971,1964,'NU'): 1,
        (1960,1971,1968,'NU'): 1,
        (1960,1971,1964,'MINID'): 2,
        (1960,1971,1968,'MINID'): 2,
        (1982,1971,1968,'MINID'): 11,
        (1982,1965,1964,'MINID'): 11,
        (1982,1978,1968,'MINID'): 11,
        (1982,1971,1964,'MINID'): 11,
        (1982,1965,1968,'MINID'): 11,
        (1982,1978,1964,'MINID'): 11,
        (1960,1978,1964,'C++'): 5,
        (1960,1978,1964,'NU'): 5,
        (1960,1978,1964,'MINID'): 5,
        (1960,1978,1968,'C++'): 5,
        (1960,1978,1968,'NU'): 5,
        (1960,1978,1968,'MINID'): 5,
    }
    tree.fit(lookup_table)
    return tree.predict(data)


print(main([1982, 1971, 1968, 'NU'])) #= 9
