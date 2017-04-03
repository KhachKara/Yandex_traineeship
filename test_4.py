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

class BinTree():
    def __init__(self, number): # инициализируем значение вершины дерева
        self.number = number
        self.left = None # необязательные параметры левый потомок
        self.right = None # необязательные параметры правый потомок
    def add_node(self,number, res = []):
        res.append(self.number)
        if number >= self.number:
            if self.right != None:
                # res.append(self.number)
                self.right.add_node(number)
            else:
                self.right = BinTree(number)
        else:
            if self.left != None:
                # res.append(self.number)
                self.left.add_node(number)
            else:
                self.left = BinTree(number)
        return res
tree =  BinTree(15)
m = [10, 16, 3, 12, 18, 13, 20, 17]

print(tree.add_node(10))
print(tree.add_node(16))
print(tree.add_node(3))
print(tree.add_node(12))
print(tree.add_node(18))
print(tree.add_node(13))
print(tree.add_node(20))
print(tree.add_node(17))
