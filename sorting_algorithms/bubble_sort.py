# -*- coding: utf-8 -*-
"""

# Bubble Sort
*   Run Time Complexity : O(n^2)
*   Space Complexity : O(1) ---> Only additional space taken by algorithm needs to be considered ignoring input given to the algorithm
"""

import numpy as np

class BubbleSort:
  """
      Class contains different problems on Bubble sort algorithm.
      Author: Siddhi Chaithanya
  """
  def __init__(self, original_array):
    """
    Args:
      original_array: List or array to be sorted
      sorted_array: Array after sorted
      sorted: Boolean to show if array is sorted or not
    """
    self.__original_array = self.__sorted_array = original_array
    self.__sorted = False
    self.__verbose = False

  def apply_bubble_sort(self, verbose=False):
    """
    Args:
      verbose: Boolean to decide if verbose output is required. Default value is False.
    Returns:
      None
    """
    # check if array is already sorted
    if self.__sorted :
      print("Array is already sorted.......")
      return

    self.__verbose = verbose

    # Apply bubble sort algorithm and set sorted = True
    self.__bubble_sort(self.__sorted_array, 0, len(self.__original_array))
    self.__sorted = True

  def __bubble_sort(self, A, L, R):
    """
    Performs bubble sort on given array.
    Args:
      A : Array on which bubble sort to be performed
      L : Arrays left index
      R : Arrays right index
    """
    verbose_output = str("======================================================\nArray to be sorted : {}".format(A))

    for i in range(L, R-1):
      for j in range(L, R-1):
        if A[j] > A[j+1]:
          (A[j], A[j+1]) = (A[j+1], A[j])
      verbose_output = "\n".join([verbose_output, str("After {}th iteration \nIntermediate array : {}".format(i,A))])

    self.__sorted = True

    if self.__verbose:
      print(verbose_output,"\n======================================================")

  def setOriginalArray(self, original_array):
    """
    Replaces original array with new array
    Args:
      original_array: List or array to be sorted
    """
    self.__original_array = original_array
    self.__sorted_array = original_array
    self.__sorted = False

  def displaySortedArray(self):
    """
    Displays sorted array
    """
    if not self.__sorted :
      print("Array is not sorted yet. Please call apply_bubble_sort() function.......")
      return
    print("Sorted array : ",self.__sorted_array)

b1 = BubbleSort([5,4,3,2,1])
b1.apply_bubble_sort(verbose=True)
b1.displaySortedArray()

b1.setOriginalArray([1, 2, 3, 4, 5])
b1.apply_bubble_sort(verbose=True)
b1.displaySortedArray()

