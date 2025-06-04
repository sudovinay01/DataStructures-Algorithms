from linked_lists.singly_linked_list import SLL
class Stack:
    def __init__(self, verbose=False):
        self.stack = SLL(type="Stack", verbose=verbose)
    
    def push(self, data):
        return self.stack._insert_head(data)

    def pop(self):
        return self.stack._delete_at_head()
    
    def show_stack(self):
        return self.stack._show_linked_list()       