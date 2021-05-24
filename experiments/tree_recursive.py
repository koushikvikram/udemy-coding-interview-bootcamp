class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def __repr__(self):
        return str(self.data)
    
    def add(self, data):
        self.children.append(Node(data))
    
    def remove(self, data):
        self.children = list(
            filter(
                lambda x : x!=data,
                self.children
            )
        )


class Tree:
    def __init__(self):
        self.root = None

    def traverseBF(self, fn=print, array=None):
        '''recursive implementation'''
        # this is done because setting array=self.root as default argument is not possible in Python
        if array is None:
            array = [self.root]

        if not array:
            return

        node = array[0]
        array.remove(node)
        array += node.children
        node = fn(node)
        
        return self.traverseBF(fn, array)

    def traverseDF(self, fn=print, array=None):
        '''recursive implementation'''
        # this is done because setting array=self.root as default argument is not possible in Python
        if array is None:
            array = [self.root]

        if not array:
            return

        node = array[0]
        array.remove(node)
        array = node.children + array
        node = fn(node)
        

        return self.traverseDF(fn, array)



# n = Node('a')
# print(n)
# n.add('b')
# n.add('c')
# print(n)
# n.remove('c')
# print(n)


# t = Tree()
# t.root = Node('a')
# t.root.add('b')
# t.root.add('c')
# t.root.children[0].add('d')
# #       a
# #      / \
# #     b   c
# #    /
# #   d
# t.traverseBF()  # 'a', 'b', 'c', 'd'


t = Tree()
t.root = Node('a')
t.root.add('b')
t.root.add('d')
t.root.children[0].add('c')
#       a
#      / \
#     b   d
#    /
#   c
t.traverseDF()  # 'a', 'b', 'c', 'd'

