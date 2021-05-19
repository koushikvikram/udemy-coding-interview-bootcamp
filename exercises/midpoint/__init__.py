# --- Directions
# Return the 'middle' node of a linked list.
# If the list has an even number of elements, return
# the node at the end of the first half of the list.
# *Do not* use a counter variable, *do not* retrieve
# the size of the list, and only iterate
# through the list one time.
# --- Example
#   const l = new LinkedList();
#   l.insertLast('a')
#   l.insertLast('b')
#   l.insertLast('c')
#   midpoint(l); # returns { data: 'b' }


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        if not self.head:
            return 0
        
        length = 1
        node = self.head.next
        
        while node:
            length += 1
            node = node.next
            
        return length

    def getFirst(self):
        return self.head
    
    def getLast(self):
        if not self.head:
            return None
        
        node = self.head
        
        while node.next:
            node = node.next
        
        return node

    def clear(self):
        self.head = None

    def removeFirst(self):
        if self.head:
            self.head = self.head.next

    def removeLast(self):
        if not self.head or not self.head.next:
            self.head = None
        else:
            node = self.head
            while node.next.next:
                node = node.next
            node.next = None

    def insertLast(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.getLast()
            node.next = Node(data)

    def getAt(self, index):
        # if index is out of bounds, return None
        i = 0
        node = self.head
        while node:
            if i == index:
                return node
            i += 1
            node = node.next
        return node
        
    def removeAt(self, index):
        if index == 0:
            self.removeFirst()
        elif index == self.size()-1:
            self.removeLast()
        else:
            previous_node = self.getAt(index-1)
            previous_node.next = previous_node.next.next

    def insertAt(self, index, data):
        if index == 0:
            self.insertFirst(data)
        else:
            previous_node = self.getAt(index-1)
            previous_node.next = Node(data, previous_node.next)

    def forEach(self, fn):
        node = self.head
        while node:
            node.data = fn(node.data)
            node = node.next

    def __iter__(self):
        '''make linked list iterable'''
        node = self.head
        while node:
            yield node
            node = node.next


# # method 1
# def midpoint(linked_list):
#     '''recursive solution'''
#     # base case 1
#     if not linked_list.head.next:
#         return linked_list.head
#     # base case 2
#     elif not linked_list.head.next.next:
#         return linked_list.head
#     # recursive case
#     linked_list.removeFirst()
#     linked_list.removeLast()
#     return midpoint(linked_list)


# method 2
def midpoint(linked_list):
    '''fast and slow pointers'''
    slow = linked_list.getFirst()
    fast = linked_list.getFirst()

    while fast.next and fast.next.next:
        # fast.next checked to handle linked list with only two nodes
        slow = slow.next
        fast = fast.next.next
    
    return slow


l = LinkedList()
l.insertLast('a')
l.insertLast('b')
print(midpoint(l).data) # a
l.insertLast('c')
l.insertLast('d') 
print(midpoint(l).data) # b
l.insertLast('e')
print(midpoint(l).data) # c
