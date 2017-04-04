# Двоичное дерево поиска
# В заданном двоичном дереве поиска с дубликатами найдите все наиболее часто встречающиеся элементы.
# Считайте, что двоичное дерево поиска определено следующим образом:
# Левое поддерево узла состоит только из узлов с ключами, меньшими либо равными ключу данного узла.
# Правое поддерево узла состоит только из узлов с ключами, большими либо равными ключу данного узла.
# Левое поддерево и правое поддерево также являются двоичными деревьями поиска.
# Примечание: в случае, если наиболее часто встречающихся элементов более одного, их можно возвращать в любом порядке.
# Например, для дерева
#    1
#     \
#      2
#     /
#    2
# результат [2]
# Элемент двоичного дерева поиска на Java описывается вот таким классом:
# public class Node {
#     public final int val;
#     public final Node left;
#     public final Node right;
#     Node(int x) { val = x; }
# }


class BinTree:
    def __init__(self, node_number):  # инициализируем значение вершины дерева
        self.node_number = node_number
        self.left = None  # необязательные параметры левый потомок
        self.right = None  # необязательные параметры правый потомок

    def add_node(self, user_number):
        res = []
        if user_number >= self.node_number:
            if self.right is not None:
                self.right.add_node(user_number)
                res.append(str(self.node_number) + str('-->') + str(user_number))
            else:
                self.right = BinTree(user_number)
                res.append(str(self.node_number) + str('-->') + str(BinTree(user_number)))
        else:
            if self.left is not None:
                self.left.add_node(user_number)
                res.append(str(user_number) + str('<--') + str(self.node_number))
            else:
                self.left = BinTree(user_number)
                res.append(str(BinTree(user_number)) + str('<--') + str(self.node_number))
        return res

    def __repr__(self):
        return str(self.node_number)


tree = BinTree(15)
m = [10, 3, 12, 16, 18, 3, 24]
for i in m:
    print(tree.add_node(i))
