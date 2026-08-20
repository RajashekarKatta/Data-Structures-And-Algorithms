# Medium Problems On String

# Find the Earliest Repeating Character
# Given a string S of length n, the task is to find the earliest repeated character in it. The earliest repeated character means, 
# the character that occurs more than once and whose second occurrence has the smallest index.
# Input: s = "geeksforgeeks" --> Output: e
class Solution:
    def firstRepeatingChar(self, s):
        freq = {}
        for char in s:        # Here we are using dictionary/ hashmap
            if char in freq:
                return char
            freq[char] = 1
        return None
a = Solution()
print(a.firstRepeatingChar("Geeksforgeeks"))

# Another way to find first Repeating Number
class Solution:
    def first_repeat_char(self, s):
        seen = set()            # here we are using hash map simply say set
        for char in s:
            if char in seen:
                return f"First Repeating char: {char}"
            seen.add(char)
        return None
a = Solution()
print(a.first_repeat_char("Geeksforgeeks"))


# First non-repeating character of given string
# Given a string s of lowercase English letters, the task is to find the first non-repeating character. If there is no such character, return '$'. 
# Input: s = "geeksforgeeks"
# Output: 'f'
class Solution:
    def first_non_repeating_char(self, s):              # s → to maintain the original order and find the first character
        freq = [0] * 26                                 # freq → to check whether that character occurs only once
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for char in s:
            if  freq[ord(char) - ord('a')] == 1:
                return f"first Non repeating character: {char}"
        return None
a = Solution()
print(a.first_non_repeating_char("geeksforgeeks"))




# K'th Non-repeating Character
# Given a string str of length n (1 <= n <= 106) and a number k, the task is to find the kth non-repeating character in the string.
# Input : str = geeksforgeeks, k = 3
# Output : r                            k means third non-repeating character is 'r', first nonprepeat char is 'f', second nonrepeatchar is 'o' and third non repeat char is 'r' our answer.
class Solution:
    def kth_non_repeating_char(self, s, k):
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        non_repeat = 0
        for char in s:
            if freq[ord(char) - ord('a')] == 1:
                non_repeat += 1
            if non_repeat == k:
                return f"K'th Non-repeating character is '{char}'"
a = Solution()
print(a.kth_non_repeating_char("geeksforgeeks", 3))




# Reverse a string preserving space positions
# Given a string s, the task is to reverse the given string while preserving the position of spaces.
# Input: "internship at geeks for geeks"
# Output: skeegrofsk ee gtapi hsn retni
class Solution:
    def reversing_string(self, s):
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == ' ':
                left += 1
            elif s[right] == ' ':
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)                           # output is skeegrofsk ee gtapi hsn retni
a = Solution()
print(a.reversing_string("internship at geeks for geeks"))


# Check if Strings Are Rotations of Each Other
# Given two strings s1 and s2 of equal length, determine whether s2 is a rotation of s1.
# A string is said to be a rotation of another if it can be obtained by shifting some leading characters of the original string to its end without changing the order of characters.
# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: After 2 right rotations, s1 will become equal to s2.
class Solution:
    def are_rotations_each_other(self, s1, s2):
        if len(s1) != len(s2):
            return False
        doubled = s1 + s1
        for i in range(len(s1)):
            if doubled[i:i+len(s2)]== s2:
                return True
        return False
a = Solution()
print(a.are_rotations_each_other("abcd", "cdab"))
            

# First Repeating character in a given string
class Solution:
    def first_repeating_character(self, s):     
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1 

        for char in s:                      # s → to maintain the original order and find the first character
            if freq[char] > 1:
                return char
        return None

a = Solution()
print(a.first_repeating_character("geeksforgeeks"))


# Add n binary strings
# Given n binary strings, the task is to find their sum which is also a binary string.
# Input:  arr[] = ["1101", "111"]
# Output: "10100"
class Solution:
    def sum_of_binary(self, arr):
        total_sum = 0
        for s in arr:
            total_sum += int(s, 2)
        return str(bin(total_sum)[2:])

a = Solution()
arr = ["1101", "111"]
print(a.sum_of_binary(arr))



# Multiply Large Numbers represented as Strings
# Given two numbers as strings s1 and s2, calculate their product.
# Note: The numbers can be negative. There can be zeros in the beginning of the numbers.
# Input: s1 = "0033", s2 = "2"  -->  Output: "66" --> Explanation: 33 * 2 = 66
class Solution:
    def multiply_strings(self, s1, s2):
        if s1 == 0 and s2 == 0:
            return 0
        s1 = int(s1)
        s2 = int(s2)
        total = s1 * s2
        return total
a = Solution()
print(a.multiply_strings("0033", "2"))


# Isomorphic Strings Check
# Given two strings s1 and s2 of equal length, consisting only of lowercase English letters, determine if they are isomorphic.
# Two strings are isomorphic if characters in s1 can be replaced to get s2 such that:
# Each character in s1 maps to a unique character in s2.
# The mapping is consistent throughout the string.
# The order of characters is preserved. -->   Input: s1 = "aab", s2 = "xxy"  ->  Output: true
class Solution:
    def isomorphic_string(self, s1, s2):
        if len(s1) != len(s2): 
            return False
        map_s1 ={}
        map_s2 = {}
        for i in range(len(s1)):
            if s1[i] not in map_s1:
                map_s1[s1[i]] = i
            if s2[i] not in map_s2:
                map_s2[s2[i]] = i

            if map_s1[s1[i]] != map_s2[s2[i]]:
                return False
        return True

a = Solution()
print(a.isomorphic_string("aab", "xxy"))       

