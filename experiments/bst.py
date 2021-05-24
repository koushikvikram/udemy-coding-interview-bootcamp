from typing import Union


class Node:
    def __init__(self):
        self.data = None
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

    def contains(self, data):
        if data == self.data:
            return self
        if data < self.data and self.left:
            return self.left.contains(data)
        elif data > self.data and self.right:
            return self.right.contains(data)
        
        return None

