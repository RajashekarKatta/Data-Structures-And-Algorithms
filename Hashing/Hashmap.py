# Hashing is a Data Structure technique designed to insert, delete and search data in average constant time O(1). 
# it maps large variable sized input values into fixed size integer indices using a mathematical formula called a Hashing Function then stores the record in hash Table
# We use hashing for dictionaires, frequency counting, maintaining data for quick access by key etc. 


# There are mainly two forms of hash typically implemented in programming languages.
# Hash Set : Collection of unique keys.
# Hash Map : Collection of key value pairs with keys being unique.


# Hash Functions
# A hash function is function that takes an input() of arbitrary size and converts it into - fixed size value, called a hash value or hash code.
# For example, using the modulo method:
# H(x) = x % 10


# Types of Hash Functions
# 1. Division Method
# 2. Multiplication Method  etc..

# Division Method
def integer_hash(key:int, table_size: int = 10) -> int:
    return key % table_size             # we use division method when we are working with integers(arrays)


def string_hash(s: str, table_size: int = 10) -> int:
    primes = 31
    hash_value = 0
    for char in s:
        hash_value = (hash_value * primes + ord(char)) % table_size
    return hash_value


# multiplication method
import math
def multiplication_hash(key: int, table_size: int = 100) -> int:
    A = (math.sqrt(5) - 1) / 2 
    fractional_part = (key * A) % 1
    index = math.floor(table_size * fractional_part)
    return index

# Check if an array is subset of another array
# Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. 
# Both arrays are not sorted, and elements are distinct.  Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
# Output: true
class Solution:
    def is_subset(self, a, b):
        hash_set = set(a)
        for num in b:
            if num not in hash_set:
                return False
        return True

s = Solution()
a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1] 
print(s.is_subset(a, b))



# Check for Disjoint Arrays or Sets ---> Two arrays are disjoint if they have no common element.
# Given two arrays a[] and b[], check if they are disjoint, i.e., there is no element common between both the arrays.
# Examples:Input: a[] = [12, 34, 11, 9, 3], b[] = [2, 1, 3, 5] --> Output: False
class Solution:
    def are_disjoint(self, a, b):
        hash_set = set(a)
        for num in b:
            if num in hash_set:
                return False
        return True

s = Solution()
a = [12, 34, 11, 9, 3]
b = [2, 1, 3, 5]
print(s.are_disjoint(a, b))


# Check if two arrays are equal or not
# Given two arrays, a[] and b[] of equal length. The task is to determine if the given arrays are equal or not. Two arrays are considered equal if:
# Both arrays contain the same set of elements.
# The arrangements (or permutations) of elements may be different.
# If there are repeated elements, the counts of each element must be the same in both arrays.
# Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1] -->  Output: true
class Solution:
    def are_equal(self, a, b):
        if len(a) != len(b):
            return False
        
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        for num in b:
            freq[num] = freq.get(num, 0) - 1

        for num in freq:
            if freq[num] != 0:
                return False
        return True

s = Solution()
a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]
print(s.are_equal(a, b))


# Fizz Buzz
class Solution:
    def fizz_buzz(self, n):
        result = []
        hash_map = {3:"Fizz", 5:"Buzz"}
        divisors = [3, 5]
        for i in range(1, n+1):     # here we are taking starting range 1 because expected result started from 1.
            s = ""
            for d in divisors:
                if i % d == 0:
                    s += hash_map[d]
            if not s:
                s += str(i)
            result.append(s)
        return result

s = Solution()
print(s.fizz_buzz(7))


# Max Distance Between Two Occurrences
# Given an array arr[], the task is to find the maximum distance between two occurrences of any element. If no element occurs twice, return 0.
# Input: arr = [1, 1, 2, 2, 2, 1] --> Output: 5
# Explanation: distance for 1 is: 5-0 = 5, distance for 2 is: 4-2 = 2, So max distance is 5.
class Solution:
    def max_distance(self, arr):
        max_distance = 0
        hash_map = {}
        for i in range(len(arr)):
            if arr[i] not in hash_map:
                hash_map[arr[i]] = i
            else:
                max_distance = max(max_distance, i - hash_map[arr[i]])
        return max_distance

s = Solution()
arr = [1, 1, 2, 2, 2, 1]
print(s.max_distance(arr))


# Duplicate within K Distance in an Array
# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. 
# If such a pair exists, return 'Yes', otherwise return 'No'. --> Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]  -->  Output: No
# Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.
class Solution:
    def duplicate_within_k_distance(self, arr, k):
        last_seen = {}
        for i, num in enumerate(arr):
            if num in last_seen:
                if (i - last_seen[num]) <= k:
                    return "yes"
            last_seen[num] = i
        return "No"

