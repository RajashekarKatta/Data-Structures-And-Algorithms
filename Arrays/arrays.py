# Arrays
# Array is a Linear Data Structure. An Array is a Collection of similar types of elements stored in a contiguous memory location.we ca acess the each item through array index

# Operations On Array
# Traversal In Array --> we have two types of Traversal
"""1.Linear Traversal: Linear Traversal is the process of visiting each element of an array sequentially.
starting from the first element and moving towards to the last element.During this process each element is printed onr after the another. 
in this order stored in an array

# Example
class Solution:
    def traversal(self, arr):
        for num in arr:
            print(num)

s = Solution()
arr = [1,2,3,4,5]
s.traversal(arr)
""" 

# Reverse Traversal
"""Reverse traversal is the process of visiting each element of an array starting from the last element and moving towards the first element.
This method is useful when you need to process the elements of an array in reverse order. 
In this type of traversal, you begin from the last index (the rightmost element) and work your way to the first index (the leftmost element).

# Example
class Solution:
    def reverse_traversal(self, arr):
        for i in range(len(arr)-1, -1, -1):
            print(arr[i])

s = Solution()
arr = [1,2,3,4,5]
s.reverse_traversal(arr)   

"""



