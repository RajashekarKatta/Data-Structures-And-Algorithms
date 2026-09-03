# Insertion Sort
"""We start with the second element, assuming the first is already sorted. If the second element is smaller, we shift the first element and insert the second in the correct position. 
Then we move to the third element and place it correctly among the first two. This process continues until the entire array is sorted."""

# Insertion Sort implementation in Python   O(n^2) Time and O(1) Space
class Solution:
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j +1] = key
        return arr
s = Solution()
arr = [5, 3, 8, 4, 2]
print(s.insertion_sort(arr))


# Q1. Ascending Order by using Insertion order
class Solution:
    def insertion_sort_ascending(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j +1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
s = Solution()
arr = [5, 3, 8, 4, 2]
print(s.insertion_sort_ascending(arr))


# Descending Order by using Insertion order
class Solution:
    def insertion_sort_ascending(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] < key:
                arr[j +1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
s = Solution()
arr = [5, 3, 8, 4, 2]
print(s.insertion_sort_ascending(arr))




# Find the Correct Position and insert the element
class Solution:
    def find_position(self, arr, key):
        arr.append(0)
        j = len(arr) -2                 # for this problem works only sorted arrays only
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        return f"Position of the inserted key is {j + 1}",  arr
    
s = Solution()
arr = [2, 4, 6, 8, 9]
print(s.find_position(arr, 5))




# Inserting an element in the given arr by using insertion sort
class Solution:
    def inserting_element(self, arr, key):
        arr.append(0)
        j = len(arr) - 2
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        return arr
s = Solution()
arr = arr = [2, 4, 6, 8, 9]
print(s.inserting_element(arr, 5))