s = Solution()
arr = [1, 2, 3, 4, 1, 2, 3, 4]
print(s.duplicate_within_k_distance(arr, 3))


# Another hash method using hash_set to find the answer
class Solution:
    def duplicate_within_k(self, arr, k):
        hash_set = set()
        for i in range(len(arr)):
            if arr[i] in hash_set:
                return True
            hash_set.add(arr[i])

            if (i >= k):
                hash_set.remove(arr[i-k])           # this step is most important
        return False

if __name__ == "__main__":
    s = Solution()
    arr = [10, 5, 3, 4, 3, 5, 6]
    if s.duplicate_within_k(arr, 3):
        print("Yes")
    else:
        print("No")


# Intersection of two Arrays
# Given two arrays a[] and b[], find their intersection — the unique elements that appear in both. Ignore duplicates, and the result can be in any order.
# Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]  --> Output: [1, 3]
# Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements
class Solution:
    def intersection_of_arrays(self, a, b):
        hash_set = set(a)
        res = []
        for num in b:
            if num in hash_set:
                res.append(num)
                hash_set.remove(num)            # Erase it from sa to avoid duplicates
        return res

s = Solution()
a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]
print(s.intersection_of_arrays(a,b))


# Union of Two Arrays
# Given two arrays a[] and b[], Return union of both the arrays in any order.
# Note: Union of two arrays is an array having all distinct elements that are present in either array.
# Input : a[] = [1, 2, 3], b[] = [4, 5, 6],  Output : [1, 2, 3, 4, 5, 6]
# Explanation: 1, 2, 3, 4, 5 and 6 are the elements present in either array.
class Solution:
    def union_of_arrays(self, a, b):
        hash_set = set()
        for num in a:
            if num not in hash_set:
                hash_set.add(num)

        for num in b:
            if num not in hash_set:
                hash_set.add(num)

        return list(hash_set)

s = Solution()
a = [1, 2, 3]
b = [4, 5, 6]
print(s.union_of_arrays(a, b))


# Most frequent in an array
# Given an integer array arr[], find the element that appears most frequently. If multiple elements have the same highest frequency, return the largest among them.
# Input : arr[] = [1, 3, 2, 1, 4, 1]  --> Output : 1
# Explanation: 1 appears three times in array which is maximum frequency.
class Solution:
    def frequency_of_arr(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        max_freq = 0
        result = 0
        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]

            elif freq[num] == max_freq and num > result:
                result = num
        return result

s = Solution()
arr = [1, 2, 2, 4, 1]
print(s.frequency_of_arr(arr))


# Two Sum - Pair with given Sum
# Given an array arr[] of n integers and a target value, check if there exists a pair whose sum equals the target. This is a variation of the 2-Sum problem.
# Input: arr[] = [0, -1, 2, -3, 1], target = -2 -->  Output: true
# Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.
class Solution:
    def Two_Sum(self, arr, target):
        hash_set = set()
        for num in arr:
            compliment = target - num
            if compliment in hash_set:
                return True
            hash_set.add(num)

        return False

s = Solution()
arr = [0, -1, 2, -3, 1]
target = -2
print(s.Two_Sum(arr, target))


# 2 Sum - Count pairs with given sum
# Given an array arr[] of n integers and a target value, find the number of pairs of integers in the array whose sum is equal to target.
# Input: arr[] = [1, 5, 7, -1, 5], target = 6 --> Output:  3
# Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).  
class Solution:
    def two_sum_pairs(self, arr, target):
        freq = {}
        pair_count = 0
        for num in arr:
            compliement = target - num
            if compliement in freq:
                pair_count += freq[compliement]

            freq[num] = freq.get(num, 0) + 1
        return pair_count

s = Solution()
arr = [1, 5, 7, -1, 5]
print(s.two_sum_pairs(arr, 6))


# Count pairs with absolute difference equal to k
# Given an array arr[] and a positive integer k, the task is to count all pairs (i, j) such that i < j and absolute value of (arr[i] - arr[j]) is equal to k. 
# Input: arr[] = [1, 4, 1, 4, 5], k = 3  --> Output: 4
# Explanation: There are 4 pairs with absolute difference 3, the pairs are [1, 4], [1, 4], [1, 4] and [4, 1]
class Solution:
    def count_pairs_with_difference_k(self, arr, k):
        hash_map = {}
        pair_count = 0
        for num in arr:
            if num - k in hash_map:                 # Bellow steps are important for this problem
                pair_count += hash_map[num-k]

            if num + k in hash_map:
                pair_count += hash_map[num + k]

            hash_map[num] = hash_map.get(num, 0) + 1

        return pair_count

