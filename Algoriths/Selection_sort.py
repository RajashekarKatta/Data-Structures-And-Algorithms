# Selection Sort Algorithm   O(n^2) Time and O(1) Space
"""We start by finding the smallest element and swap it with the first element. Then we find the next smallest element among the remaining and swap it with the second element.
This continues until all elements are placed in their correct positions."""

# Selection Sort Implementation in Python
class Solution:
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

s = Solution()
arr = [5, 3, 8, 4, 2]
print(s.selection_sort(arr))



# Ascending order in selection sort
class Solution:
    def selection_sort_ascending(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
s = Solution()
arr = [6, 8, 2, 4, 5, 9]
print(s.selection_sort_ascending(arr))


# Selection Sort Desecnding order
class Solution:
    def selection_sort_desecnding(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] > arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
s = Solution()
arr = [6, 8, 2, 4, 5, 9]
print(s.selection_sort_desecnding(arr))



# Find minimum using selection sort
class Solution:
    def find_minimum(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr[0]
s = Solution()
arr = [6, 8, 2, 4, 5, 9]
print(s.find_minimum(arr))


# Finding Maximum Element in selection Sort
class Solution:
    def find_minimum(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr[-1]
s = Solution()
arr = [4, 9, 2, 7, 5]
print(s.find_minimum(arr))


# Find Second Smallest in selection sort algorithm
class Solution:
    def find_minimum(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr[1]
s = Solution()
arr = [8, 3, 6, 1, 5]
print(s.find_minimum(arr))




# Second Largest element in selection sort
class Solution:
    def find_minimum(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr[-2]
s = Solution()
arr = [4, 9, 2, 7, 5]
print(s.find_minimum(arr))



# Reverse Sorted Array by using selection sort
class Solution:
    def find_minimum(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr
s = Solution()
arr = [5, 4, 3, 2, 1]
print(s.find_minimum(arr))


