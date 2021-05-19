# Queue Weaving
# --- Directions
# 1) Complete the task in weave/queue.js
# 2) Implement the 'weave' function.  Weave
# receives two queues as arguments and combines the
# contents of each into a new, third queue.
# The third queue should contain the *alterating* content
# of the two queues.  The function should handle
# queues of different lengths without inserting
# 'undefined' into the new one.
# *Do not* access the array inside of any queue, only
# use the 'add', 'remove', and 'peek' functions.

# --- Example 1
#    queueOne = Queue()
#    queueOne.add(1)
#    queueOne.add(2)
#    
#    queueTwo = Queue()
#    queueTwo.add('Hi')
#    queueTwo.add('There')
#    
#    q = weave(queueOne, queueTwo)
#    print(q)

#    q.remove() # 1
#    q.remove() # 'Hi'
#    q.remove() # 2
#    q.remove() # 'There'

# --- Example 2
#    queueOne = Queue()
#    queueOne.add(1)
#    queueOne.add(2)
#    queueOne.add(3)
#    
#    queueTwo = Queue()
#    queueTwo.add('Hi')
#    queueTwo.add('There')

#    q = weave(queueOne, queueTwo)
#    print(q)

#    q.remove() # 1
#    q.remove() # 'Hi'
#    q.remove() # 2
#    q.remove() # 'There'
#    q.remove() # 3

# --- Example 3
#    queueOne = Queue()
#    queueOne.add(1)
#    queueOne.add(2)

#    queueTwo = Queue()
#    queueTwo.add('Hi')
#    queueTwo.add('There')
#    queueTwo.add('Good')
#    queueTwo.add('Morning')
#    
#    q = weave(queueOne, queueTwo)
#    print(q)

#    q.remove() # 1
#    q.remove() # 'Hi'
#    q.remove() # 2
#    q.remove() # 'There'
#    q.remove() # 'Good'
#    q.remove() # 'Morning'


class Queue:
    def __init__(self):
        self.queue = []
    def __repr__(self):
        return str(self.queue)
    def add(self, element):
        self.queue.append(element)
    def remove(self):
        first_element = self.queue[0]
        self.queue = self.queue[1:]
        return first_element
    def peek(self):
        try:
            return self.queue[0]
        except:
            return None
    def size(self):
        return len(self.queue)


def weave(queue1, queue2):
    if queue1.size() == 0:
        return queue2
    if queue2.size() == 0:
        return queue1 
    
    result = Queue()

    while queue1.peek() or queue2.peek():
        if queue1.peek():
            result.add(queue1.remove())
        if queue2.peek():
            result.add(queue2.remove())
        
    return result


q1 = Queue()
q1.add(1)
q1.add(2)
q1.add(3)
q1.add(4)

q2 = Queue()
q2.add("one")
q2.add("two")
q2.add("three")
q2.add("four")

print("First Queue: {}".format(q1))
print("Second Queue: {}".format(q2))
print("Weaved Queue: {}".format(weave(q1, q2)))


# ----------- Example 2 ----------
# queueOne = Queue()
# queueOne.add(1)
# queueOne.add(2)

# queueTwo = Queue()
# queueTwo.add('Hi')
# queueTwo.add('There')

# q = weave(queueOne, queueTwo)
# print(q)

# ----------- Example 3 ----------
# queueOne = Queue()
# queueOne.add(1)
# queueOne.add(2)
# queueOne.add(3)

# queueTwo = Queue()
# queueTwo.add('Hi')
# queueTwo.add('There')

# q = weave(queueOne, queueTwo)
# print(q)

# ----------- Example 4 ----------
# queueOne = Queue()
# queueOne.add(1)
# queueOne.add(2)

# queueTwo = Queue()
# queueTwo.add('Hi')
# queueTwo.add('There')
# queueTwo.add('Good')
# queueTwo.add('Morning')

# q = weave(queueOne, queueTwo)
# print(q)
