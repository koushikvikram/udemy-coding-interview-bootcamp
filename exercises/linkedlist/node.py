# the 'Node' class

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return str(self.data)


n0 = Node("!")
n1 = Node('There', n0)
n2 = Node("Hi", n1)
n3 = Node(", ", n2)
n4 = Node("Hello", n3)

print("{}{}{} {}{}".format(
    n4, 
    n4.next, 
    n3.next, 
    n2.next, 
    n1.next
    )
)
