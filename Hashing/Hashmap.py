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
        for i in range(1, n+1):
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
