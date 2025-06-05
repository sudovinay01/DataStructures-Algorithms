from linked_lists.circular_linked_list import CLL
class Q:
    def __init__(self, max_length=10):
        self.q = CLL(type="Que")
        self.max_length = max_length
    
    def enqueue(self, data):
        if self.isFull():
            print(f"{self.q._type} is full. Max allowed {self.q._type} is {self.max_length}. Current Q size is {self.q._length}")
            return
        return self.q._insert_end(data)
    
    def dequeue(self):
        if self.isEmpty():
            print(f"{self.q._type} is empty...")
            return
        return self.q._delete_at_head()
    
    def isEmpty(self):
        return not self.q._head
    
    def size(self):
        return self.q._len()
    
    def isFull(self):
        return self.q._length == self.max_length
    
    def peek(self):
        if self.isEmpty():
            print(f"{self.q._type} is empty...")
            return
        return self.q._head.data
    
    def show_queue(self):
        return self.q._show_linked_list()
