import numpy as np

class Heap:
    def __init__(self, heap):
        self.heap = np.array(heap)
        print(f"Building heap from the given array: {self.heap}")
        self.isHeap = False
        self.__build_max_heap()
    
    def __max_heapify(self, parent):
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
        if not self.isHeap:
            for p in range(len(self.heap)//2-1, 0, -1):
                self.__max_heapify(p)
            self.isHeap = True
    
    def heap_insert(self, data):
        self.heap = np.insert(self.heap, self.heap.size, data)
        self.isHeap = False
        i = self.heap.size-1
        while i>0 and self.heap[i] > self.heap[i//2-1]:
            (self.heap[i], self.heap[i//2-1]) = (self.heap[i//2-1], self.heap[i])
            i//=2
        self.isHeap = True
        print(f"Insert successfull call show_heap()")
    
    def show_heap(self):
        print(f"Current heap: {self.heap}")


