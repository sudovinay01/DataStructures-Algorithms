# -*- coding: utf-8 -*-
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

import numpy as np

class Search:
  """
  class contains different sorting techniques
  """
  def __init__(self, arr):
    self.__arr = arr

  def __linearSearch(self, arr, key):
    """
    Performs Linear search algorithm on a given array
    """
    for i in range(len(arr)):
      if arr[i] == key:
        return i
    return -1

  def __binarySearch(self, arr, key):
    """
    Performs Binary search algorithm on a given array
    """
    arr_center = len(arr)//2
    left = 0
    right = len(arr) - 1
    while arr_center > 0:
      if arr[arr_center] > key:
        right = arr_center
      elif arr[arr_center] < key:
        left = arr_center
      else:
        return arr_center
      arr_center = (left + right)//2
    return -1

  def search(self, key, binarySearch=False):
    if not binarySearch:
      return self.__linearSearch(self.__arr, key)
    else :
      return self.__binarySearch(self.__arr, key)

s1 = Search(np.array([1,2,3,4,5,6,7,8,9]))
s1.search(7, binarySearch=True)

