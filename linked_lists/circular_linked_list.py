from linked_lists.node import Node_V1
from linked_lists.linked_list_base import LL
class CLL(LL):

    def __init__(self, type="CLL", verbose=False):
        super().__init__(type, verbose=verbose)
        self._tail = None
    
    def _insert_head(self, data):
        """
        This function will insert at head of the circular linked list
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if self._verbose:
            print(f"Inserting data = {data} at head of the {self._type}.....")
        
        if not self._head:
            self._head = Node_V1(data, None)
            (self._head.next, self._tail) = (self._head, self._head)
            self._length+=1
            return
        
        node = Node_V1(data, None)
        (node.next, self._head) = (self._head, node)
        self._length+=1
    
    def _insert_at_position(self, data, position):
        """
        The function inserts the data at the position specified by position
        Time Complexity : O(n) n -> Length of the Linked List
        Space Complexity : O(1)
        """
        if self._verbose:
            print(f"Inserting data = {data} at position : {position} of the {self._type}.....")
        
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
        
        new_ant = Node_V1(data, None)
        (new_ant.next, ant.next) = (ant.next, new_ant)
        self._length+=1
    
    def _insert_end(self, data):
        """
        This function inserts the data at the end of the Linked List
        Time Complexity : O(1) -> because we have a pointer which points at the end of the CLL
        Space Complexity : O(1)
        """
        if self._verbose:
            print(f"Inserting data = {data} at the end of the {self._type}.....")
        
        if not self._head:
            self._insert_head(data)
            return
        
        node = Node_V1(data, self._head)
        (self._tail.next, self._tail) = (node, node)
        self._length+=1
    
    def _delete_at_head(self):
        """
        This function deletes the element at the head of the Linked List
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if not self._head:
            if self._verbose:
                print(f"{self._type} has no elements. Deletion not possible...")
            return None

        if self._head == self._tail:
            (deleted, self._head, self._tail) = (self._head.data, None, None)
            self._length-=1
            return deleted
        
        (deleted, self._head, self._tail.next) = (self._head.data, self._head.next, self._head)
        self._length-=1
        return deleted
    
    def _delete_at_end(self):
        """
        This function deletes the element at the end of the Linked List
        Time Complexity : O(n) n -> length of the Linked List
        Space Complexity : O(1)
        """
        if not self._head:
            if self._verbose:
                print(f"{self._type} has no elements. Deletion not possible...")
            return None

        if self._head == self._tail:
            (deleted, self._head, self._tail) = (self._head.data, None, None)
            self._length-=1
            return deleted
        
        ant = self._head
        while ant.next != self._tail:
            ant = ant.next
        (deleted, ant.next, self._tail) = (self._tail.data, self._head, ant)
        self._length-=1
        return deleted
    
    def _show_linked_list(self):
        """
        This function displays the current Linked List
        Time Complexity : O(n) n -> represents the length of the Linked List
        """
        print(f"Current {self._type}: ")
        temp = self._head
        while temp != self._tail:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print(f"{self._tail.data}")
