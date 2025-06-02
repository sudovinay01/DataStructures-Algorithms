from linked_lists.node import Node
class SLL:
    """
    This class contains the classical implementation of the Single Linked List which includes
    1. insert_head : Insert at the head of the Single Linked List
    2. insert_end : Insert at the end of the Single Linked List
    3. insert_at_position : Insert at the position specified by the user
    4. show_linked_list : Shows the current status of the Single Linked List
    5. len : Gets the length of Single Linked List
    """
    def __init__(self):
        self._head = None
        self._length = 0
        self._type = "SLL"
    
    def _insert_head(self, data):
        """
        This function will insert at head of the linked list
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        print(f"Inserting at head of the {self._type}.....")
        if not self._head:
            self._head = Node(data, None)
            return
        
        node = Node(data, None)
        (node.next, self._head) = (self._head, node)
        self._length+=1

    def insert_end(self, data):
        """
        This function inserts the data at the end of the Linked List
        Time Complexity : O(n) n -> length of the Linked List
        Space Complexity : O(1)
        """
        print(f"Inserting at the end of the {self._type}.....")
        if not self._head:
            self._head = Node(data, None)
        
        temp = self._head
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None)
        self._length+=1
    
    def insert_at_position(self, data, position):
        """
        The function inserts the data at the position specified by position
        Time Complexity : O(n) n -> Length of the Linked List
        Space Complexity : O(1)
        """
        if position == 1:
            self.insert_head(data)
            self._length+=1
            return
        
        print(f"Inserting at position : {position} of the {self._type}.....")
        temp, ant = 1, self._head
        while temp<position-1 and ant:
            ant = ant.next
            temp += 1
        
        if not ant:
            print(f"Invalid position, the maximum positions available are <= {temp}")
            return
        new_ant = Node(data, None)
        (new_ant.next, ant.next) = (ant.next, new_ant)
        self._length+=1

    def show_linked_list(self):
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

    def len(self):
        """
        The function returns the length of the Linked List
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        return self._length