
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node [' + str(self.data) + ']'


class Tree:  # класс, описывающий само дерево
    def __init__(self):
        self.root = None  # корень дерева

    def newNode(self, data):  # функция для добавления узла в дерево
        return Node(data,None,None)

    def height(self, node):  # функция для вычисления высоты дерева
        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)

            if l_height > r_height:
                return (l_height + 1)
            else:
                return (r_height + 1)

    def mirrorTree(self, node):  # функция для зеркального отражения дерева
        if node.left and node.right:
            node.left, node.right = node.right, node.left
            self.mirrorTree(node.right)
            self.mirrorTree(node.left)
        else:
            if node.left == None and node.right:
                return self.mirrorTree(node.right)
            if node.right == None and node.left:
                return self.mirrorTree(node.left)

    def lookup(self, node, target):  # функция для проверки наличия узла
        if node == None:return 0
        else:
            if target == node.data: return 1
            else:
                if target < node.data: return self.lookup(node.left, target)
                else: return self.lookup(node.right, target)

    def getMaxWidth(self,root):  # функция для вычисления ширины дерева
      maxWdth = 0
      i = 1
      width = 0
      h = self.height(root)
      while( i< h):
        width =   self.getWidth(root, i)
        if(width > maxWdth):
            maxWdth = width
        i +=1
      return maxWdth

    def getWidth(self, root, level):
      if root == None:
        return 0
      if level == 1:
        return 1
      elif level > 1:
          return self.getWidth(root.left, level-1) +  self.getWidth(root.right, level-1)

    def printGivenLevel(self, root, level):  # функция для распечатки элементов на определенном уровне дерева
        if root == None:
            return
        if level == 1:
            print("%d " % root.data)
        elif level > 1:
            self.printGivenLevel(root.left, level - 1)
            self.printGivenLevel(root.right, level - 1)

    def printLevelOrder(self, root):  # функция для распечатки дерева
        h = self.height(self.root)
        i = 1
        while (i <= h):
            self.printGivenLevel(self.root, i)
            i += 1

    def sameTree(a, b):
        if a is None and b is None:
            return 1
        elif a and b:
            return (
                a.data == b.data and
                sameTree(a.left, b.left) and
                sameTree(a.right, b.right)
            )
        return 0

    def size(node):
        if node == None: return 0;
        return (size(node.left) + 1 + size(node.right));