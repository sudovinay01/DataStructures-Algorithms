"""

# Searching techniques
Author : Siddhi Chaithanya

*   Linear search

    1.   Best Case : Ω(1)
    2.   Worst Case : O(n)

*   Binary search (if array is already sorted)

    1.   Best Case : Ω(1)
    2.   List item : O(logn)
"""

from algorithms_base.algorithm import Algorithm
from algorithms_base.options_error import OptionNotFound
import numpy as np

class Search(Algorithm):
    def __init__(self, original_array):
        self.original_array = list(original_array)
        self.verbose = False
        self.is_sorted = False
    
    def search(self, key, kind="linear", occurences="first"):
        try:
            if kind == "linear":
                return self.__linearSearch(key, occurences)
            elif kind == "binary":
                return self.__binarySearch(key, 0, len(self.original_array), occurences)
            else:
                raise OptionNotFound(kind)
        except OptionNotFound as e:
            print(f"Option kind = {kind} doesnot exist...")
    
    def __linearSearch(self, key, occurences="first"):
        """
        Performs Linear search algorithm on a given array
        """
        element_indices = []
        try:
            if str(occurences).casefold()=="first" or str(occurences).casefold()=="f":
                for i in range(len(self.original_array)):
                    if self.original_array[i] == key:
                        element_indices.append(i)
                        break
            elif str(occurences).casefold()=="last" or str(occurences).casefold()=="l":
                for i in range(-1, 0-len(self.original_array)-1, -1):
                    if self.original_array[i] == key:
                        element_indices.append(i+len(self.original_array))
                        break
            elif str(occurences).casefold()=="all" or str(occurences).casefold()=="a":
                for i in range(len(self.original_array)):
                    if self.original_array[i] == key:
                        element_indices.append(i)
            else:
                msg = "option occurences = {} doesnot exist".format(occurences)
                raise OptionNotFound(msg)
            return element_indices
        except OptionNotFound as e:
            print(f"Exception caught : {e}")
    
    def __binarySearch(self, key, left, right, occurences="first"):
        """
        Performs Binary search algorithm on a given array
        """
        element_indices = []
        arr_center = (left+right-1)//2
        while left < right:
            if self.original_array[arr_center] > key:
                right = arr_center-1
            elif self.original_array[arr_center] < key:
                left = arr_center+1
            else:
                if str(occurences).casefold() == "all" or str(occurences).casefold() == "a":
                    element_indices.append(arr_center)
                    element_indices = element_indices + self.__binarySearch(key, left, arr_center-1, occurences) + self.__binarySearch(key, arr_center+1, right, occurences)
                elif str(occurences).casefold() == "first" or str(occurences).casefold() == "f":
                    if len(element_indices) == 1:
                        element_indices[0] = arr_center
                    else:
                        element_indices.append(arr_center)
                    right = arr_center-1
                elif str(occurences).casefold() == "last" or str(occurences).casefold() == "l":
                    if len(element_indices) == 1:
                        element_indices[0] = arr_center
                    else:
                        element_indices.append(arr_center)
                    left = arr_center+1
            arr_center = (left + right)//2
        return element_indices