from linked_lists.linked_list_base import LL
from nodes.node import Node_V2

class DLL(LL):
    def __init__(self, type="DLL"):
        super().__init__(type)

    def insert_head(self, data):
        """
        This function will insert at head of the linked list
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if not self._head:
            self._head = Node_V2(data)
            self._length+=1
            return
        
        node = Node_V2(data)
        (node.next, self._head.prev, self._head) = (self._head, node, node)
        self._length+=1
    
    def insert_at_position(self, data, position):
        """
        The function inserts the data at the position specified by position
        Time Complexity : O(n) n -> Length of the Linked List
        Space Complexity : O(1)
        """
        if position > self._length+1:
            print(f"Invalid position, the maximum positions available are <= {self._length+1}")
            return

        if position == 1:
            self.insert_head(data)
            return
        
        if position == self._length+1:
            self.insert_end(data)
            return
        
        ant, temp = self._head, 1
        while temp<position-1:
            ant = ant.next
            temp+=1
        new_ant = Node_V2(data, ant, ant.next)
        (ant.next.prev, ant.next) = (new_ant, new_ant)
        self._length+=1
    
    def insert_end(self, data):
        """
        This function inserts the data at the end of the Linked List
        Time Complexity : O(n) n -> length of the Linked List
        Space Complexity : O(1)
        """
        if not self._head:
            self.insert_head(data)
            return
        
        ant = self._head
        while ant.next:
            ant = ant.next
        ant.next = Node_V2(data, ant)
        self._length+=1
    
    def delete_at_head(self):
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
    
    def delete_at_end(self):
        return super().delete_at_end()
    
    def reverse(self):
        if not self._head or not self._head.next:
            return
        
        front_ant = self._head.next
        while front_ant:
            (self._head.next, self._head.prev) = (self._head.prev, self._head.next)
            self._head = front_ant
            front_ant = front_ant.next
        (self._head.next, self._head.prev) = (self._head.prev, self._head.next)

    def show_linked_list(self, symbol="<->"):
        return super().show_linked_list(symbol)