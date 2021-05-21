# Tree Width and Level Width 
# --- Directions
# Given the root node of a tree, return
# an array where each element is the width
# of the tree at each level.
# --- Example
# Given:
#     0
#   / |  \
# 1   2   3
# |       |
# 4       5
# Answer: [1, 3, 2]


from typing import List


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


def levelWidth(root: Node) -> List[int]:
    counters = []  # will store the count of nodes in each level
    array = [root, 'stop']  # 'stop' denotes the end of that level
    width = 0  # width of level
    
    while len(array) > 1:  # > 1 prevents an infinite loop when only 'stop' is present in the array
        node = array[0]
        array.remove(node)
        if node == 'stop':
            counters.append(width)  # append level width to counters
            width = 0  # reset width 
            array.append('stop')  # move 'stop' to the end of array - this is similar to a "checkout divider" 
            # that people place between their order and then next person's 
        else:
            width += 1
            array += node.children
    
    # at the end of the while loop, array will appear as follows - ['stop']
    # since 'stop' would not be checked by the "if node == 'stop':" statement
    # the width will not be appended to counters
    # so, we do it manually below
    counters.append(width)

    return counters


root = Node('a')
root.add('b')
root.add('c')
root.children[0].add('d')
root.children[1].add('e')
print(levelWidth(root))  # 1, 2, 2
