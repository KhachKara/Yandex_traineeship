import random
import string


class BinTree:
    def __init__(self, node):
        self.level = None
        self.parent = None
        self.left_son = None
        self.right_son = None
        self.node = node

    def add_node(self, user_node, nodes = []):
        if user_node[0] > dict.values(self.node):
            self.right_son = user_node[0]
            nodes.append(user_node[0])
        elif user_node[0] < dict.values(self.node):
            self.left_son = user_node[0]
            nodes.append(user_node[0])
        else:
            return -1
        return nodes


name = ['A']
key = [15]
Node = {'name': key}

tree = BinTree(Node)

for j in range(10):
    key.append(random.randint(0, 20))
for k in range(0, 26):
    name.append(string.ascii_uppercase[random.randint(0, 25)])
    if k == 10:
        break
tree.add_node([key], name)
print(tree.add_node([key], name))
