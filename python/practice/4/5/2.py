
from SVG import SVG

scale_x = 20
scale_y = 50
svg = SVG()


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.root=None
        if left != None:
            self.left.root = self
        if right != None:
            self.right.root = self
        self.x = 250
        self.y = 0
        self.height = getHeight(self)
    def upd(self,mix=1000,ma=0):
        mix,ma = min(self.x,mix),max(ma,self.x)
        if self.left!=None:
            self.left.x = self.x - scale_x*(self.left.height)
            self.left.y = self.y + scale_y
            l = self.left.upd()
            mix, ma = min(l[0], mix), max(ma, l[1])
        if self.right != None:
            self.right.x = self.x + scale_x*(self.right.height)
            self.right.y = self.y + scale_y
            r = self.right.upd()
            mix, ma = min(r[0], mix), max(ma, r[1])
        return mix,ma
    def viz(self):
        if self.left != None:
            self.left.viz()
        svg.circle(self.x,self.y,r=5,color='black')
        if self.root!=None:
            svg.line(self.x, self.y, self.root.x, self.root.y, color='black')
        if self.right != None:
            self.right.viz()


def getHeight(root):
    if root == None:
        return -1
    else:
        return 1 + max(getHeight(root.left), getHeight(root.right))


tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)
tree.x = 400
s = tree.upd()
tree.x = (s[1]-s[0])//2 + (s[1]-s[0])//2*0.5

tree.upd()
tree.left.x = tree.x-max(tree.x-tree.left.x,tree.right.x-tree.x)
tree.left.upd()
tree.viz()
svg.save('pic.svg',1000,tree.height*scale_y + 20)
# height = getHeight(tree)
# y = scale_y*height
# x = 0

