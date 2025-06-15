from linked_lists.linked_list_base import LL
class SLL(LL):
    """
    This class contains the classical implementation of the Single Linked List which includes
    1. insert_head : Insert at the head of the Single Linked List
    2. insert_end : Insert at the end of the Single Linked List
    3. insert_at_position : Insert at the position specified by the user
    4. show_linked_list : Shows the current status of the Single Linked List
    5. len : Gets the length of Single Linked List
    """
    def __init__(self, type="SLL"):
        super().__init__(type)
    
    def insert_head(self, data):
        super().insert_head(data)

    def insert_end(self, data):
        super().insert_end(data)

    def insert_at_position(self, data, position):
        super().insert_at_position(data, position)

    def delete_at_end(self):
        return super().delete_at_end()
    
    def delete_at_head(self):
        return super().delete_at_head()
    
    def reverse(self):
        if not self._head or not self._head.next:
            return
        
        prev_ant, front_ant = None, self._head
        while front_ant:
            (front_ant, self._head.next, prev_ant) = (front_ant.next, prev_ant, self._head)
            self._head = front_ant
        self._head = prev_ant

    def show_linked_list(self, symbol="->"):
        return super().show_linked_list(symbol)