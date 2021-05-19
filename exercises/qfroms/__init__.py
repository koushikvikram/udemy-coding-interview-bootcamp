# Queue from Stack

# --- Directions
# Implement a Queue datastructure using two stacks.
# *Do not* create an array inside of the 'Queue' class.
# Queue should implement the methods 'add', 'remove', and 'peek'.
# For a reminder on what each method does, look back
# at the Queue exercise.
# --- Examples
#     const q = new Queue();
#     q.add(1);
#     q.add(2);
#     q.peek();  # returns 1
#     q.remove(); # returns 1
#     q.remove(); # returns 2


class Stack:
    def __init__(self):
        self.stack = []
    
    def __repr__(self):
        return str(self.stack)

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        last_item = self.stack[-1]
        self.stack = self.stack[:-1]
        return last_item
    
    def peek(self):
        try:
            return self.stack[-1]
        except:
            return None


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def add(self, item):
        self.stack1.push(item)
    
    def remove(self):
        # push everything from stack1 onto stack2
        while self.stack1.peek():
            self.stack2.push(self.stack1.pop())
        
        # remove last element of stack 2
        last_element = self.stack2.pop()

        # restore stack 1
        while self.stack1.peek():
            self.stack2.push(self.stack1.pop())
        
        return last_element

    def peek(self):
        # push everything from stack1 onto stack2
        while self.stack1.peek():
            self.stack2.push(self.stack1.pop())
        
        # peek last element of stack 2
        last_element = self.stack2.peek()

        # restore stack 1
        while self.stack1.peek():
            self.stack2.push(self.stack1.pop())
        
        return last_element


q = Queue()
q.add(1)
q.add(2)
print(q.peek())  # returns 1
print(q.remove()) # returns 1
print(q.remove()) # returns 2


'''
Procedure
---------
add(1)
stack 1 - 1
stack 2 - 

add(2)
stack 1 - 1 2
stack 2 - 

add(3)
stack 1 - 1 2 3
stack 2 - 

remove()
stack 1 - 
stack 2 - 3 2 1
stack2.pop()
stack 1 - 2 3
stack 2 - 

add(4)
stack 1 - 2 3 4
stack 2 - 

add(5)
stack 1 - 2 3 4 5
stack 2 - 

remove()
stack 1 - 
stack 2 - 5 4 3 2
stack2.pop()
stack 1 - 3 4 5
stack 2 -

add(6)
stack 1 - 3 4 5 6
stack 2 - 

peek()
stack 1 - 
stack 2 - 6 5 4 3
stack2.peek()
stack 1 - 3 4 5 6
stack 2 - 
'''