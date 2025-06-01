import numpy as np
from typing import List

class Heap:
    """
    A class representing a max heap data structure.
    This class provides methods to build a max heap, insert elements,
    check if an array is a max heap, and display the current heap.
    Attributes:
        heap (np.ndarray): The array representing the heap.
        isHeap (bool): A flag indicating whether the heap is built.
    Methods:
        __max_heapify(parent): Puts the element at the specified parent index in its correct position in the max heap.
        __build_max_heap(): Builds the max heap from the initial array.
        heap_insert(data): Inserts a new element or list of elements into the heap.
        __check_max_heap(to_check): Checks if a given array is a max heap.
        is_heap(h=None): Checks if the current heap or a specified array is a max heap.
        show_heap(): Displays the current state of the heap.
    """
    
    def __init__(self, heap: List[int|float]):
        self.heap = np.array(heap)
        self.isHeap = False
        self.__build_max_heap()
    
    def __max_heapify(self, parent):
        """
        This max heapify function puts element specified by parent at its right place.
        Time Complexity : O(log n) -> Depth of the heap is log n.
        Space Complexity : O(1) -> No extra space is used.
        """
        left_child = 2*parent + 1
        right_child = 2*parent + 2
        largest = parent
        
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[parent]:
            largest = left_child
        
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        
        if largest != parent:
            (self.heap[parent], self.heap[largest]) = (self.heap[largest], self.heap[parent])
            self.__max_heapify(largest)
    
    def __build_max_heap(self):
        """
        Build max heap.
        Time Complexity : O(n) -> Each element will be visited only once
        Space Complexity : O(1) -> No extra space is used.
        """
        if not self.isHeap:
            for p in range(len(self.heap)//2-1, 0, -1):
                self.__max_heapify(p)
            self.isHeap = True
    
    def heap_insert(self, data:int|float|List[int|float]):
        """
        Inserts a new element or list of new elements into the heap.
        Time Complexity : O(log n) if data is a single element -> Insertion will take log n time as it will require to traverse the height of the heap.
        Time Complexity : O(n) if data is a list -> Insertion will take linear time as it will require to build the heap.
        Space Complexity : O(1) -> No extra space is used
        """
        # Keeping the backup of original heap before insertion to roll back at later if insertion fails in middle of insertion operation
        heap_backup = self.heap.copy()
        try:
            if isinstance(data, list):
                self.heap = np.concatenate((self.heap, np.array(data)))
                self.isHeap = False
                self.__build_max_heap()
            else:
                self.heap = np.insert(self.heap, self.heap.size, data)
                i = self.heap.size-1
                while i>0 and self.heap[i] > self.heap[i//2-1]:
                    (self.heap[i], self.heap[i//2-1]) = (self.heap[i//2-1], self.heap[i])
                    i//=2
            print(f"Insert successfull call show_heap() to view the heap...")
        except Exception as e:
            print("Exception caused in heap insertion, insertion failed.....")
            self.heap = heap_backup
    
    def __check_max_heap(self, to_check):
        """
        Checks if given array to_check is max heap or not
        Time Complexity : O(n) -> Atleast half of the elements will be checked to confirm if it is a max heap or not.
        Space Complexity : O(1) -> No extra space is used.
        """
        try:
            for p in range(len(to_check)//2-1, 0, -1):
                if not (to_check[p] >= to_check[2*p+1] and to_check[p] >= to_check[2*p+2]):
                    return False
            return True
        except Exception as e:
            print(e.__cause__())

    def is_heap(self, h:List[int|float]=None):
        """
        This function checks if the given array is heap or not
        If nothing is specified as part of h, it checks if the
        list provided at the begining of Heap object creation
        is heap or not.
        """
        if h:
            return self.__check_max_heap(np.array(h))
        return self.__check_max_heap(self.heap)
    
    def show_heap(self):
        """
        Displays the current heap.
        """
        print(f"Current heap: {self.heap}")


