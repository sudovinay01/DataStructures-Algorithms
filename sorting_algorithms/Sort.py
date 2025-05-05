# -*- coding: utf-8 -*-
"""

# Insertion Sort
*   Run Time Complexity :
    1.   Worst case : O(n^2)
    2.   Best case : Ω(n)
*   Space Complexity : O(1) ---> Only additional space taken by algorithm needs to be considered ignoring input given to the algorithm
"""

from algorithms_base.algorithm import Algorithm
from algorithms_base.options_error import OptionNotFound
import numpy as np

class Sort(Algorithm):
  """
      Class contains different problems on Insertion sort algorithm.
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
    print("This only works for numerical values. So, make sure to provide numerical array.....")

  def apply(self, kind="quick_random", verbose=False):
    """
    Sorts the array in ascending order 
    kind : quick_random, q_r, merge, m, selection, s, insertion, i, bubble, b
    verbose : True, False
    Default : apply("quick_random", False)
    """
    try:
        if str(kind).casefold() == "quick_random" or str(kind).casefold() == "q_r":
            self.apply_quick_sort(randomPivot=True, verbose=verbose)
        elif str(kind).casefold() == "quick" or str(kind).casefold() == "q":
            self.apply_quick_sort(verbose=verbose)
        elif str(kind).casefold() == "merge" or str(kind).casefold() == "m":
            self.apply_merge_sort(verbose=verbose)
        elif str(kind).casefold() == "selection" or str(kind).casefold() == "s":
            self.apply_selection_sort(verbose=verbose)
        elif str(kind).casefold() == "insertion" or str(kind).casefold() == "i":
            self.apply_insertion_sort(verbose=verbose)
        elif str(kind).casefold() == "bubble" or str(kind).casefold() == "b":
            self.apply_bubble_sort(verbose=verbose)
        else:
            raise OptionNotFound(kind)
        print("Array is now sorted...\nCall displaySortedArray() to view the sorted array \nTo sort another array set using setOriginalArray()")
    except OptionNotFound as one:
      print(f"Option kind = {kind} doesnot exist...{one}")
    except Exception as e:
        print(f"Caught exception : {e}")

  def apply_insertion_sort(self, verbose=False):
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

    # Apply insertion sort algorithm and set sorted = True
    self.__insertion_sort(self.__sorted_array, 0, len(self.__original_array))
    self.__sorted = True

  def __insertion_sort(self, A, L, R):
    """
    Performs insertion sort on given array.
    Args:
      A : Array on which insertion sort to be performed
      L : Arrays left index
      R : Arrays right index
    """
    verbose_output = str("======================================================\nArray to be sorted : {}".format(A))

    for i in range(L+1, R):
      compare_point = A[i]
      j = i-1
      while j >= 0 and A[j] > compare_point:
        A[j+1] = A[j]
        j -= 1
      A[j+1] = compare_point
      verbose_output = "\n".join([verbose_output, str("After {}th iteration \nIntermediate array : {}".format(i-1,A))])
    self.__sorted = True

    if self.__verbose:
      print(verbose_output,"\n======================================================")

  def apply_quick_sort(self, randomPivot=False, verbose=False):
    """
    Args:
      randomPivot: Boolean to decide if pivot element should be selected. Default value is False.
      verbose: Boolean to decide if verbose output is required. Default value is False.
    Returns:
      None
    """
    # check if array is already sorted
    if self.__sorted :
      print("Array is already sorted.......")
      return

    self.__verbose = verbose

    # Apply quick sort algorithm and set sorted = True
    self.__quick_sort(self.__sorted_array, 0, len(self.__original_array)-1, randomPivot)
    self.__sorted = True

  def __quick_sort(self, A, L, R, random_pivot):
    """
    Performs quick sort on given array.
    Args:
      A : Array on which quick sort to be performed
      L : Arrays left index
      R : Arrays right index
      random_pivot : booean value to decide picking of pivot element
    """
    if L < R :
      pivot_index = self.__pivot_placement(A, L, R, random_pivot)
      self.__quick_sort(A, L, pivot_index - 1, random_pivot)
      self.__quick_sort(A, pivot_index + 1, R, random_pivot)

    self.__sorted = True

  def __pivot_placement(self, A, L, R, random_pivot):
    """
      Choose pivot and find its right place in the array.
      Pivot can be choosen as the element at last index or randomly.
      Args:
        A : Array on which pivot placement to be found
        L : Arrays left index
        R : Arrays right index
        random_pivot : booean value to decide picking of pivot element
    """
    verbose_output = str("======================================================\nArray : {}, Left Index : {}, Right Index : {}".format(A[L:R+1], L, R))

    if random_pivot:
      rand_index = np.random.randint(L, R)
      verbose_output = "\n".join([verbose_output, str("Random pivot index : {}".format(rand_index)), str("Random pivot element : {}".format(A[rand_index]))])
      (A[R], A[rand_index]) = (A[rand_index], A[R])
    else:
      verbose_output = "\n".join([verbose_output, str("Pivot index : {}\nPivot element : {}".format(R, A[R]))])
    
    pivot_element = A[R]
    left_movement = L-1
    right_movement = L

    while right_movement < R:
      if A[right_movement] <= pivot_element:
        left_movement += 1
        (A[left_movement], A[right_movement]) = (A[right_movement], A[left_movement])
      right_movement += 1

    (A[left_movement+1], A[R]) = (A[R], A[left_movement+1])

    verbose_output = "\n".join([verbose_output, str("Correct pivot index : {}".format(left_movement+1)), str("Left partition : {}".format(A[L:left_movement+1])), str("Right partition : {}".format(A[left_movement+2:R+1]))])
    if self.__verbose:
      print(verbose_output,"\n======================================================")

    return left_movement + 1
  
  def apply_merge_sort(self, verbose=False):
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

    # Apply merge sort algorithm and set sorted = True
    self.__merge_sort(self.__sorted_array, 0, len(self.__original_array)-1)
    self.__sorted = True

  def __merge_sort(self, A, L, R):
    """
    Performs merge sort on given array.
    Args:
      A : Array on which merge sort to be performed
      L : Arrays left index
      R : Arrays right index
    """
    division_point = (L+R-1)//2
    if L < R :
      self.__merge_sort(A, L, division_point)
      self.__merge_sort(A, division_point+1, R)
      self.__merge(A, L, division_point, R)

  def __merge(self, A, L, division_point, R):
    """
      Merge two individual arrays into 1 sorted array
      Args:
        A : Array on which merge to be performed
        L : Arrays left index
        division_point : Arrays division point
        R : Arrays right index
    """
    verbose_output = str("======================================================\nArray : {}, Left Index : {}, Right Index : {}".format(A[L:R+1], L, R))

    A_temp = list()
    first_index = L
    second_index = division_point + 1
    while first_index <=division_point and second_index <= R :
      if A[first_index] < A[second_index] :
        A_temp.append(A[first_index])
        first_index += 1
      else :
        A_temp.append(A[second_index])
        second_index += 1

    if first_index <= division_point :
      for i in range(first_index, division_point+1) :
        A_temp.append(A[i])
    if second_index <= R :
      for i in range(second_index, R+1) :
        A_temp.append(A[i])

    for i in range(L, R+1) :
      A[i] = A_temp[i-L]

    verbose_output = "\n".join([verbose_output, str("Merged array : {}\nTemp array : {}".format(A, A_temp))])
    if self.__verbose:
      print(verbose_output,"\n======================================================")
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
      verbose_output = "\n".join([verbose_output, str("After {}th iteration \nIntermediate array : {}".format(i, A))])

    self.__sorted = True

    if self.__verbose:
      print(verbose_output,"\n======================================================")

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
      print("Array is not sorted yet. Please call apply_insertion_sort() function.......")
      return
    print("Sorted array : ",self.__sorted_array)

