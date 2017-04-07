import random
import string


class BinTree:
    def __init__(self, node_name, node_key):
        self.level = None
        self.parent = None
        self.left_son = None
        self.right_son = None
        self.node_name = node_name
        self.node_key = node_key

    def add_node(self, user_node, nodes = []):
        if user_node[1] > self.node_key:
            self.right_son = user_node[1]
            nodes.append(user_node[1])
        elif user_node[1] < self.node_key:
            self.left_son = user_node[1]
            nodes.append(user_node[1])
        else:
            return -1
        return nodes


name = ['ABC']
key = [15]
tree = BinTree(name, key)

for j in range(10):
    key.append(random.randint(0, 20))
for k in string.ascii_uppercase:
    name.append(random.randint(0, 26))
tree.add_node([key], name)
print(tree.add_node([key], name))

