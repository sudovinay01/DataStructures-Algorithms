# -*- coding: utf-8 -*-
"""

# Selection sort


*   Run Time Complexity : O(n^2)
*   Space Complexity : O(1) ---> Only additional space taken by algorithm needs to be considered ignoring input given to the algorithm
"""

import numpy as np

class SelectionSort:
  """
      Class contains different problems on Selection sort algorithm.
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

  def apply_selection_sort(self, verbose=False):
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

    # Apply selection sort algorithm and set sorted = True
    self.__selection_sort(self.__sorted_array, 0, len(self.__original_array))
    self.__sorted = True

  def __selection_sort(self, A, L, R):
    """
    Performs selection sort on given array.
    Args:
      A : Array on which selection sort to be performed
      L : Arrays left index
      R : Arrays right index
    """
    verbose_output = str("======================================================\nArray to be sorted : {}".format(A))

    for i in range(L, R):
      min_index = np.argmin(A[i:R])
      (A[min_index+i], A[i]) = (A[i], A[min_index+i])
      verbose_output = "\n".join([verbose_output, str("After first iteration \n Intermediate array : {}".format(A))])

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
      print("Array is not sorted yet. Please call apply_selection_sort() function.......")
      return
    print("Sorted array : ",self.__sorted_array)

A = [5, 4, 4, 10, 9, 5, 6, 3, 2, 1]
s1 = SelectionSort(A)
s1.apply_selection_sort(verbose=True)
s1.displaySortedArray()

s1.apply_selection_sort(verbose=True)

s1.setOriginalArray([10, 12, 8, 1, 0, -20])
s1.apply_selection_sort(verbose=True)
s1.displaySortedArray()

