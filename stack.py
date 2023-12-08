class Stack:
    def __init__(self):
        self.some_stack = []

    def is_empty(self):
        return True if not self.some_stack else False

    def push(self, element):
        self.some_stack.append(element)

    def pop_element(self):
        return self.some_stack.pop()

    def peek(self):
        return self.some_stack[-1]

    def size(self):
        return len(self.some_stack)

    def __repr__(self):
        return ", ".join([x for x in self.some_stack]) if self.some_stack else "[]"
