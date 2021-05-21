# --- Directions
# 1) Create a node class.  The constructor
# should accept an argument that gets assigned
# to the data property and initialize an
# empty array for storing children. The node
# class should have methods 'add' and 'remove'.
# 2) Create a tree class. The tree constructor
# should initialize a 'root' property to null.
# 3) Implement 'traverseBF' and 'traverseDF'
# on the tree class.  Each method should accept a
# function that gets called with each element in the tree

# In a tree, we have to very precisely specify which node to add or remove elements from
# So, a generic add or remove method can't be used like how they're used in a linked list

# Eg. Tree:
#            20
#           /|\
#          / | \
#         0 40 -15
#        /|\    |
#       / | \   |
#      12 -2 1 -2

# TraverseBF - Remove node and apply function to it, then add it's children to END of Array
# 
# Array: [20]
#                                                                       Array: [], Removed first node, node = 20
# Array: [0, 40, -15] # children of removed node added to end of array
#                                                                       Array: [40, -15], Removed first node, node = 0
# Array: [40, -15, 12, -2, 1] # children of removed node added to end of array
#                                                                       Array: [-15, 12, -2, 1] # Removed first node, node = 40
# Array: [-15, 12, -2, 1] # no children to be added to end of array
#                                                                       Array: [12, -2, 1] # Removed first node, node = -15
# Array: [12, -2, 1, -2] # children of removed node added to end of array
#                                                                       Array: [-2, 1, -2] # Removed first node, node = 12
# Array: [-2, 1, -2] # no children to be added
#                                                                       Array: [1, -2] # Removed first node, node = -2
# Array: [1, -2] # no children to be added
#                                                                       Array: [-2] # Removed first node, node = 1
# Array: [-2] # no children to be added
#                                                                       Array: [] # Removed first node, node = -2
# Array: [] # no children to be added
#                                                                       Empty array, so while Array: evaluates to False, terminate loop


# TraverseDF - Remove node and apply function to it, then add it's children to BEGINNING of Array
# Array: [20]
#                                                                       Array: [], Removed first node, node = 20
# Array: [0, 40, -15] # children of removed node added to beginning of array
#                                                                       Array: [40, -15], Removed first node, node = 0
# Array: [12, -2, 1, 40, -15] # children of removed node added to beginning of array
#                                                                       Array: [-2, 1, 40, -15] # Removed first node, node = 12
# Array: [-2, 1, 40, -15] # no children to be added to beginning of array
#                                                                       Array: [1, 40, -15] # Removed first node, node = -2
# Array: [1, 40, -15] # no children to be added to beginning of array
#                                                                       Array: [40, -15] # Removed first node, node = 1
# Array: [40, -15] # no children to be added
#                                                                       Array: [-15] # Removed first node, node = 40
# Array: [-15] # no children to be added
#                                                                       Array: [] # Removed first node, node = -15
# Array: [-2] # children of removed node added to beginning of array
#                                                                       Array: [] # Removed first node, node = -2
# Array: [] # no children to be added
#                                                                       Empty array, so while Array: evaluates to False, terminate loop



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
                lambda x: x.data!= data, 
                self.children
            )
        )


class Tree:
    def __init__(self):
        self.root = None
    
    def traverseBF(self, fn):
        array = [self.root]
        while array:
            node = array[0]  # get first node from array
            array.remove(node)  # remove this node from array
            array = array + node.children  # push the node's children to the END of the array
            node = fn(node)  # apply function to node

    def traverseDF(self, fn):
        array = [self.root]
        while array:
            node = array[0] # get first node from array
            array.remove(node) # remove this node from array
            array = node.children + array # push the node's children to the BEGINNING of the array
            node = fn(node) # apply function to node


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
#       a
#      / \
#     b   c
#    /
#   d
# t.traverseBF(print)  # 'a', 'b', 'c', 'd'


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
t.traverseDF(print)  # 'a', 'b', 'c', 'd'
