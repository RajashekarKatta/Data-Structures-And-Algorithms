# Two Pointer Technique
# In DSA Two Pointer Technique is very important pattern. if you understand this pattern much easy to slove Arrays, Strings, Subarrays, Pair Problems

# Use two positions (indices/pointers) in an array or string and move them according to the problem's condition.
# Two pointer technique types  1. Opposite Direction
# 2. Same direction / Sliding window Style 3. Fast and Slow pointer


# Problems On Opposite direction
# Reverse an Array
class Solution:
    def reverse_arr(self, arr):
        left, right = 0, len(arr) -1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
s = Solution()
arr = [1,2,3,4,5]
print(s.reverse_arr(arr))


# Reverse a String
class Solution:
    def reverse_str(self, s):
        s = list(s)
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)

a = Solution()
print(a.reverse_str("rajashekar"))



# Check if Array is Palindrome
class Solution:
    def check_palindrome(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return arr
s = Solution()
arr = [1,2,3,2,1]
print(s.check_palindrome(arr))


# Valid Palindrome -> String
class Solution:
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
a = Solution()
print(a.is_palindrome("malayalam"))
print(a.is_palindrome("A man, a plan, a canal: Panama"))


# Two Sum in a Sorted Array
class Solution:
    def two_sum(self, arr, target):
        left, right = 0, len(arr)-1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False
s = Solution()
arr = [1, 2, 3, 4, 6]
print(s.two_sum(arr, 6))


# Pair With Given Sum in Sorted Array
class Solution:
    def pair_sum(self, arr, target):
        left, right = 0, len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return [arr[left], arr[right]]

            elif current_sum < target:
                left += 1

            else:
                right -= 1
        return []


s = Solution()
arr = [1, 2, 3, 4, 6]
target = 6
print(s.pair_sum(arr, target))


# Pair With Given Difference
class Solution:
    def pair_with_difference(self, arr, k):
        left, right = 0, 1
        while left < len(arr):
            difference = arr[right] - arr[left]
            if difference == k:
                return [arr[left], arr[right]]
            elif difference < k:
                right += 1
            else:
                left += 1

                if left == right:
                    right += 1
        return []

s = Solution()
arr = [1, 2, 5, 8, 10]
print(s.pair_with_difference(arr, 2))



# Merge Two Sorted Arrays
class Solution:
    def merge_two_arr(self, arr1, arr2):
        i, j = 0, 0             # Here we are using same direction
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result
s = Solution()
a = [1, 3, 5]
b = [2, 4, 6]
print(s.merge_two_arr(a, b))


# Level 2 — Intermediate
# Remove Duplicates from Sorted Array
class Solution:
    def remove_duplicates(self, arr):
        slow = 0
        for fast in range(len(arr)):
            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]
        return arr[:slow+1]
s = Solution()
arr = [1, 1, 2, 2, 3, 4, 4]
print(s.remove_duplicates(arr))


# Remove a given value from an array in place.
class Solution:
    def remove_element(self, arr, val):
        i = 0
        for j in range(len(arr)):
            if arr[j] != val:
                arr[i] = arr[j]
                i += 1
                
        return i       # Number of valid elements
    
s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(s.remove_element(nums, val))


# Move Zeroes
class Solution:
    def Move_zeros(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1
        return arr
-1
s = Solution()
arr = [1,0,2,0,0,3,4]
print(s.Move_zeros(arr))



# Squares of a Sorted Array
class Solution:
    def square_sorted_arr(self, arr):
        n = len(arr)
        left, right = 0, n-1
        result = [0] * n
        for i in range(n-1, -1, -1):
            if abs(arr[left]) > abs(arr[right]):
                result[i] = arr[left] ** 2
                left += 1
            else:
                result[i] = arr[right] ** 2
                right -= 1
        return result

s = Solution()
arr = [-4, -1, 0, 3, 10]
print(s.square_sorted_arr(arr))


# Dutch National Flag Problem in Python
# The Dutch National Flag problem is a popular algorithmic problem proposed by Edsger Dijkstra. 
# The problem is to sort an array consisting of three distinct elements (or "colors") in a single pass through the array. 
# The three elements could be anything, but for simplicity, we'll use 0, 1, and 2.
# The goal is to arrange the array such that all 0s come first, followed by all 1s, and then all 2s.
# Input: arr[] = {0, 1, 2, 0, 1, 2}    --> Output: {0, 0, 1, 1, 2, 2}
class Solution:
    def dutch_national_flag(self, arr):
        left = 0 
        mid = 0
        right = len(arr) - 1
        while mid <= right:
            if arr[mid] == 0:
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1

            else:
                arr[mid], arr[right] = arr[right], arr[mid]
                right -= 1
        return arr
s = Solution()
arr = [0, 1, 2, 0, 1, 2]
print(s.dutch_national_flag(arr))


# Partition Array Around a Value We want:
# Elements less than x on the left
# Elements greater than or equal to x on the right
class Solution:
    def partioton_arr(self, arr, x):
        left, right = 0, len(arr) - 1
        while left <= right:
            if arr[left] < x:
                left += 1
            elif arr[right] >= x:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return arr
s = Solution()
arr = [9, 12, 3, 5, 14, 10, 10]
x = 10
print(s.partioton_arr(arr, x))



# Separate Positive and Negative Numbers
class Solution:
    def separate_positive_negative(self, arr):
        left = 0
        right = len(arr) - 1
        while left <= right:
            if arr[left] < 0:               # left is already negative → move forward
                left += 1

            elif arr[right] >= 0:           # right is already positive → move backward
                right -= 1

            else:                           # left has positive and right has negative → swap
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return arr
s = Solution()
arr = [1, -2, 3, -4, 5, -6]
print(s.separate_positive_negative(arr))



# Container with Most Water
# Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, 
# find the maximum amount of water that can be contained between any two lines, together with the x-axis.
# Input: arr[] = [1, 8, 6, 2, 5, 4, 8, 3, 7]  -->  Output: 49
# Explanation: 8 and 5 are 5 distance apart. So the size of the base = 5. Height of container = min(8, 5) = 5. So, total area = 5 * 5 = 25.
class Solution:
    def container_with_most_water(self, arr):
        left, right = 0, len(arr) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_water = min(arr[left], arr[right])
            area = width * current_water
            max_water = max(max_water, area)
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return max_water

s = Solution()
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7] 
print(s.container_with_most_water(arr))










# Same Direction Two Pointer Problems
# Move Zeroes
# Move all zeroes to the end while maintaining the order of non-zero elements.
class Solution:
    def move_zeros_end(self, arr):
        slow = 0
        for fast in range(len(arr)):
            if arr[fast] != 0:
                arr[slow] = arr[fast]
                slow += 1
        while slow < len(arr):
            arr[slow] = 0
            slow += 1
        return arr
s = Solution()
arr = [0, 1, 0, 3, 12]
print(s.move_zeros_end(arr))


# Find Unique Elements
class Solution:
    def unique_ele(self, arr):
        slow = 0
        for fast in range(len(arr)):
            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]
                
        return arr[:slow+1]

s = Solution()
arr = [1, 2, 2, 3, 3, 4]
print(s.unique_ele(arr))


# Remove Duplicates from Sorted Array II
# Now each number can appear at most twice.
class Solution:
    def remove_duplicates_II(self, arr):
        slow = 2
        for fast in range(2, len(arr)):
            if arr[fast] != arr[slow - 2]:
                arr[slow] = arr[fast]
                slow += 1
        return arr

s = Solution()
arr = [1, 1, 1, 2, 2, 3]
print(s.remove_duplicates_II(arr))