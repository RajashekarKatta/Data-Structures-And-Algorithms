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
        for i in range(len(arr)-1):    # This Step is more imporatnt "(len(arr)-1)"
            arr[i] = arr[i+1]
        arr[-1] = first_element
        return arr

s = Solution()
arr = [1,2,3,4,5]
print(s.rotate_left(arr))


# # Remove duplicates from Sorted Array
# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.
# Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.
# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]
class Solution:
    def remove_duplicates(self, arr):
        i = 0
        for j in range(len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]
        return arr[:i+1]

s = Solution()
arr =[1, 2, 2, 3, 4, 4, 4, 5, 5]
print(s.remove_duplicates(arr))


# Remove duplicates from undorted array
class Solution:
    def remove_duplicates_unsorted(self, arr):
        seen = set()
        result = []
        for num in arr:
            if num not in seen:
                result.append(num)
                seen.add(num)
        return result
s = Solution()
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(s.remove_duplicates_unsorted(arr))


# # # Generating All Subarrays
# Given an array arr[], the task is to generate all the possible subarrays of the given array.
# Input: arr[] = [1, 2, 3] -> Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]
class Solution:
    def generate_subarrays(self, arr):
        result = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                result.append(arr[i:j+1])          # important step arr[i:j+1] and return result
        return result
s = Solution()
arr = [1,2,3]
print(s.generate_subarrays(arr))


# Reversing an array
class Solution:
    def reverse_arr(self, arr):
        left, right = 0, len(arr)-1
        while left < right:      # Here we are using two pointer technique
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
s = Solution()
arr = [1,2,3,4,5]
print(s.reverse_arr(arr))


# # Rotate an Array - Clockwise or Right
# Rotations in the array is defined as the process of rearranging the elements in an array by shifting each element to a new position. 
# This is mostly done by rotating the elements of the array clockwise or counterclockwise.
# input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2 -> Output: {5, 6, 1, 2, 3, 4}
class Solution:
    def rotate_arr(self, arr, d):     # Right rotation 
        n =len(arr)
        d = d % n
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        reverse(arr, 0, n-1)
        reverse(arr, 0, d-1)
        reverse(arr, d, n-1)
        return arr                  # output [4,5,1,2,3]
  
s = Solution()
arr = [1,2,3,4,5]
print(s.rotate_arr(arr, 2)) 


# # Rotate an Array - Anti-Clockwise or left
class Solution:
    def rotate_arr_left(self, arr, d):
        n = len(arr)
        d = d % n
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        reverse(arr, 0, d-1)
        reverse(arr, d, n-1)
        reverse(arr, 0, n-1)
        return arr
s = Solution()
arr = [1,2,3,4,5]
print(s.rotate_arr_left(arr, 2))


# Move all Zeros to End of Array
# Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]  -> Output: [1, 2, 4, 3, 5, 0, 0, 0] -> Time  → O(n) Space → O(1)
class Solution:
    def move_zeros(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count], arr[i] = arr[i], arr[count]   # here we are using two pointer technique
                count += 1
        return arr

s = Solution()
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(s.move_zeros(arr))


