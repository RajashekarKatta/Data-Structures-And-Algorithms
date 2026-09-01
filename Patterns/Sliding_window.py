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
# Given an array of 
#  gers arr[] and an integer k, find the maximum possible sum among all contiguous subarrays of size exactly k.
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
                current_sum -= arr[left]            # These steps are important for this problem
                left += 1

            max_sum = max(max_sum, current_sum)
        return max_sum
s = Solution()
arr = [1, 2, 3, 4, 5]
print(s.max_sum_subarray(arr, 11))



# Count substrings with k distinct characters           /****\
# Given a string s consisting of only lowercase English letters and an integer k, count the total number of substrings (not necessarily distinct) of s that contain exactly k distinct characters.
# Note: A substring is a contiguous sequence of characters within a string.
# Substrings that are identical but occur at different positions should each be counted separately.
# Input: s = "abc", k = 2   -->  Output: 2
# Explanation: Possible substrings are ["ab", "bc"]
class Solution:
    def count_at_most_k(self, s, k):
        freq = {}
        left = 0
        count = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]] 
                left += 1
            count += right - left + 1
        return count
    
    def count_substring(self, s, k):
        return (self.count_at_most_k(s, k) - self.count_at_most_k(s, k - 1))
    
s = Solution()
print(s.count_substring("abc", 2))




# # Moving Averages using Sliding window Technique
class Solution:
    def moving_averages(self, arr, k):
        averages = []
        current_sum = sum(arr[:k])
        averages.append(current_sum//k)
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            averages.append(current_sum//k)
        return averages
s = Solution()
arr = [30, 32, 34, 31, 35, 33, 29]
print(s.moving_averages(arr, 3))



# Smallest subarray with sum ≥ target.
# Given an array of positive integers arr[] and a positive integer target, find the minimum length of 
# a contiguous subarray whose sum is greater than or equal to target.
# If there is no such subarray, return -1.
class Solution:
    def min_subarray_length(self, arr, target):
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(arr)):
            current_sum += arr[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= arr[left]
                left += 1
        if min_length == float('inf'):
            return -1
        return min_length

s = Solution()
arr = [2, 3, 1, 2, 4, 3]
print(s.min_subarray_length(arr, 7))


# Smallest subarray with sum ≥ target.       NOTE: "SAME PROBLEM ABOVE ONE BUT HERE WE ARE RETURNING SMALLEST SUBARRAY"
# Given an array of positive integers arr[] and a positive integer target, find the minimum length of 
# a contiguous subarray whose sum is greater than or equal to target.
# If there is no such subarray, return -1.
class Solution:
    def minimum_subarray(self, arr, target):
        left = 0
        current_sum = 0
        min_length = float('inf')
        result = []
        for right in range(len(arr)):
            current_sum += arr[right]
            while current_sum >= target:
                if min_length > (right - left + 1):
                    min_length = right - left + 1
                    result = arr[left:right+1]
                current_sum -= arr[left]
                left += 1
        return result
    
s = Solution()
arr = [2, 3, 1, 2, 4, 3]
print(s.minimum_subarray(arr, 7))



# Smallest Subarray with Sum Greater Than a Given Value      *****
# Given an array of positive integers arr[] and an integer x, find the minimum length of a contiguous subarray whose sum is strictly greater than x.
# If there is no such subarray, return 0.
# Input: arr[] = [1, 4, 45, 6, 10, 19]  --> x = 51
class Solution:
    def smallest_subarray_with_sum_greater(self, arr, target):
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(arr)):
            current_sum += arr[right]
            while current_sum > target:
                min_length = min(min_length, right - left + 1)
                current_sum -= arr[left]
                left += 1
        if min_length != float('inf'):
            return min_length
        else:
            return 0
s = Solution()
arr = [1, 4, 45, 6, 10, 19]
print(s.smallest_subarray_with_sum_greater(arr, 52))



# Subarray with Given Sum               Most important problem              *****
# Given an array of positive integers arr[] and a positive integer target, find a contiguous subarray whose sum is equal to target.
# Return the starting and ending positions of the first such subarray. If no such subarray exists, return [-1].
class Solution:
    def subarry_with_sum(self, arr, target):
        left = 0
        current_sum = 0
        for right in range(len(arr)):
            current_sum += arr[right]
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                return arr[left:right]
        return None
s = Solution()
arr = [1, 4, 20, 3, 10, 5]
print(s.subarry_with_sum(arr, 33))



# Maximum Consecutive Ones After Flipping Zeroes    *****
# Given a binary array arr[] and an integer k, find the maximum length of a subarray containing all ones after flipping at most k zeroes to 1's.
# Input: arr[] = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], k = 2   --> Output: 8
# Explanation: By flipping the zeroes at index 5 and 7, we get the longest subarray from index 3 to 10 containing all 1's.
class Solution:
    def max_consective_ones(self, arr, k):
        left = 0
        max_length = 0
        zero_count = 0
        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
s = Solution()
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
print(s.max_consective_ones(arr, 2))    


# Max Consecutive Bit                           *****
# Given an array arr[] consisting of only 0’s and 1’s, return count of the maximum number of consecutive 1’s or 0’s present in the array. 
# Input: arr[] = [0, 1, 0, 1, 1, 1, 1]  -->  Output: 4
# Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6
class Solution:
    def max_consective_1(self, arr):
        current = 1
        maximum = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                current += 1
            else:
                current = 1
            maximum = max(maximum, current)
        return f"maximum consective ones {maximum}"
s = Solution()
arr = [0, 1, 0, 1, 1, 1, 1]
print(s.max_consective_1(arr))




# Longest Subarray with K Sections of Unique Items              maximum fruits in baseket           *****
# You are given an array of positive integers arr[] and an integer k. The task is to find length of the longest subarray with the following conditions
# Each element must fit into one of k sections.
# Each section can only store a unique number and its multiple consecutive instances.
# Input: arr[] = [1, 2, 2, 3, 1, 4], k = 2  -->  Output: 3
# Explanation: The subarray is [1, 2, 2, 3, 1], the sections are [1], [2, 2], [3] and [1]
# Total elements chosen = 3.
class Solution:
    def longest_subarray(self, arr, k):
        freq = {}
        left = 0
        max_length = 0
        for right in range(len(arr)):
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            while len(freq) > k:
                freq[arr[left]] -= 1

                if freq[arr[left]] == 0:
                    del freq[arr[left]] 
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
s = Solution()
arr = [1, 2, 2, 3, 1, 4]
print(s.longest_subarray(arr, 2))



# Subarrays Product Less than K                 *****
# Difficulty: MediumAccuracy: 21.0%Submissions: 123K+Points: 4
# Given an integer array arr[] of positive numbers, the task is to find the number of possible contiguous subarrays having product less than k.
# Input : k = 10, arr[] = [1, 2, 3, 4]  --->  Output : 7
# Explanation: The contiguous subarrays whose product is less than 10 are [1], [2], [3], [4], [1, 2], [2, 3], and [1, 2, 3]. Therefore, the total number of valid contiguous subarrays is 7.
class Solution:
    def count_subarrays(self, arr, k):
        left = 0
        product = 1
        count = 0
        for right in range(len(arr)):
            product *= arr[right]
            while product >= k:
                product //= arr[left]
                left += 1
            count += right - left + 1
        return count 
s = Solution()
arr = [1, 2, 3, 4]
print(s.count_subarrays(arr, 10))








