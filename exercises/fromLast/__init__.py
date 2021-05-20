# --- Directions
# Given a linked list, return the element n spaces
# from the last node in the list.  Do not call the 'size'
# method of the linked list.  Assume that n will always
# be less than the length of the list.
# --- Examples
#    l = LinkedList()
#    l.insertLast('a')
#    l.insertLast('b')
#    l.insertLast('c')
#    l.insertLast('d')
#    fromLast(l, 2).data # 'b'


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


def fromLast(linked_list, n):
    slow = linked_list.getFirst()
    fast = linked_list.getAt(n)

    # if 'getAt' is not allowed, use a for loop
    # for _ in range(n):
    #     fast = fast.next

    # slow pointer will always be 'n' nodes behind fast pointer
    while fast.next:
        slow = slow.next
        fast = fast.next
    # when fast pointer reaches the end, slow pointer will be 'n' nodes behind the end
    return slow


l = LinkedList()
l.insertLast('a')
l.insertLast('b')
l.insertLast('c')
l.insertLast('d')
print(fromLast(l, 2).data) # 'b'
