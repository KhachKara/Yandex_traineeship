class BinTree:
    def __init__(self, node_name, node_key):
        self.level = None
        self.parent = None
        self.left_son = None
        self.right_son = None
        self.node_name = node_name
        self.node_key = node_key

    def add_node(self, user_node, nodes = []):
        if user_node > self.node_key:
            self.right_son = self.node_key
            nodes.append(self.node_key)
        elif user_node < self.node_key:
            self.left_son = self.node_key
            nodes.append(self.node_key)
        else:
            return -1
        return nodes

tree = BinTree('ABC', 15)
tree.add_node(10)
print(tree.add_node())