# Another Way to find the answer ->  Time O(n) Space → O(1)
class Solution:
    def move_zeros_end(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < len(arr):
            arr[count] = 0
            count += 1
        return arr
s = Solution()
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(s.move_zeros_end(arr))


# Minimum increment by k operations to make all equal
# You are given an array of n-elements, you have to find the number of operations needed to make all elements of array equal.
# Where a single operation can increment an element by k. If it is not possible to make all elements equal print -1.
# Input : arr[] = {4, 7, 19, 16},  k = 3  -> Output : 10
class Solution:
    def min_increment(self, arr, k):
        total = 0
        max_one = max(arr)
        for i in range(len(arr)):
            if (max_one - arr[i]) % k != 0 :
                return -1
            total += (max_one - arr[i]) // k
        return f"Number of Operations needed : {total}"
s = Solution()
arr = [4,7,19,16]
print(s.min_increment(arr, 3))



# Find the Largest element in a given array
class Solution:
    def largest_ele(self, arr):
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        return f"Largest element in the given array: {largest}"

s = Solution()
arr = [10,20,30,40,50]
print(s.largest_ele(arr))



# Find the sum of all elements
class Solution:
    def sum_of_elements(self, arr):
        total = 0
        for num in arr:
            total += num
        return total
s =  Solution()
arr = [10,20,30,40,50]
print(s.sum_of_elements(arr))


# Find the second largest element in the given array
class Solution:
    def second_largest_element(self, arr):
        largest = arr[0]
        second = arr[0]
        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:  # this is important because incase if you get both it will look second largest
                second = num
        return second

s = Solution()
arr = [10.,25,54,39,16,54,]
print(s.second_largest_element(arr))


# Largest three distinct elements in an array
# Given an array arr[], the task is to find the top three largest distinct integers present in the array.
# Note: If there are less than three distinct elements in the array, then return the available distinct numbers in descending order.
# Input: arr[] = [10, 4, 3, 50, 23, 90] -> Output: [90, 50, 23
class Solution:
    def largest_distinct_three(self, arr):
        largest = arr[0]
        second_largest = arr[0]
        third_largest = arr[0]
        for num in arr:
            if num > largest:
                third_largest = second_largest
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                third_largest = second_largest
                second_largest = num
            elif num > third_largest and num != second_largest and num != largest:
                third_largest = num
        return largest, second_largest, third_largest
s = Solution()
arr = [10, 4, 3, 50, 23, 90]
print(s.largest_distinct_three(arr))


# Check if the given Array is Sorted or not if sorted return True or else return False
class Solution:
    def is_sorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:                   # Here this line is important
                return False
        return True
s = Solution()
arr = [1,5,3,2,4]
print(s.is_sorted(arr))


# Find the missing number in a given array
class Solution:
    def missing_number(self, arr):
        n = len(arr) + 1
        total_sum = sum(arr)
        expected_sum = n * (n+1) //2        # here most important part is parenthis(n+1) if you forgot to put parenthsis the output will chage 
        return expected_sum - total_sum
s = Solution()
arr = [1,2,3,5]     # here missing number is 4 lets see output
print(s.missing_number(arr))


# Find the frequency of an given array
class Solution:
    def frequency_count(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        return freq
s = Solution()
arr = [1,6,3,4,1,2,6,3,2]
print(s.frequency_count(arr))


# Find the closest numbeer to Zero
class Solution:
    def closest_to_zero(self, arr):
        closest = arr[0]
        for num in arr:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(closest, num)
        return closest
s = Solution()
arr = [-4,-2,1,-1,4,8]
print(s.closest_to_zero(arr))

# Find the given Two arrays Union
class Solution:
    def union_of_arrays(sself, arr1, arr2):
        union = []
        seen = set()
        for num in arr1:
            if num not in seen:
                seen.add(num)
                union.append(num)
        for num in arr2:
            if num not in seen:
                seen.add(num)
                union.append(num)
        return union
s = Solution()
arr1 = [1,2,3,4]
arr2 = [1,2,3]
print(s.union_of_arrays(arr1, arr2))  


# # Intersection of Two arrays
class Solution:
    def intersection_of_arrays(self, arr1, arr2):
        intersection = []
        seen = set(arr2)              # this is important step
        for num in arr1:
            if num in seen:
                intersection.append(num)
        return intersection
s = Solution()
arr1 = [1,2,3,4]
arr2 = [2,4,6]
print(s.intersection_of_arrays(arr1, arr2))


# Find the Single Number in a given number
class Solution:
    def single_number(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] == 1:
                return f"Single number in an given array: {num}"
        return - 1
s = Solution()
arr = [4, 1, 2, 1, 2]
print(s.single_number(arr))

# Count Occurrences of an Element in an given array
class Solution:
    def coun_occurrence(sel, arr, target):
        count = 0
        for num in arr:
            if num == target:
                count += 1 
        return count                # Count of an element 2 is 3 because three times appears in array
s = Solution()
arr = [1, 2, 2, 2, 3]
print(s.coun_occurrence(arr, 2))


# # check if two arrays are equal:
class Solution:
    def check_two_array_are_equal(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True
s = Solution()
arr1 = [1,2,3,4]
arr2 = [1,2,3,4]
print(s.check_two_array_are_equal(arr1, arr2))

# Find the first repeating element in an array of integers
# Given an array of integers arr[], The task is to find the index of first repeating element in it i.e. 
# the element that occurs more than once and whose index of the first occurrence is the smallest. 
# Input: arr[] = {10, 5, 3, 4, 3, 5, 6}  -> Output: 5
class Solution:
    def first_repeating_ele(self, arr):
        freq = {}                               # Here We are using hashmap 
        for num in arr:  
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] > 1:
                return num
s = Solution()
arr = [10, 5, 3, 4, 3, 5, 6]
print(s.first_repeating_ele(arr))

# Another way to find the first repeating element
class Solution:
    def first_repeat_ele(self, arr):
        seen = set()                # here we are using hash set
        first = -1
        for i in range(len(arr)-1, -1, -1):  #  here to line 522 to 525 most important lines for this problem.
            if arr[i] in seen:
                first = arr[i]
            seen.add(arr[i])
        return first
s = Solution()
arr = [10, 5, 3, 4, 3, 5, 6]
print(s.first_repeat_ele(arr))


# Two Sum problem  # here we are returning numbers
class Solution:
    def two_sum(self ,arr, target):
        hash_map = {}
        for i, num in enumerate(arr):
            compliment = target - num
            if compliment in hash_map:
                return [compliment, num]
            hash_map[num] = i
s = Solution()
arr = [2, 7, 11, 15]
target = 9
print(s.two_sum(arr, target))


# Two Sum Problem 
class Solution:
    def two_sum(self, arr, target):
        hash_map = {}
        for i, num in enumerate(arr):
            compliment = target - num
            if compliment in hash_map:
                return [hash_map[compliment], i]     # Here we are returning indexes
            hash_map[num] = i

s = Solution()
arr = [2, 7, 11, 15]
print(s.two_sum(arr, target))


# If Given arr is sorted find the two pair sum
class Solution:
    def two_sum_sorted(self, arr, target):
        left, right = 0, len(arr) - 1
        current_sum = 0
        result = []
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return arr[left], arr[right]             # if you want index numbers write "return left, right"
            elif current_sum < target:
                left += 1
            else:
                right -= 1

s = Solution()
arr = [2, 7, 11, 15]
print(s.two_sum_sorted(arr, 9))

