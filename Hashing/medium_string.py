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