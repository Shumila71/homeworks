class Num:
    def __init__(self, value):
        self.value = value

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class CalcVisitor:
    def visit(self, node):
        if isinstance(node, Num):
            return node.value
        elif isinstance(node, Add):
            return self.visit(node.left) + self.visit(node.right)
        elif isinstance(node, Mul):
            return self.visit(node.left) * self.visit(node.right)     


        
ast = Add(Num(7), Mul(Num(3), Num(2)))
cv = CalcVisitor()
print(cv.visit(ast))