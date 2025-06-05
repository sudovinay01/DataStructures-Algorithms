from linked_lists.singly_linked_list import SLL
class Stack:
    def __init__(self, max_length=10):
        self.stack = SLL(type="Stack")
        self.max_length = max_length
    
    def push(self, data):
        if self.isFull():
            print(f"{self.stack._type} overflow. Max allowed stack size is {self.max_length}")
            return
        return self.stack._insert_head(data)

    def pop(self):
        if self.isEmpty():
            print(f"{self.stack._type} underflow.")
            return
        return self.stack._delete_at_head()
    
    def isEmpty(self):
        return not self.stack._head
    
    def isFull(self):
        return self.stack._length == self.max_length
    
    def peek(self):
        if self.isEmpty():
            print(f"{self.stack._type} underflow.")
            return
        return self.stack._head.data
    
    def size(self):
        return self.stack._len()
    
    def show_stack(self):
        return self.stack._show_linked_list()       