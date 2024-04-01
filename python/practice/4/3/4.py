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

class StackVisitor:
    def visit(self, node):
        if isinstance(node, Num):
            return f"PUSH {node.value}"
        elif isinstance(node, Add):
            return f"{self.visit(node.left)}\n{self.visit(node.right)}\nADD"
        elif isinstance(node, Mul):
            return f"{self.visit(node.left)}\n{self.visit(node.right)}\nMUL"


        
ast = Add(Num(7), Mul(Num(3), Num(2)))
cv = StackVisitor()
print(cv.visit(ast))