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
        if dict.keys(user_node) > dict.keys(self.node):
            self.right_son = dict.keys(user_node)
            nodes.append(dict.values(user_node))
        elif dict.keys(user_node) < dict.keys(self.node):
            self.left_son = dict.keys(user_node)
            nodes.append(dict.values(user_node))
        else:
            return -1
        return nodes


name = 'A'
key = [15]
Node = {name: key}

tree = BinTree(Node)

for i in range(10):
    dict.keys(Node)

tree.add_node(Node)
print(tree.add_node(Node))


# for j in range(10):
#     key.append(random.randint(0, 20))
# for k in range(0, 26):
#     name.append(string.ascii_uppercase[random.randint(0, 25)])
#     if k == 10:
#         break