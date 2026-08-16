# Array medium problems or you can say Level tWo problems in array


# # Duplicate within K Distance in an Array
# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. 
#If such a pair exists, return 'Yes', otherwise return 'No'.
# Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]--> Output: Yes
class SOlution:
    def duplicate_within_k_distance(self, arr, k):
        last_seen = {}
        for i, num in enumerate(arr):
            if num in last_seen:
                if i - last_seen[num] <= k:
                    return "yes"
            last_seen[num] = i
        return "No"
s = SOlution()
arr = [1, 2, 3, 1, 4, 5]
print(s.duplicate_within_k_distance(arr, 3))


# Rearrange array such that even positioned are greater than odd
# Given an array arr[], rearrange its elements according to 1-based indexing such that for every even index i, arr[i] is greater than or equal to arr[i-1],
# and for every odd index i, arr[i] is less than or equal to arr[i-1]. Return the rearranged array that satisfies these conditions for all valid indices.
# Find the resultant array.[consider 1-based indexing].
# Input: arr[] = [1, 2, 2, 1]  ->  Output: [2 1 2 1]
class Solution:
    def rearrange_arr(self, arr):   # Alternative sorting  problem
        for i in range(1, len(arr)):
            if (1 + i) % 2 == 0:
                if arr[i] > arr[i-1]:
                    arr[i] , arr[i-1] = arr[i-1], arr[i]
            else:
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
        return arr
s = Solution()
arr = [1, 2, 2, 1] 
print(s.rearrange_arr(arr))  



# # Sum of all Subarrays
# Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.
# Input: arr[] = [1, 4, 5, 3, 2] ->> Output: 116
class Solution:
    def sum_of_all_subarrays(self, arr):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarrays.append(arr[i:j+1])
        return subarrays

s = Solution()
arr = [1, 3, 2]
print(s.sum_of_all_subarrays(arr))


# # Find Smallest Missing Positive Number
# Given an unsorted array arr[] with both positive and negative elements, the task is to find the smallest positive number missing from the array.
# Note: You can modify the original array.
# Input: arr[] = {2, -3, 4, 1, 1, 7} -->> Output: 3
# Explanation: 3 is the smallest positive number missing from the array.
class Solution:
    def smallest_missing_number(self, arr):
        new_set = set()
        for num in arr:
            if num not in new_set:
                new_set.add(num)

        i = 1
        while True:
            if i not in new_set:
                return i
            i += 1
s = Solution()
arr = [2, -3, 4, 1, 1, 7]
print(s.smallest_missing_number(arr))