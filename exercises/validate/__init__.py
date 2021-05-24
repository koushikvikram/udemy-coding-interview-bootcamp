#  --- Directions
#  Given a node, validate the binary search tree,
#  ensuring that every node's left hand child is
#  less than the parent node's value, and that
#  every node's right hand child is greater than
#  the parent

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

    def insert(self, data):
        if data < self.data and self.left:
            self.left.insert(data)
        elif data < self.data:
            self.left = Node(data)
        elif data > self.data and self.right:
            self.right.insert(data)
        elif data > self.data:
            self.right = Node(data)


def validate(node, min=None, max=None):
    # no validation required for root node
    # min and max will be set to None for root node
    if max and node.data > max:
        return False
    if min and node.data < min:
        return False

    # update max if we're moving to the left
    if node.left and not validate(node.left, min, node.data):
        return False    
    # update min if we're moving to the right
    if node.right and not validate(node.right, node.data, max):
        return False

    return True


# Try working through the following tree to understand the code better
#     10
#     /\
#    0 12


# Then, try working through the following tree to understand the code better
#          10
#         /  \
#        /    \
#       0     12
#      / \   /  \
#    -1   4 11  20
#      \       /  \
#      15     17  99


# valid BST
n = Node(10)
n.insert(5)
n.insert(15)
n.insert(0)
n.insert(20)
print(validate(n)) # True


# invalid BST
n = Node(10)
n.insert(5)
n.insert(15)
n.insert(0)
n.insert(20)
n.left.left.right = Node(999)
print(validate(n)) # False