from hypothesis import given
import hypothesis.strategies as st

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

# Strategy for generating expression trees
@st.composite
def expression_trees(draw):
    # Base case: generating a Num node
    if draw(st.booleans()):
        return Num(draw(st.integers()))
    # Recursive cases: generating Add or Mul nodes
    else:
        left = draw(expression_trees())
        right = draw(expression_trees())
        if draw(st.booleans()):
            return Add(left, right)
        else:
            return Mul(left, right)

# Strategy for generating expression trees with at least one Num node as leaf
@st.composite
def expression_trees_with_num(draw):
    tree = draw(expression_trees())
    # Ensure that the tree has at least one Num node as the leaf
    while not isinstance(tree, Num):
        tree = draw(expression_trees())
    return tree

# Property-based test for StackVisitor
@given(expression_trees_with_num())
def test_stack_visitor(expr):
    cv = StackVisitor()
    result = cv.visit(expr)
    # Assert that the result is a string
    assert isinstance(result, str)
    # Assert that the result doesn't contain any newlines
    assert '\n' not in result

# Run the test
test_stack_visitor()
