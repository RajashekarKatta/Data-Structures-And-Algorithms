# Sliding Window Technique to Solve the Problems

# Imagine if you want to fing the maxim sum of the any subarray
# Finding maxsum subarray by using Brute Force  arr = [2,4,6,8,10,12] window_size k = 3
class Solution:
    def max_sum_brute_force(self, arr, k): 
        max_sum = 0
        for i in range(len(arr)- k + 1):
            current_sum = 0
            for j in range(i, i+k):
                current_sum += arr[j]               # BRUTE FORCE METHOD

            max_sum = max(max_sum, current_sum)
        return max_sum
s = Solution()
arr = [2,4,6,8,10,12]
print(s.max_sum_brute_force(arr, 3))



# Now we will see Sliding window approach 
class Solution:
    def max_sum(self, arr, k):
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]       # this is important step
            max_sum = max(max_sum, window_sum)
        return max_sum
s = Solution()
arr = [2,4,6,8,10,12]
print(s.max_sum(arr, 3))

# In Sliding window we have two types  1). Fixed size window like max_sum, average,...etc
# 2) Variable size Sliding Window the window changes. Window keeps changing. This is harder but much more useful.
# Example for variable size sliding window
# Longest substring without repeating characters.
# Given a string s having lowercase characters, find the length of the longest substring without repeating characters. 
# Input: s = "geeksforgeeks"  -->  Output: 7 
# Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.
class Solution:
    def longest_substring(self, s):
        seen = set()
        left = 0
        maximum = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])

            maximum = max(maximum, right - left + 1)
        return f"longest substring without repeating characters {maximum}"

a = Solution()
print(a.longest_substring("GeeksforGeeks"))




