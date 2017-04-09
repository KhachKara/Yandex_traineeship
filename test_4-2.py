import random
__path = []
__bintree_list = []


class BinTree:
    def __init__(self, node_number):
        self.node_number = node_number
        self.left = None
        self.right = None
        self.len = 1

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
            self.len += 1
            return r
        return __path

    def __repr__(self):
        le = str(self.left.node_number) if self.left else str(self.left)
        r = str(self.right.node_number) if self.right else str(self.right)
        return le + ' <- ' + str(self.node_number) + ' -> ' + r

    def __contains__(self, value): # value in self
        '''Проверяет находится ли value в дереве self.'''
        if value > self.node_number:
            if self.right:
                return self.right.__contains__(value)
            else:
                return False
        elif value < self.node_number:
            if self.left:
                return self.left.__contains__(value)
            else:
                return False
        else:
            return True

    def to_list(self, fl = [0]):
        '''Возвращает отсортированный список'''
        global __bintree_list
        if fl[0] == 0:
            __bintree_list = []
        fl[0] += 1
        if self.left:
            self.left.to_list()
        __bintree_list.append(self.node_number)
        if self.right:
            self.right.to_list()
        fl[0] -= 1
        if fl[0] == 0:
            return __bintree_list

    #def __cmp__(self, other): # self == other
        
    def __nonzero__(self): # bool(self)
        return False if len == 0 else True

    def __len__(self): # len(self)
        return self.len

    def __iter__(self):
        if self.left:
            self.left.__iter__()
        yield self.node_number
        if self.right:
            self.right.__iter__()
        
        
        

tree = BinTree(10)
m = []
for j in range(50):
    m.append(random.randint(0, 20))
print(m)
for i in m:
    tree.add_node(i)
print(tree.to_list())
for i in range(21):
    print(str(i) + ' is ' + str(i in tree))
