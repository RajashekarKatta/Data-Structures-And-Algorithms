# Basic String Problems

# Find the length of the given string
class Solution:
    def length_of_string(self, s):
        length = 0
        for char in s:
            length += 1
        return length
a = Solution()
print(a.length_of_string("rajashekar"))



# Check if two strings are same
class Solution:
    def are_strings_equal(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True

a = Solution()
print(a.are_strings_equal("hello", "hello"))



# Program to Search a Character in a String
class Solution:
    def findchar(self, s, ch):
        for i in range(len(s)):
            if s[i] == ch:
                return i
        return -1

a = Solution()
print(a.findchar("geeksforgeeks", "k"))


# Insert a character in String at a Given Position
class Solution:
    def insertchar(self, s ,ch, pos):
        result =''
        for i in range(len(s)):
            if i == pos:
                result += ch
            result += s[i]
        return result
a = Solution()
print(a.insertchar("Geeks", "A", 3))


# Remove a Character from a Given Position
class Solution:
    def remove_char(self, s, pos):
        result = ''
        for i in range(len(s)):
            if i == pos:
                continue
            result += s[i]
        return result

a = Solution()
print(a.remove_char("Geeks", 3))


# Remove all occurrences of a character in a string
class Solution:
    def remove_all_occurrencce(self, s, ch):
        result = ''
        for i in range(len(s)):
            if s[i] == ch:
                continue
            result += s[i]
        return result
a = Solution()
print(a.remove_all_occurrencce("GeeksforGeeks", 'e'))


# Concatenation of Two Strings
class Solution:
    def concatination(self, s1, s2):
        result = ''
        for char in s1:       # Simply you can use "return s1 + s2"
            result += char

        for char in s2:
            result += char
        return result

a = Solution()
print(a.concatination("Hello", "World!"))


# Reverse a String
class Solution:
    def reverse_string(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
a = Solution()
print(a.reverse_string("rajashekar"))


# All substrings of a given String
class Solution:
    def generate_substrings(self, s):
        result =[]
        for i in range(len(s)):
            for j in range(i, len(s)):
                result.append(s[i:j+1])
        return result
a = Solution()
print(a.generate_substrings("abc"))


# Check for Binary String
class Solution:
    def check_binary(self, s):
        for i in range(len(s)):
            if s[i] != '0' and s[i] != '1':
                return False
        return True
a = Solution()
print(a.check_binary("01010101010"))


# Camel case of a given sentence
class Solution:
    def camel_case(self, s):
        words = s.split()
        result = [words[0].lower()]
        for word in words[1:]:
            result.append(word.capitalize())
        return ''.join(result)
a = Solution()
print(a.camel_case("i got intern in geeksforgeeks"))


# Count of substrings that start and end with 1 in given Binary String
class Solution:
    def binary_substring(self, s):
        count = 0
        for char in s:
            if char =="1":
                count += 1
        n = count
        return (n * (n-1))//2            # here we are using (n * (n - 1)) // 2 not n+1
a = Solution()
print(a.binary_substring("10011"))


# Check if given String is Pangram or not
# Given a string s, check if it is Pangram or not. 
# A pangram is a sentence containing all letters of the English Alphabet.
# Input: s = "The quick brown fox jumps over the lazy dog" --> Output: true
class Solution:
    def check_panagram(self, s):
        freq = [0] * 26
        for char in s:
            if 'A' <= char <= 'Z':
                freq[ord(char) - ord('A')] += 1
            elif 'a' <= char <= 'z':
                freq[ord(char) - ord('a')] += 1
        for char in freq:
            if char == 0:
                return False
        return True
a = Solution()
print(a.check_panagram("The quick brown fox jumps over lazy dog"))


# Palindrome String
# Given a string s, the task is to check if it is palindrome or not.
# Input: s = "abba"  -->  Output: true
class Solution:
    def is_palindrome(self, s):
        s = list(s)
        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
a = Solution()
print(a.is_palindrome("malayalam"))


# Check if a string is substring of another
# Given two strings txt and pat, the task is to find if pat is a substring of txt. If yes, return the index of the first occurrence, else return -1.
# Input: txt = "geeksforgeeks", pat = "eks" --> Output: 2
class Solution:
    def check_substring(self, txt, pat):
        n = len(txt)
        m = len(pat)
        for i in range(n-m+1):
            if txt[i:i+m] == pat:
                return i
        return -1
a = Solution()
print(a.check_substring("geeksfogeeks", "eks"))


# Check if one string is subsequence of other
# Given two strings s1 and s2, find if the first string is a Subsequence of the second string, i.e. if s1 is a subsequence of s2.  
# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
# Input: s1 = "AXY", s2 = "ADXCPY" --> Output: true 
class Solution:
    def is_subsequence(self, s1, s2):
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)
a = Solution()
print(a.is_subsequence("AXY", "ADXCPY"))



# Check if two Strings are Anagrams of each other
# Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.
# Input: s1 = “geeks”  s2 = “kseeg” --> Output: true
class Solution:
    def are_anagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = [0] * 26
        for char in s1:
            freq[ord(char)- ord('a')] += 1
        for char in s2:
            freq[ord(char)- ord('a')] -= 1
        for char in freq:
            if freq[char] != 0:
                return False
        return True

a = Solution()
print(a.are_anagrams("geeks", "kseeg"))


# Using Dictionary - O(n + m) Time and O(1) Space
class Solution:
    def are_angram(self, s1, s2):
        freq = {}
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        for char in s2:
            freq[char] = freq.get(char, 0) - 1
        for char in freq.values():
            if char != 0:
                return False
        return True
a = Solution()
print(a.are_angram("geeks", "kseeg"))


# Check if two strings are k-anagrams or not
# Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.
# Note: Two strings are called k-anagrams if the following two conditions are true. 
# Both have same number of characters.
# Two strings can become anagram by changing at most k characters in a string.
class Solution:
    def check_k_anagrams(self, s1, s2, k):
        if len(s1) != len(s2):
            return False
        freq = [0] * 26
        for char in s1:
            freq[ord(char)- ord('a')] += 1
        for char in s2:
            freq[ord(char)- ord('a')] -= 1

        changing_count = 0
        for i in freq:
            if i > 0:
                changing_count += i
        return changing_count <= k
a = Solution()
print(a.check_k_anagrams("anagram", "grammar", 3))

