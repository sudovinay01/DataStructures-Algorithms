"""

# Searching techniques
Author : Siddhi Chaithanya

*   Linear search

    1.   Best Case : Ω(1)
    2.   Worst Case : O(n)

*   Binary search (array should be in sorted order)

    1.   Best Case : Ω(1)
    2.   List item : O(logn)
"""

from algorithms_base.algorithm import Algorithm
from algorithms_base.options_error import OptionNotFound
import numpy as np

class Search(Algorithm):
    def __init__(self, original_array):
        if isinstance(original_array, list) or isinstance(original_array, set) or isinstance(original_array, tuple) or isinstance(original_array, np.ndarray):
            self.original_array = list(original_array)
        self.verbose = False
        self.__is_sorted = False
    
    def search(self, key, kind="linear", occurences="first"):
        """
        Performs search operation for key on given array
        key : element to be searched
        kind : "linear", "binary"
        occurences : "first", "last", "all", "f", "l", "a" all are case insensitive
        first : first most occurence of an element
        last : last most occurence of an element
        all : all occurences of an element
        Note : For now this method only works for identical elements
        """
        try:
            if kind == "linear":
                return self.__linear_search(key, occurences)
            elif kind == "binary":
                self.__check_is_sorted()
                if self.__is_sorted:
                    return self.__binary_search(key, 0, len(self.original_array), occurences)
                else:
                    raise Exception(f"For binary search array should be sorted in ascending order. array = {self.original_array}")
            else:
                raise OptionNotFound(kind)
        except OptionNotFound as one:
            print(f"Option kind = {kind} doesnot exist...{one}")
        except Exception as e:
            print(f"Caught exception : {e}")
    
    def __linear_search(self, key, occurences="first"):
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
    
    def __binary_search(self, key, left, right, occurences="first", element_indices=[]):
        """
        Performs Binary search algorithm on a given array
        """
        if left <= right:
            arr_center = (left+right)//2
            if self.original_array[arr_center] > key:
                return self.__binary_search(key, left, arr_center-1, occurences)
            elif self.original_array[arr_center] < key:
                return self.__binary_search(key, arr_center+1, right, occurences)
            else:
                if str(occurences).casefold() == "all" or str(occurences).casefold() == "a":
                    element_indices.append(arr_center)
                    self.__binary_search(key, left, arr_center-1, occurences)
                    self.__binary_search(key, arr_center+1, right, occurences)
                else:
                    if len(element_indices) == 1:
                        element_indices[0] = arr_center
                    else:
                        element_indices.append(arr_center)
                    
                    if str(occurences).casefold() == "first" or str(occurences).casefold() == "f":
                        return self.__binary_search(key, left, arr_center-1, occurences)
                    if str(occurences).casefold() == "last" or str(occurences).casefold() == "l":
                        return self.__binary_search(key, arr_center+1, right, occurences)
        return element_indices
    
    def __check_is_sorted(self):
        if not self.__is_sorted:
            for i in range(len(self.original_array)-1):
                if self.original_array[i] > self.original_array[i+1]:
                    return
            self.__is_sorted = True
