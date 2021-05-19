# Linked List

''' Stub
class LinkedList:
    def __init__(self):
        raise NotImplementedError
    def insertFirst(self, data):
        raise NotImplementedError
    def size(self):
        raise NotImplementedError
    def getFirst(self):
        raise NotImplementedError
    def getLast(self):
        raise NotImplementedError
    def clear(self):
        raise NotImplementedError
    def removeFirst(self):
        raise NotImplementedError
    def removeLast(self):
        raise NotImplementedError
    def insertLast(self, data):
        raise NotImplementedError
    def getAt(self, index):
        raise NotImplementedError
    def removeAt(self, index):
        raise NotImplementedError
    def insertAt(self, data, index):
        raise NotImplementedError
    def forEach(self, fn):
        raise NotImplementedError

for node in LinkedList:
    # doing this should be possible

'''


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


l = LinkedList()
print(l.getFirst()) # None
print(l.getLast()) # None
l.head = Node(10)
print(l.head) # 10
l.insertFirst(20)
l.insertFirst(30)
print(l.head) # 30
print(l.head.next) # 20
print(l.size()) # 3
print(l.getFirst()) # 30
print(l.getLast()) # 10
# l.clear()
# print(l.size()) # ------ 0
l.removeFirst()
print(l.getFirst()) # 20
# x = LinkedList()
# print(x.removeFirst()) # ------ None
l.removeLast()
print(l.getLast()) # 20
# x = LinkedList()
# x.insertFirst(10)
# x.removeLast()
# print(x.getLast()) # None
# x.removeLast()
# print(x.getLast()) # None
l.insertLast(10)
print(l.getLast()) # 10
# x = LinkedList()
# print(x.getAt(1)) # None
l.insertFirst(30)
print(l.getAt(2)) # 10

l.removeAt(0)
print(l.getAt(0)) # 20
l.insertFirst(30)
l.removeAt(1)
print(l.getAt(1)) # 10
# print(l.size())
# print(l.getAt(0))

l.insertAt(1, 20)
print(l.getAt(1)) # 20

l.forEach(lambda x: x*2)
print(l.getFirst()) # 60
print(l.getLast()) # 20

for n in l: # 60, 40, 20
    print("Inside iterator: {}".format(n.data))
    