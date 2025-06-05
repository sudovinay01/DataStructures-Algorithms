from linked_lists.linked_list_base import LL
from linked_lists.node import Node_V2

class DLL(LL):
    def __init__(self, type="DLL"):
        super().__init__(type)

    def _insert_head(self, data):
        """
        This function will insert at head of the linked list
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if not self._head:
            self._head = Node_V2(data, None, None)
            self._length+=1
            return
        
        node = Node_V2(data, None, None)
        (node.next, self._head.prev, self._head) = (self._head, node, node)
        self._length+=1
    
    def _insert_at_position(self, data, position):
        """
        The function inserts the data at the position specified by position
        Time Complexity : O(n) n -> Length of the Linked List
        Space Complexity : O(1)
        """
        if position > self._length+1:
            print(f"Invalid position, the maximum positions available are <= {self._length+1}")
            return

        if position == 1:
            self._insert_head(data)
            return
        
        if position == self._length+1:
            self._insert_end(data)
            return
        
        ant, temp = self._head, 1
        while temp<position-1:
            ant = ant.next
            temp+=1
        new_ant = Node_V2(data, ant, ant.next)
        (ant.next.prev, ant.next) = (new_ant, new_ant)
        self._length+=1
    
    def _insert_end(self, data):
        """
        This function inserts the data at the end of the Linked List
        Time Complexity : O(n) n -> length of the Linked List
        Space Complexity : O(1)
        """
        if not self._insert_head:
            self._insert_head(data)
            return
        
        ant = self._head
        while ant.next:
            ant = ant.next
        ant.next = Node_V2(data, ant, None)
        self._length+=1
    
    def _delete_at_head(self):
        """
        This function deletes the element at the head of the Linked List
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if not self._head:
            return None

        (deleted, self._head, self._head.prev) = (self._head.data, self._head.next, None)
        self._length-=1
        return deleted
    
    def _delete_at_end(self):
        return super()._delete_at_end()
    
    def _show_linked_list(self, symbol="<->"):
        return super()._show_linked_list(symbol)