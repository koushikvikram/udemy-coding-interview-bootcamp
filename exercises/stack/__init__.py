# Stack
# --- Directions
# Create a stack data structure.  The stack
# should be a class with methods 'push', 'pop', and
# 'peek'.  Adding an element to the stack should
# store it until it is removed.
# --- Examples
#   const s = new Stack();
#   s.push(1);
#   s.push(2);
#   s.pop(); # returns 2
#   s.pop(); # returns 1


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


# s = Stack()
# s.push(1)
# print("Stack: {}".format(s))
# s.push(2)
# print("Stack: {}".format(s))
# element = s.pop()
# print("Element: {}, Stack: {}".format(element, s))
# element = s.pop()
# print("Element: {}, Stack: {}".format(element, s))
