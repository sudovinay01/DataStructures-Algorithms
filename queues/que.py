from linked_lists.circular_linked_list import CLL
class Q:
    def __init__(self, verbose=False):
        self.q = CLL(type="Que", verbose=verbose)
    
    def enqueue(self, data):
        return self.q._insert_end(data)
    
    def dequeue(self):
        return self.q._delete_at_head()
    
    def show_queue(self):
        return self.q._show_linked_list()
