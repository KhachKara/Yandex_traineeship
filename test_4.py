import random
__path = []
class BinTree:
    def __init__(self, node_number):  # инициализируем значение вершины дерева
        self.node_number = node_number
        self.left = None  # необязательные параметры левый потомок
        self.right = None  # необязательные параметры правый потомок


    def add_node(self, user_number, fl = [0]):
        global __path
        if fl[0] == 0:
            __path = [self.node_number]
        else:
            __path.append(self.node_number)
        fl[0] += 1
        if user_number >= self.node_number:
            if self.right is None:
                self.right = BinTree(user_number)
                __path.append(user_number)
            else:
                self.right.add_node(user_number)
        else:
            if self.left is None:
                self.left = BinTree(user_number)
                __path.append(user_number)
            else:
                self.left.add_node(user_number)
        fl[0] -= 1
        if fl[0] == 0:
            r = __path[:]
            __path = []
            return r
        return __path

    def __repr__(self):
        return str(self.node_number)


tree = BinTree(15)
m = []
for j in range(10):
    m.append(random.randint(0, 20))
print(m)
for i in m:
    print(tree.add_node(i))