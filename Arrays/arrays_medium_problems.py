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