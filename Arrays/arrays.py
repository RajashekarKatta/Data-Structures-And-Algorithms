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

# Insert Element at the Beginning of an Array
"""Inserting an element at the beginning of an array takes O(n) time in a normal array. suppose we want to insert an element in the beginning of an array
So The existing elements have to move one position to the right. We need to move n elements, so This takes Time complexity O(n).
# Example
arr = [2,3,4,5]
arr.insert(0, 1)
print(arr)  # [1,2,3,4,5]

"""

# Insert Element at a Given Position in an Array
"""To add an element at a given position in an array, shift all the elements from that position one index to the right, 
and after shifting insert the new element at the required position. So this take Time Complexity O(n)
# Example
arr = [1,2,3,4,5]
arr.insert(2, 10)
print(arr)
"""

# Insert Element at the End of an Array
"""To insert an element at the end of an array, we can simply add the new element at the nth index. So this take Time Complexity O(1)
# Example
arr = [1,2,3,4]
arr.append(5)
print(arr)
"""

# Delete an Element from the Beginning of an Array
"""The idea is to start from the second element and shift all the elements one position to the left. After shifting all the elements,
reduce the array size by 1 to remove the extra element at the end.So this take Time Complexity O(n)
"""

# Delete an Element from a Given Position in an Array
"""The idea is to shift all the elements occurring after the given position, one index to the left and reduce the size of the array by 1.
So this take Time Complexity O(n)
"""

# Delete an Element from the end of an array
"""To delete an element from the end of an array, we can simply reduce the size of array by 1. So this takes Time complexity O(1)
"""

# Example for Basic Arrays
# Alternate elements of an array --> Given an array arr[], the task is to print every alternate element of the array starting from the first element.
class Solutions:
    def alter_native_ele(self, arr):
        result = []
        for i in range(0, len(arr), 2):
            result.append(arr[i])
        return result
s = Solutions()
arr = [1,2,3,4,5,6]
print(s.alter_native_ele(arr))


# Leaders in an array
"""Given an array arr[] of size n, the task is to find all the Leaders in the array. 
An element is a Leader if it is greater than or equal to all the elements to its right side. Note: The rightmost element is always a leader.
Input: arr[] = [16, 17, 4, 3, 5, 2]

"""
class Solution:
    def leaders(self, arr):
        leaders = []
        max_from_right = arr[-1]
        n = len(arr)
        leaders.append(max_from_right)
        for i in range(n-2, -1, -1):      # This is the important step -> (n-2, -1,-1) 
            if arr[i] > max_from_right:
                max_from_right = arr[i]
                leaders.append(arr[i])
        leaders.reverse()
        return leaders
s = Solution()
arr = [16, 17, 4, 3, 5, 2]
print(s.leaders(arr))


# # Rotating Array by one Position right side
class Solution:
    def rotate_right(self, arr):
        if len(arr) <= 1:
            return arr
        last_element = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last_element
        return arr
s = Solution()
arr = [1,2,3,4,5]
print(s.rotate_right(arr))


# Rotating array by one position left side
class Solution:
    def rotate_left(self, arr):
        if len(arr) <= 1:
            return arr
        first_element = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = first_element
        return arr

s = Solution()
arr = [1,2,3,4,5]
print(s.rotate_left(arr))