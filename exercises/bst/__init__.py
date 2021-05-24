# --- Directions
# 1) Implement the Node class to create
# a binary search tree.  The constructor
# should initialize values 'data', 'left',
# and 'right'.
# 2) Implement the 'insert' method for the
# Node class.  Insert should accept an argument
# 'data', then create and insert a new node
# at the appropriate location in the tree.
# 3) Implement the 'contains' method for the Node
# class.  Contains should accept a 'data' argument
# and return the Node in the tree with the same value.

'''
Concept
-------
In BST, the left node's value should be less than parent's and right node's value greater than parent's.
When inserting a new node, start from root node. If value is greater than root, repeat the same process on the right node, 
if lesser, repeat the same process on the left node.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

    def insert(self, data):
        '''recursive solution'''
        # if data < current node, insert on left hand side
        # if left hand side exists
        if data < self.data and self.left:
            self.left.insert(data)
        # if left hand side does not exist
        elif data < self.data:
            self.left = Node(data)
        # if data > current node, insert on right hand side
        # if right hand side exists
        elif data > self.data and self.right:
            self.right.insert(data)
        # if right hand side does not exist
        elif data > self.data:
            self.right = Node(data)

    def contains(self, data):
        '''recursive solution'''
        if self.data == data:
            return self

        if data < self.data and self.left:
            return self.left.contains(data)
        elif data > self.data and self.right:
            return self.right.contains(data)
        
        return None



node = Node(10)
node.insert(5)
node.insert(15)
node.insert(17)

print(node) # 10
print(node.left) # 5
print(node.right) # 15
print(node.right.right) # 17
print(node.contains(17)) # 17
print(node.contains(10)) # 10
print(node.contains(2)) # None
print(node.contains(19)) # None

