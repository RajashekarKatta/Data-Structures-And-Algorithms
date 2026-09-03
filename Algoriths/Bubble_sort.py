# Types of Sorting Techniques
"""There are various sorting algorithms are used in data structures. The following two types of sorting algorithms can be broadly classified.
1. Comparison-based sorting algorithms.
    a. Bubble Sort
    b. Insertion Sort
    c. Selection Sort
    d. Quick Sort
    e. Merge Sort
    f. Heap Sort

2. Non-comparison-based sorting algorithms.
    a. Counting Sort
    b. Bucket Sort
    c. Radix Sort
    
"""

# Bubble Sort Algorithm -> O(n^2) Time and O(1) Space:
"""Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 
This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high."""

# Bubble Sort Algorithm Implementation in Python
class Solution:
    def bubble_sort(self, arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            for j in range(0, n-i-1): # Last i elements are already in place
                if arr[j] > arr[j +1]:
                    arr[j], arr[j+1] = arr[j +1], arr[j] # Swap if the element found is greater than the next element
        return arr
s = Solution()
arr = [64, 34, 25, 12, 22, 11, 90]
print(s.bubble_sort(arr)) # Output: [11, 12, 22, 25, 34, 64, 90]




# Optimized Bubble Sort Algorithm -> O(n) Time and O(1) Space:  Bubble Sort in-place sorting algorithm.
"""The optimized version of bubble sort checks if any swapping occurs in the inner loop. If no swapping occurs, it means the array is already sorted, and we can break out of the loop early."""
class Solution:
    def optimized_bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j +1]:
                    arr[j] , arr[j+1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
s = Solution()
arr = [42, 12, 58, 71, 34, 49, 82]
print(s.optimized_bubble_sort(arr)) # Output: [12, 34, 42, 49, 58, 71, 82]



# Interview Answer for Bubble Sort Alogorithm:
"""Bubble Sort is a comparison-based sorting algorithm. It repeatedly compares adjacent elements and swaps them if they are in the wrong order. 
After each pass, the largest unsorted element moves to its correct position at the end of the array."""


# Ascending Order bubble Sort algorithm implementation in Python
class Solution:
    def bubble_sort_ascending(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
s = Solution()
arr = [5, 3, 8, 4, 2]
print(s.bubble_sort_ascending(arr))  # Output: [2, 3, 4, 5, 8]



# Descending Order bubble Sort algorithm implementation in Python
class Solution:
    def bubble_sort_descending(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
s = Solution()
arr = [5, 3, 4, 8, 2]    # Bubble sort Descending Order
print(s.bubble_sort_descending(arr))



# Count Passes bubble Sort algorithm implementation in Python
class Solution:
    def count_passes(self, arr):
        count = 0
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            count += 1
            if not swapped:
                break
        return f"Count passes are {count}"
s = Solution()
arr = [5, 4, 3, 2, 1]
print(s.count_passes(arr))      # Output 5




# count comparisons using bubble sort algorithm 
class Solution:
    def bubble_sort_count_comparision(self, arr):
        n = len(arr)
        comparisions = 0
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                comparisions += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[i]
                    swapped = True
            if not swapped:
                break
        return f"Comparision count is {comparisions}"
s = Solution()
arr = [1, 2, 3, 4, 5]
print(s.bubble_sort_count_comparision(arr))



# Question count swappss using bubble sort algorithm
class Solution:
    def count_swapps(self, arr):
        n = len(arr)
        swap = 0
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    swap += 1
            if not swapped:
                break
        return swap
s = Solution()
arr = [5, 4, 3, 2, 1]
print(s.count_swapps(arr))



# Is arrary sorted
class Solution:
    def bubble_sort_is_sorted(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                return True
        return False

s = Solution()
arr = [1, 2, 3, 4, 5]
print(s.bubble_sort_is_sorted(arr))



# Finding The largest element by using Bubble sort
class Solution:
    def largest_element(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1], arr[j]
        return f"First largest element {arr[-1]}"

s = Solution()
arr = [1, 2, 5, 4, 3]
print(s.largest_element(arr))




# Find Second Largest element
class Solution:
    def largest_element(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1], arr[j]
        return f"Second largest element {arr[-2]}"

s = Solution()
arr = [1, 2, 5, 4, 3]
print(s.largest_element(arr))