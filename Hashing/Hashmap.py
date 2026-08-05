# Hashmap using dictionary in python
# Hashmap + Dictionary using sliding window technique to find the longest substring with sum K Problem
class Solution:
    def longest_substring_with_sum_k(self, arr, k):
        sum_dict = {}
        max_length = 0
        current_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum == k:
                max_length = i + 1

            if current_sum - k in sum_dict:
                length = i - sum_dict[current_sum - k]
                max_length = max(max_length, length)

            if current_sum not in sum_dict:
                sum_dict[current_sum] = i
        return max_length

s = Solution()
arr = [10, 5, 2, 7, 1, 9]
k = 15
print(s.longest_substring_with_sum_k(arr, k))