s = Solution()
arr = [1, 4, 1, 4, 5]
k = 3
print(s.count_pairs_with_difference_k(arr, k))


# Only Repeating From 1 To n-1
# Given an array arr[] of size n filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. The task is to find the repetitive element.
# Input: arr[] = [1, 3, 2, 3, 4]
# Explanation: The number 3 is the only repeating element.
class Solution:
    def find_repeating_ele(self, arr):
        hash_set = set()
        for num in arr:
            if num in hash_set:
                return f"Repeating element in given array {num}"
            hash_set.add(num)
        return None

s = Solution()
arr = [1, 3, 2, 3, 4]
print(s.find_repeating_ele(arr))


# Missing Element in Range
# Given an array arr[] of integers and a range [low, high], find all the numbers within the range that are not present in the array. return the missing numbers in sorted order.
# Input: arr[] = [10, 12, 11, 15], low = 10, high = 15   --> Output: [13, 14]
# Explanation: Numbers 13 and 14 lie in the range [10, 15] but are not present in the array.
class Solution:
    def missing_element_range(self, arr, low, high):
        hash_set = set(arr)
        res = []
        i = low
        while i <= high:
            if i not in hash_set:
                res.append(i)
            i += 1
        return res
s = Solution()
arr = [10, 12, 11, 15]
low = 10
high = 15
print(s.missing_element_range(arr, low, high))
        
# We can also write code using for loop
class Solution:
    def missing_ele_range(self, arr, low, high):
        hash_set = set(arr)
        res = []
        for i in range(low, high + 1):
            if i not in hash_set:
                res.append(i)

        return res
s = Solution()
arr = [10, 12, 11, 15]
low = 10
high = 15
print(s.missing_ele_range(arr, low, high))


# Missing Elements of a Range in an Array
# Given an array arr[] of size n, let min and max be the minimum and maximum elements in the array respectively. 
# Find how many numbers should be added so that every element in the range [min, max] occurs at least once in the array.
# input : arr[] = [4, 5, 3, 8, 6] --> Output : 1
# Explanation: Range is 3-8; only 7 is missing, so count = 1.
class Solution:
    def missing_ele_count(self, arr):
        hash_set = set(arr)
        count = 0
        min_value = min(arr)
        max_value = max(arr)
        for i in range(min_value, max_value+1):
            if i not in hash_set:
                count += 1
        return count

s = Solution()
arr = [4, 5, 3, 8, 6]
print(s.missing_ele_count(arr))


# Minimum Subsets with Distinct Elements
# You are given an array of n-element. You have to make subsets from the array such that no subset contain duplicates. Find out minimum number of subset possible.
# Input : arr[] = {1, 2, 3, 4}  --> Output :1
# Explanation : A single subset can contains all values and all values are distinct.
class Solution:
    def min_subset_with_distinct_ele(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        result = max(freq.values())
        return f"Distinct subset count: {result}"

s = Solution()
arr = [1,2,3,3]
print(s.min_subset_with_distinct_ele(arr))


# Another way to find the answer
class Solution:
    def minimum_subset_with_distinct_ele(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        max_count = 0
        for key, value in freq.items():
            if max_count < value:
                max_count = value
        return f"Distinct subset count: {max_count}"

s = Solution()
arr = [40,50,30,40,50,30,30]
print(s.minimum_subset_with_distinct_ele(arr))


# Remove minimum elements such that no common elements exist in two arrays
# Given two arrays arr1[] and arr2[] consisting of n and m elements respectively. The task is to find the minimum number of elements 
# to remove from each array such that intersection of both arrays becomes empty and both arrays become mutually exclusive.
# input: arr[] = { 1, 2, 3, 4}, arr2[] = { 2, 3, 4, 5, 8 }  --> Output: 3
# Explanation: We need to remove 2, 3 and 4 from any array.
class Solution:
    def remove_minimum_ele(self, arr1, arr2):
        freq1 = {}
        freq2 = {}
        count = 0
        for num in arr1:
            freq1[num] = freq1.get(num, 0) + 1
        for num in arr2:
            freq2[num] = freq2.get(num, 0) + 1
        for num in freq1:
            if num in freq2:
                count += min(freq1[num], freq2[num])
        return f"minimum number of elements to remove: {count}"

s = Solution()
arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 4, 5, 8]
print(s.remove_minimum_ele(arr1, arr2))










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
