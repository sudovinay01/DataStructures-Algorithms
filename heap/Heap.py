import numpy as np

class Heap:
    def __init__(self, heap):
        self.heap = np.array(heap)
        self.isHeap = False
        self.__build_max_heap()
    
    def __max_heapify(self, parent):
        """
        This max heapify function puts element specified by parent at its right place.
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
        """
        if not self.isHeap:
            for p in range(len(self.heap)//2-1, 0, -1):
                self.__max_heapify(p)
            self.isHeap = True
    
    def heap_insert(self, data:int):
        # Keeping the backup of original heap before insertion to roll back at later if insertion fails in middle of insertion operation
        heap_backup = self.heap.copy()
        try:
            self.heap = np.insert(self.heap, self.heap.size, data)
            i = self.heap.size-1
            while i>0 and self.heap[i] > self.heap[i//2-1]:
                (self.heap[i], self.heap[i//2-1]) = (self.heap[i//2-1], self.heap[i])
                i//=2
            print(f"Insert successfull call show_heap() to view the heap...")
        except Exception as e:
            print("Exception caused in heap insertion, insertion failed.....")
            self.isHeap = self.check_max_heap()
            self.heap = heap_backup
    
    def __check_max_heap(self):
        """
        Checks if given array is max heap
        """
        try:
            for p in range(len(self.heap)//2-1, 0, -1):
                if not (self.heap[p] >= self.heap[2*p+1] and self.heap[p] >= self.heap[2*p+2]):
                    return False
            return True
        except Exception as e:
            print(e.__cause__())

    def show_heap(self):
        print(f"Current heap: {self.heap}")


