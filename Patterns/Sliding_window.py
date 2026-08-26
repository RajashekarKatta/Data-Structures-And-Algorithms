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




# Maximum sum of a subarray of size k
# Given an array of integers arr[] and an integer k, find the maximum possible sum among all contiguous subarrays of size exactly k.
# A subarray is a sequence of consecutive elements from the original array. Return the maximum sum that can be obtained from any such subarray of length k.
# Input  : arr[] = [100, 200, 300, 400],  k = 2 -->  Output : 700
class Solution:
    def maximum_sum_of_subarray(self, arr, k):
        window_sum = sum(arr[:k])
        maximum_sum = 0
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            maximum_sum = max(maximum_sum, window_sum)
        return maximum_sum
    
s = Solution()
arr = [100, 200, 300, 400]
print(s.maximum_sum_of_subarray(arr, 2))



# Smallest window containing 0, 1 and 2
# Given a string s consisting of the characters 0, 1 and 2, find the length of the smallest substring of string s that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.
# Input: s = "01212" --> Output: 3
# Explanation: The substring 012 is the smallest substring that contains the characters 0, 1 and 2.
class Solution:
    def smallest_substring(self, s):
        freq = {}
        left = 0
        min_length = float('inf')
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while len(freq) == 3:
                min_length = min(min_length, right - left + 1)
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
        if min_length == float('inf'):
            return -1
        return min_length

a = Solution()
print(a.smallest_substring("01212"))


# Remove all consecutive duplicates from a string
# Given a string s , we have to remove all the consecutive duplicate characters of the string and return the resultant string. 
# Input: str = "aaaaabbbbbb"  --> Output: ab
# Explanation: Remove consecutive duplicate characters from a string s  such as 5 a's are at consecutive so only write a and same like that in b's condition.
class Solution:
    def remove_consective_duplicates(self, s):
        result = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result.append(s[i])
        return ''.join(result)

a = Solution()
print(a.remove_consective_duplicates("aaaaabbbbbbb"))


# Maximum sum subarray having sum less than or equal to given sum
# Given an array arr[] of integers and a number x, find the sum of subarray having a maximum sum less than or equal to the given value of x.
# Input: arr[] = [1, 2, 3, 4, 5], x = 11   -> Output: 10
# Explanation: Subarray having maximum sum is [1, 2, 3, 4].
class Solution:
    def max_sum_subarray(self, arr, x):
        left = 0
        current_sum = 0
        max_sum = 0
        for right in range(len(arr)):
            current_sum += arr[right]
            while current_sum > x:
                current_sum -= arr[left]
                left += 1

            max_sum = max(max_sum, current_sum)
        return max_sum
s = Solution()
arr = [1, 2, 3, 4, 5]
print(s.max_sum_subarray(arr, 11))
