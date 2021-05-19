# --- Description
# Create a queue data structure.  The queue
# should be a class with methods 'add' and 'remove'.
# Adding to the queue should store an element until
# it is removed
# --- Examples
#     const q = new Queue();
#     q.add(1);
#     q.remove(); # returns 1;

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
        return self.queue[0]
    def size(self):
        return len(self.queue)    


q = Queue()
q.add(4)
q.add(6)
q.add(8)
print(q)

element = q.remove()
print("Removed element: {}".format(element))
print("Updated queue: {}".format(q))
print("Size of updated queue: {}".format(q.size()))
print("First element: {}".format(q.peek()))