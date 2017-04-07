class BinTree:
    def __init__(self, top, node, level):
        self.top = top
        self.node = node
        self.level = level

class BinNode:
    def __init__(self, left_son, right_son, node_name, node_key):
        self.parent = None
        self.left_son = left_son
        self.right_son = right_son
        self.node_name = node_name
        self.node_key = node_key
    def add_node(self):


tree = BinTree(10, 20, 5)
noode = BinNode(True, False, 'ABC', 15)

