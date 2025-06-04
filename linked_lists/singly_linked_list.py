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
    def __init__(self, type="SLL", verbose=False):
        super().__init__(type, verbose=verbose)
    
    def _insert_head(self, data):
        super()._insert_head(data)

    def _insert_end(self, data):
        super()._insert_end(data)

    def _insert_at_position(self, data, position):
        super()._insert_at_position(data, position)

    def _delete_at_end(self):
        return super()._delete_at_end()
    
    def _delete_at_head(self):
        return super()._delete_at_head()
    
    def _show_linked_list(self):
        return super()._show_linked_list()