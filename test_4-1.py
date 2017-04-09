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


name = ['A']
key = [15]
Node = {name[0]: key}
node_list = []  # список узлов



tree = BinTree(Node)
number = int(input('Количество узлов: '))
for i in range(number):
    name.append(string.ascii_uppercase[random.randint(0, 25)])
    key.append(random.randint(0, 100))
    node_list.append(Node.fromkeys(name[i], key[i]))

print(node_list)