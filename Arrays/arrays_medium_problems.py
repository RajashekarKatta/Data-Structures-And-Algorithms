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
# Input: arr[] = [1, 2, 2, 1]  ->  Output: [2 1 2] 1
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