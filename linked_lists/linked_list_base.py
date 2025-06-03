from linked_lists.node import Node
from abc import ABC, abstractmethod
class LL(ABC):
    def __init__(self):
        self._head = None
        self._length = 0
        self._type = "LL"
    
    @abstractmethod
    def _insert_head(self, data):
        """
        This function will insert at head of the linked list
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        print(f"Inserting data = {data} at head of the {self._type}.....")
        if not self._head:
            self._head = Node(data, None)
            self._length+=1
            return
        
        node = Node(data, None)
        (node.next, self._head) = (self._head, node)
        self._length+=1

    @abstractmethod
    def _insert_end(self, data):
        """
        This function inserts the data at the end of the Linked List
        Time Complexity : O(n) n -> length of the Linked List
        Space Complexity : O(1)
        """
        print(f"Inserting data = {data} at the end of the {self._type}.....")
        if not self._head:
            self._insert_head(data)
            return
        
        temp = self._head
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None)
        self._length+=1
    
    @abstractmethod
    def _insert_at_position(self, data, position):
        """
        The function inserts the data at the position specified by position
        Time Complexity : O(n) n -> Length of the Linked List
        Space Complexity : O(1)
        """
        print(f"Inserting data = {data} at position : {position} of the {self._type}.....")
        if position > self._length+1:
            print(f"Invalid position, the maximum positions available are <= {self._length+1}")
            return
        
        if position == 1:
            self.insert_head(data)
            return
        
        if position == self._length+1:
            self._insert_end(data)
            return

        temp, ant = 1, self._head
        while temp<position-1:
            ant = ant.next
            temp += 1
        
        new_ant = Node(data, None)
        (new_ant.next, ant.next) = (ant.next, new_ant)
        self._length+=1

    @abstractmethod
    def _show_linked_list(self):
        """
        This function displays the current Linked List
        Time Complexity : O(n) n -> represents the length of the Linked List
        """
        print(f"Current {self._type}: ")
        temp = self._head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print(f"{temp}")

    def _len(self):
        """
        The function returns the length of the Linked List
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        return self._length